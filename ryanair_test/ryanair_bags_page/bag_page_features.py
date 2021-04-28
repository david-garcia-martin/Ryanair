from common.common_functions import test_print
from ryanair_test.ryanair_bags_page.bag_page_locators import BagPageUtil


class BagPage(object):
    def test_flow(self):
        BagPageUtil.set_bag_selection(self.browser)
        BagPageUtil.set_bag_page_continue_button(self.browser)
        BagPageUtil.set_bag_page_dismiss_cta(self.browser)
        test_print(self.browser.current_url)
