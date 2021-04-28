from common.common_functions import test_print
from ryanair_test.ryanair_seating_page.seating_page_locators import SeatingPageUtil


class SeatingPage(object):
    def test_flow(self):
        SeatingPageUtil.set_seating_modal(self.browser)
        SeatingPageUtil.set_seats(self.browser)
        SeatingPageUtil.set_seating_continue_button(self.browser)
        SeatingPageUtil.set_seating_page_dismiss_cta(self.browser)
        test_print(self.browser.current_url)
