from __future__ import division
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
        If the element has a debounce, sleeps for 1.5x the debounce value.

        :param element: A Splinter input element object.
        """
        debounce_value = BasePageObject.extract_debounce_value(element)
        if debounce_value > 0:
            time.sleep(1.5 * debounce_value/1000)

    @staticmethod
    def extract_debounce_value(element):
        """
        Try to extract the AngularJS debounce value from ng-model-options attribute in the input element.

        Usually that attribute is something like this: ng-model-options="{ debounce: 300 }".

        :param element:  A Splinter input element object.
        :return: debounce value, 0 if does not have it.
        """
        debounce_value = "0"
        ng_model_options = element['ng-model-options']
        if ng_model_options is not None:
            result_debounce = re.search("""debounce"*'*:"*'*\s*"*'*(\d*)"*'*,*\s*""", ng_model_options, re.IGNORECASE)
            if result_debounce:
                debounce_value = result_debounce.group(1)
        return int(debounce_value)
