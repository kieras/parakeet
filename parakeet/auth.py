# -*- coding: utf-8 -*-
import base64, time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from parakeet.lettuce_logger import LOG


def decode(password):
    """
    Decode a base64 encoded password.

    :param password: base64 encoded password.
    :type password: str

    :return: decoded password.
    """
    return base64.b64decode(password)


class LoginPage:

    def __init__(self, browser, home_title):
        """

        :param browser: the browser.
        :type browser: ParakeetBrowser

        :param home_title: the home page title you expect after logging in.
        :type home_title: str
        """
        self.browser = browser
        self.home_title = home_title

        self.window = ''

    def fill_email(self, email):
        LOG.debug('fill_email')
        try:
            self.browser.find_element_by_id('identifierId').type(email)
        except TimeoutException:
            LOG.debug('click_on_identifier_before_fill_email')
            self.browser.find_element_by_xpath('//ul/li[last()]/div[@role="link"]').click()
            self.browser.find_element_by_id('identifierId').type(email)

        return self

    def click_next(self):
        LOG.debug('click_next')
        self.browser.find_element_by_id('identifierNext').click()
        return self

    def fill_password(self, password):
        LOG.debug('fill_password')
        self.browser.splinter.\
            is_element_visible_by_css('#password input', self.browser.waiting_time)
        self.browser.splinter.type('password', decode(password))
        return self

    def login(self):
        LOG.debug('login')
        self.browser.find_element_by_id('passwordNext').click()
        return self

    def redirect_to_home(self):
        LOG.debug('redirect_to_home')
        WebDriverWait(self.browser.selenium, self.browser.waiting_time, self.browser.poll_frequency)\
            .until(ec.title_contains(self.home_title))
        WebDriverWait(self.browser.selenium, self.browser.waiting_time, self.browser.poll_frequency)\
            .until(ec.invisibility_of_element_located((By.CLASS_NAME, 'main-loading')))
        return self

    def click_sign_in(self):
        LOG.debug('click_sign_in')
        self.browser.find_element_by_xpath('//md-card-actions/button').click()
        time.sleep(1)
        return self

    def switch_windows_before(self):
        LOG.debug('switch_windows_before')
        self.browser.selenium.switch_to_window(self.window)
        return self

    def switch_windows_after(self):
        LOG.debug('switch_windows_after')
        popup = self.browser.selenium.window_handles[1]
        self.browser.selenium.switch_to_window(popup)
        return self

    def set_window(self):
        LOG.debug('set_window')
        self.window = self.browser.selenium.window_handles[0]
        return self

    def click_to_log_with_another_account(self):
        LOG.debug('click_to_log_with_another_account')
        element = '//*[@id="view_container"]/div/div/div[2]/div/div/div/form/content/section/div/content/div/div/ul/li[2]/div'
        if self.browser.is_element_present_by_xpath(element):
            LOG.debug('another account option is present, lets click on it')
            self.browser.find_element_by_xpath(element).click()
        return self
