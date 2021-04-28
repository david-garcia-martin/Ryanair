import unittest

from common.common_functions import initiate_driver, url, browser
from ryanair_test.ryanair_seating_page.seating_page_features import SeatingPage


class TestSeatingPage(SeatingPage, unittest.TestCase):
    browser = None

    @classmethod
    def setUpClass(cls):
        cls.browser = initiate_driver(browser)
        cls.browser.get(url)
        cls.url = url

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
