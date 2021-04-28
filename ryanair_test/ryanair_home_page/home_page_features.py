from common.common_functions import test_print
from ryanair_test.ryanair_home_page.home_page_locators import HomePageUtil


class HomePage(object):
    def test_flow(self):
        HomePageUtil.set_cookie_popup(self.browser)
        HomePageUtil.set_one_way_trip(self.browser)
        HomePageUtil.set_flight_departure(self.browser)
        HomePageUtil.set_flight_destination(self.browser)
        HomePageUtil.set_departure_date(self.browser)
        HomePageUtil.set_adults_passengers(self.browser)
        HomePageUtil.set_children_passengers(self.browser)
        HomePageUtil.set_passenger_confirm_button(self.browser)
        HomePageUtil.set_search_button(self.browser)
        test_print(self.browser.current_url)
