# -*- coding: utf-8 -*-
from __future__ import division
import time
import re
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
        self.element = self.wait_element_to_be_clickable()
        self.element.click()
        return self

    def click_and_wait_disappear(self):
        self.click()
        self.wait_invisibility_of_element_located()
        return self

    def type(self, value):
        self.element = self.wait_visibility_of_element_located()
        self.element.send_keys(value)
        self.debounce()
        return self

    def get_attribute(self, name):
        return self.element.get_attribute(name)

    def wait_visibility_of_element_located(self):
        return WebDriverWait(self.parakeet.selenium, self.parakeet.waiting_time).until(
            ec.visibility_of_element_located(self.locator)
        )

    def wait_invisibility_of_element_located(self):
        return WebDriverWait(self.parakeet.selenium, self.parakeet.waiting_time).until(
            ec.invisibility_of_element_located(self.locator)
        )

    def wait_element_to_be_clickable(self):
        return WebDriverWait(self.parakeet.selenium, self.parakeet.waiting_time).until(
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
        self.splinter = Browser(config['browser'])
        self.selenium = self.splinter.driver
        self.waiting_time = int(config['default_implicitly_wait_seconds'])
        self.selenium.implicitly_wait(self.waiting_time)
        self.selenium.set_window_size(int(config['window_size']['width']), int(config['window_size']['height']))

    def find_element_by_id(self, element_id):
        locator = (By.ID, element_id)
        element = self.get_element_waiting_for_its_presence(locator)
        return ParakeetElement(element, locator, self)

    def find_element_by_xpath(self, element_xpath):
        locator = (By.XPATH, element_xpath)
        element = self.get_element_waiting_for_its_presence(locator)
        return ParakeetElement(element, locator, self)

    def is_element_present_by_id(self, element_id):
        return self.splinter.is_element_present_by_id(element_id, self.waiting_time)

    def is_element_present_by_xpath(self, element_xpath):
        return self.splinter.is_element_present_by_xpath(element_xpath, self.waiting_time)

    def is_text_present(self, text):
        return self.splinter.is_text_present(text)

    def quit(self):
        self.splinter.quit()

    def visit(self, url):
        self.splinter.visit(url)

    def visit_home(self):
        self.visit(self.config['home_url'])

    def get_element_waiting_for_its_presence(self, locator):
        element = WebDriverWait(self.selenium, self.waiting_time).until(
            ec.presence_of_element_located(locator)
        )
        return element

