# -*- coding: utf-8 -*-
from __future__ import division
import time
import re

from selenium.common.exceptions import TimeoutException
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from random import randint
from time import sleep
from parakeet.lettuce_logger import LOG

from .utils import next_image


class ParakeetElement(object):
    """
    A wrapper around Selenium WebElement for AngularJS and AngularJS Material projects.

    Attributes:
        element: The Selenium WebElement object.
        locator: A tuple of (by, path) from Selenium API.
        parakeet: The instance of ParakeetBrowser.
    """
    def __init__(self, element, locator, parakeet):
        self.element = element
        self.locator = locator
        self.parakeet = parakeet

    def clear(self):
        self.element = self.wait_visibility_of_element_located()
        self.element.clear()
        return self

    def click(self):
        try:
            self.parakeet.retry(method=self.click_once)
        except Exception as ex:
            LOG.error('Attempts exceeded')

        return self

    def click_once(self):
        self.element = self.wait_element_to_be_clickable()
        self.element.click()
        return self

    def click_and_wait_disappear(self):
        self.click()
        self.wait_invisibility_of_element_located()
        return self

    def type(self, value, type_pause=0):
        _type_pause = type_pause if type_pause > 0 else self.parakeet.type_pause
        LOG.debug('type {} {}'.format(value.encode('utf-8', 'replace'), _type_pause))
        self.element = self.wait_visibility_of_element_located()
        self._type_handle(_type_pause, value)

        self.debounce()

        return self

    def _type_handle(self, _type_pause, value):
        if _type_pause > 0:
            self._type_slowly(value, _type_pause)
        else:
            LOG.debug('type_normal {}'.format(value.encode('utf-8', 'replace')))
            self.element.send_keys(value)

    def _type_slowly(self, value, type_pause):
        LOG.debug('type_slowly {}'.format(value.encode('utf-8', 'replace')))

        if not (type_pause and isinstance(type_pause, float) and 0.0 < type_pause < 1):
            raise ValueError(
                'The type_pause argument need to be an float valid number between 0.01 and 0.99'
            )

        for character in value:
            self.element.send_keys(character)
            time.sleep(type_pause)

        return self

    def get_attribute(self, name):
        return self.element.get_attribute(name)

    def wait_visibility_of_element_located(self):
        return WebDriverWait(self.parakeet.selenium, self.parakeet.waiting_time, self.parakeet.poll_frequency).until(
            ec.visibility_of_element_located(self.locator)
        )

    def wait_invisibility_of_element_located(self):
        return WebDriverWait(self.parakeet.selenium, self.parakeet.waiting_time, self.parakeet.poll_frequency).until(
            ec.invisibility_of_element_located(self.locator)
        )

    def wait_element_to_be_clickable(self):
        return WebDriverWait(self.parakeet.selenium, self.parakeet.waiting_time, self.parakeet.poll_frequency).until(
            ec.element_to_be_clickable(self.locator)
        )

    def debounce(self):
        """
        If the element has an AngularJS debounce set, it sleeps for 1.5x the debounce value.
        """
        ng_model_options_value = self.get_attribute('ng-model-options')

        if ng_model_options_value is not None:
            debounce_value = ParakeetElement.extract_debounce_value(ng_model_options_value)
            if debounce_value > 0:
                time.sleep(1.5 * debounce_value/1000)

    @staticmethod
    def extract_debounce_value(attribute_value):
        """
        Try to extract the AngularJS debounce value from ng-model-options value.

        Usually that attribute value is something like this: '{ debounce: 300 }'.

        :param attribute_value:  The string representing the ng-model-options attribute value.
        :return: debounce value, or 0 if does not have one.
        """
        debounce_value = "0"
        result_debounce = re.search("""debounce"*'*:"*'*\s*"*'*(\d*)"*'*,*\s*""", attribute_value, re.IGNORECASE)
        if result_debounce:
            debounce_value = result_debounce.group(1)
        return int(debounce_value)


