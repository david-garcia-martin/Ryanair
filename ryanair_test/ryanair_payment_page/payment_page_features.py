import time

from common.common_functions import test_print
from ryanair_test.ryanair_bags_page.bag_page_locators import BagPageUtil
from ryanair_test.ryanair_extras_page.extras_page_locators import ExtrasPageUtil
from ryanair_test.ryanair_flight_page.flight_page_locators import FlightPageUtil
from ryanair_test.ryanair_home_page.home_page_locators import HomePageUtil
from ryanair_test.ryanair_payment_page.payment_page_locators import PaymentPageUtil
from ryanair_test.ryanair_seating_page.seating_page_locators import SeatingPageUtil


class PaymentPage(PaymentPageUtil):
    def test_payment_error_message(self):
        HomePageUtil.set_cookie_popup(self.browser)
        HomePageUtil.set_one_way_trip(self.browser)
        HomePageUtil.set_flight_departure(self.browser)
        HomePageUtil.set_flight_destination(self.browser)
        HomePageUtil.set_departure_date(self.browser)
        HomePageUtil.set_adults_passengers(self.browser)
        HomePageUtil.set_children_passengers(self.browser)
        HomePageUtil.set_passenger_confirm_button(self.browser)
        HomePageUtil.set_search_button(self.browser)

        FlightPageUtil.set_flight(self.browser)
        FlightPageUtil.set_flight_fare(self.browser)
        FlightPageUtil.set_login_later(self.browser)
        FlightPageUtil.set_passengers_first_name_last_name(self.browser)
        FlightPageUtil.set_passenger_title(self.browser)
        FlightPageUtil.set_flight_page_continue_button(self.browser)

        SeatingPageUtil.set_seating_modal(self.browser)
        SeatingPageUtil.set_seats(self.browser)
        SeatingPageUtil.set_seating_continue_button(self.browser)
        SeatingPageUtil.set_seating_page_dismiss_cta(self.browser)

        BagPageUtil.set_bag_selection(self.browser)
        BagPageUtil.set_bag_page_continue_button(self.browser)
        BagPageUtil.set_bag_page_dismiss_cta(self.browser)

        ExtrasPageUtil.set_extras_page_continue_button(self.browser)
        ExtrasPageUtil.set_extras_final_page_basket(self.browser)
        ExtrasPageUtil.set_basket_checkout(self.browser)

        PaymentPageUtil.set_email_log_in(self.browser)
        PaymentPageUtil.set_password_log_in(self.browser)
        PaymentPageUtil.set_log_in_button(self.browser)
        PaymentPageUtil.set_phone_number(self.browser)
        PaymentPageUtil.set_insurance(self.browser)
        PaymentPageUtil.set_payment_country_dropdown(self.browser)
        PaymentPageUtil.set_payment_text_fields_information(self.browser, self.payment_information)
        PaymentPageUtil.set_cc_expiration_month_and_year(self.browser)
        PaymentPageUtil.set_currency_dropdown_menu(self.browser)
        PaymentPageUtil.set_currency_dropdown_item(self.browser)
        PaymentPageUtil.set_terms_and_conditions(self.browser)
        PaymentPageUtil.set_pay_now_button(self.browser)
        time.sleep(0.6)
        try:
            error_message = self.get_payment_error_message(self.browser)
            test_print('Successfully verified error message: {0}'.format(error_message), flash='!')
        except Exception:
            raise AssertionError(
                'ERROR: Payment error message is missing on url: "{0}" '.format(self.browser.current_url))
