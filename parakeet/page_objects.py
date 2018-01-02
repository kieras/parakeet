from __future__ import division
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec


class BasePageObject(object):
    """A base class for all page objects.

    Attributes:
        browser: The Splinter browser instance.
        config: The config dictionary.
    """

    def __init__(self, browser):
        self.browser = browser

    def wait_element_to_be_clickable(self, expr, by_locator_strategy=By.XPATH, timeout=10):
        return WebDriverWait(self.browser.driver, timeout)\
            .until(ec.element_to_be_clickable((by_locator_strategy, expr)))

    def wait_visibility_of_element_located(self, expr, by_locator_strategy=By.XPATH, timeout=10):
        return WebDriverWait(self.browser.driver, timeout)\
            .until(ec.visibility_of_element_located((by_locator_strategy, expr)))

    def wait_invisibility_of_element_located(self, expr, by_locator_strategy=By.XPATH, timeout=10):
        return WebDriverWait(self.browser.driver, timeout) \
            .until(ec.invisibility_of_element_located((by_locator_strategy, expr)))

    @staticmethod
    def debounce(element):
        """
        If the element has an AngularJS debounce set, it sleeps for 1.5x the debounce value.

        :param element: An input element object.
        """
        ng_model_options_value = BasePageObject.getAttribute(element, 'ng-model-options')

        if ng_model_options_value is not None:
            debounce_value = BasePageObject.extract_debounce_value(ng_model_options_value)
            if debounce_value > 0:
                time.sleep(1.5 * debounce_value/1000)

    @staticmethod
    def extract_debounce_value(ng_model_options_value):
        """
        Try to extract the AngularJS debounce value from ng-model-options value.

        Usually that attribute value is something like this: '{ debounce: 300 }'.

        :param attr_value:  The string representing the ng-model-options attribute value.
        :return: debounce value, or 0 if does not have one.
        """
        debounce_value = "0"
        result_debounce = re.search("""debounce"*'*:"*'*\s*"*'*(\d*)"*'*,*\s*""", ng_model_options_value, re.IGNORECASE)
        if result_debounce:
            debounce_value = result_debounce.group(1)
        return int(debounce_value)

    @staticmethod
    def get_attribute(element, attribute_name):
        """
        Gets an attribute value from a web element.
        Works with Selenium or Splinter elements.

        :param element: A Selenium or Splinter web element
        :param attribute_name: The attribute's name
        :return: the attribute value, or None if it does not exists
        """
        attribute_value = None
        if isinstance(element, WebElement):
            # Selenium element
            attribute_value = element.get_attribute(attribute_name)
        else:
            # Splinter element
            attribute_value = element[attribute_name]
        return attribute_value

