import unittest

from common.common_functions import initiate_driver, url, browser
from ryanair_test.ryanair_bags_page.bag_page_features import BagPage


class TestBagPage(BagPage, unittest.TestCase):
    browser = None

    @classmethod
    def setUpClass(cls):
        cls.browser = initiate_driver(browser)
        cls.browser.get(url)
        cls.url = url

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