class ParakeetBrowser(object):
    """
    A wrapper around Splinter / Selenium for AngularJS and AngularJS Material projects.

    Attributes:
        config: The Parakeet/project config dictionary.
        splinter: The Splinter browser/driver instance.
        selenium: The Selenium driver instance.
        waiting_time: Maximum time in seconds to wait for an action.
    """

    def __init__(self, config):
        self.config = config
        self.splinter = Browser(config.get('browser'), headless=config.get('headless'))
        self.selenium = self.splinter.driver
        self.waiting_time = int(config.get('default_implicitly_wait_seconds'))
        self.poll_frequency = int(config.get('default_poll_frequency_seconds'))
        self.snapshot_debug = config.get('snapshot_debug', False)
        self.color_log = config.get('color_log', False)
        self.type_pause = float(config.get('type_pause', 0))
        self.retry_get_element = int(config.get('retry', 1))
        self.selenium.implicitly_wait(self.waiting_time)
        self.selenium.set_window_size(int(config['window_size']['width']),
                                      int(config['window_size']['height']))

    def find_element_by_id(self, element_id, waiting_time=None):
        LOG.debug('find_element_by_id({})'
                  .format(element_id))
        locator = (By.ID, element_id)
        element = self.get_element_waiting_for_its_presence(locator, waiting_time)
        return ParakeetElement(element, locator, self)

    def find_element_by_xpath(self, element_xpath):
        LOG.debug('find_element_by_xpath({})'
                  .format(element_xpath))
        locator = (By.XPATH, element_xpath)
        element = self.get_element_waiting_for_its_presence(locator)
        return ParakeetElement(element, locator, self)

    def is_element_present_by_id(self, element_id):
        LOG.debug('is_element_present_by_id({})'
                  .format(element_id))
        return self.splinter.is_element_present_by_id(element_id, self.waiting_time)

    def is_element_present_by_xpath(self, element_xpath, p_waiting_time=None):
        _waiting_time = p_waiting_time if p_waiting_time else self.waiting_time
        LOG.debug('is_element_present_by_xpath({}, {})'
                  .format(element_xpath, _waiting_time))
        return self.splinter.is_element_present_by_xpath(element_xpath, _waiting_time)

    def is_text_present(self, text):
        LOG.debug('is_text_present({})'
                  .format(text))
        return self.splinter.is_text_present(text)

    def quit(self):
        LOG.debug('quit')
        self.splinter.quit()

    def visit(self, url):
        LOG.debug('visit')
        self.splinter.visit(url)

    def visit_home(self):
        LOG.debug('visit_home')
        self.visit(self.config['home_url'])

    def get_element_waiting_for_its_presence(self, locator, waiting_time=None):
        _waiting_time = waiting_time if waiting_time else self.waiting_time
        LOG.debug('get_element_waiting_for_its_presence({}, {}, {})'
                  .format(locator, _waiting_time, self.poll_frequency))
        element = None

        try:
            element = WebDriverWait(self.selenium, _waiting_time, self.poll_frequency).until(
                ec.presence_of_element_located(locator)
            )
        except TimeoutException:
            LOG.error("Time is up! {}s".format(_waiting_time))
            self.selenium\
                .save_screenshot('parakeet_timeout_error_{:05d}.png'
                                 .format(next_image()))

        return element

    def get_element_waiting_for_its_presence_by_xpath(self, xpath, waiting_time=None):
        _waiting_time = waiting_time if waiting_time else self.waiting_time
        LOG.debug('get_element_waiting_for_its_presence_by_xpath({}, {}, {})'
                  .format(xpath, _waiting_time, self.poll_frequency))
        return self.get_element_waiting_for_its_presence((By.XPATH, xpath), _waiting_time)

    # noinspection PyBroadException
    def retry(self, method=None, **kwargs):
        """
        Method retry the execution
        :param method:
        :param kwargs:
        :return:
        """
        _next = 'next_iterator'
        _retry = self.retry_get_element
        _next_iterator = kwargs.get(_next, 1)

        try:
            LOG.debug('Trying {}/{} to perform method {}'
                      .format(_next_iterator, _retry, method.__name__))

            kwargs.pop(_next, None)
            result = method(**kwargs)

            if isinstance(result, bool) and \
                    not result and \
                    _next_iterator < _retry:
                    return self._perform_method(_next, _next_iterator, kwargs, method)

            return result
        except Exception as ex:
            LOG.warn('Exception: {}'.format(str(ex)))
            if 'md-backdrop' in str(ex):
                self._remove_back_drop()

            if 'md-scroll-mask' in str(ex):
                self._remove_scroll_back()

            if _next_iterator < _retry:
                return self._perform_method(_next, _next_iterator, kwargs, method)

            self.selenium.save_screenshot('parakeet_error_{:05d}_{}.png'
                                          .format(next_image(), method.__name__))
            LOG.error('Exception: {}'.format(str(ex)))
            raise ex

    def _remove_scroll_back(self):
        LOG.info('---- Remove md-scroll-mask ---')
        self.splinter.execute_script("document.getElementsByClassName('md-scroll-mask')[0]['style']['display'] = 'none'")

    def _remove_back_drop(self):
        LOG.info('---- Remove md-backdrop ---')
        self.splinter.execute_script("document.getElementsByTagName('md-backdrop')[0].style.display = 'none'")

    def _perform_method(self, next, next_iterator, kwargs, method):
        """
        Perform the method and return the value
        :param next:
        :param next_iterator:
        :param kwargs:
        :param method:
        :return:
        """
        kwargs[next] = next_iterator + 1
        sleep(randint(1, 3))
        return self.retry(method=method, **kwargs)
