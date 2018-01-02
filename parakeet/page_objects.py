# -*- coding: utf-8 -*-


class BasePageObject(object):
    """A base class for all page objects.

    Attributes:
        browser: The ParakeetBrowser instance.
    """

    def __init__(self, browser):
        self.browser = browser


