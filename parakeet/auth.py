# -*- coding: utf-8 -*-
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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

    def fill_email(self, email):
        self.browser.find_element_by_id('identifier').type(email)
        return self

    def click_next(self):
        self.browser.find_element_by_id('identifierNext').click()
        return self

    def fill_password(self, password):
        self.browser.splinter.is_element_visible_by_css('#password input', self.browser.waiting_time)
        self.browser.splinter.type('password', decode(password))
        return self

    def login(self):
        self.browser.find_element_by_id('passwordNext').click()
        return self

    def redirect_to_home(self):
        WebDriverWait(self.browser.selenium, 10).until(ec.title_contains(self.home_title))
        WebDriverWait(self.browser.selenium, 10).until(ec.invisibility_of_element_located((By.CLASS_NAME, 'main-loading')))
        return self
