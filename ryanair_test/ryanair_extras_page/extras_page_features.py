from common.common_functions import test_print
from ryanair_test.ryanair_extras_page.extras_page_locators import ExtrasPageUtil


class ExtrasPage(object):
    def test_flow(self):
        ExtrasPageUtil.set_extras_page_continue_button(self.browser)
        ExtrasPageUtil.set_extras_final_page_basket(self.browser)
        ExtrasPageUtil.set_basket_checkout(self.browser)
        test_print(self.browser.current_url)
