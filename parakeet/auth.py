# -*- coding: utf-8 -*-
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        :type browser: splinter.Browser

        :param home_title: the home page title you expect after logging in.
        :type home_title: str
        """
        self.browser = browser
        self.home_title = home_title

    def fill_email(self, email):
        self.browser.is_element_present_by_id('identifierId', wait_time=10)
        self.browser.fill('identifier', email)
        return self

    def click_next(self):
        self.browser.is_element_present_by_id('identifierNext', wait_time=10)
        self.browser.find_by_id('identifierNext').click()
        return self

    def fill_password(self, password):
        self.browser.is_element_visible_by_css('#password input', wait_time=10)
        self.browser.type('password', decode(password))
        return self

    def login(self):
        self.browser.is_element_present_by_id('passwordNext', wait_time=10)
        WebDriverWait(self.browser.driver, 10).until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
        self.browser.find_by_id('passwordNext').click()
        return self

    def redirect_to_home(self):
        WebDriverWait(self.browser.driver, 10).until(EC.title_contains(self.home_title))
        WebDriverWait(self.browser.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'main-loading')))
        return self
