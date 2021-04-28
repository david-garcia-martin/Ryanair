from common.common_functions import test_print
from ryanair_test.ryanair_flight_page.flight_page_locators import FlightPageUtil


class FlightPage(object):
    def test_flow(self):
        FlightPageUtil.set_flight(self.browser)
        FlightPageUtil.set_flight_fare(self.browser)
        FlightPageUtil.set_login_later(self.browser)
        FlightPageUtil.set_passengers_first_name_last_name(self.browser)
        FlightPageUtil.set_passenger_title(self.browser)
        FlightPageUtil.set_flight_page_continue_button(self.browser)
        test_print(self.browser.current_url)
