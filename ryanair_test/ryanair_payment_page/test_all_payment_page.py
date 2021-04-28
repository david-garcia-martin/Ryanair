import sys
import unittest

from common.common_functions import initiate_driver, url, browser, \
    cc, cc_cvv, get_random_fn_and_ln, address, address2, \
    city, zip_code, html_test_reporter_util, get_report_description
from ryanair_test.ryanair_payment_page.payment_page_features import PaymentPage


class TestPaymentPage(PaymentPage, unittest.TestCase):
    browser = None

    @classmethod
    def setUpClass(cls):
        cls.browser = initiate_driver(browser)
        cls.browser.get(url)
        cls.payment_information = [cc, cc_cvv, get_random_fn_and_ln()[0], address, address2, city, zip_code]
        cls.url = url

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    html_test_reporter_util(suite, 'RyanairTestPaymentErrorPage', 'Ryanair Payment Error page tests',
                            get_report_description())
