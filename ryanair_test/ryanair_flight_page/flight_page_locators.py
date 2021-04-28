import random

from common.common_functions import wait_click, get_random_fn_and_ln, wait_write, wait_for_elements, adults, \
    wait_click_url


class FlightPageLocators:
    flight_page_flight_card = '.flight'
    flight_page_flight_fare = '.fare-card__price'
    flight_page_login_later = '.login-touchpoint__login-later'
    flight_page_passenger_information = '.details-form-container input'
    flight_page_passenger_title_dropdown = '.details-form-container .dropdown'
    flight_page_passenger_title_items = '.dropdown-item__label'
    flight_page_continue_button = '.continue-flow__button'


class FlightPageUtil(object):

    @staticmethod
    def set_flight(driver):
        wait_click(driver, css_select=FlightPageLocators.flight_page_flight_card)

    @staticmethod
    def set_flight_fare(driver):
        wait_click(driver, css_select=FlightPageLocators.flight_page_flight_fare)

    @staticmethod
    def set_login_later(driver):
        wait_click(driver, css_select=FlightPageLocators.flight_page_login_later)

    @staticmethod
    def set_passengers_first_name_last_name(driver):
        fn_ln_list = get_random_fn_and_ln()
        for index in range(len(fn_ln_list)):
            wait_write(driver, fn_ln_list[index], css_select=FlightPageLocators.flight_page_passenger_information,
                       index=index)

    @staticmethod
    def set_passenger_title_dropdwon(driver, index):
        wait_click(driver, css_select=FlightPageLocators.flight_page_passenger_title_dropdown, index=index)

    @staticmethod
    def set_passenger_title(driver):
        for index in range(0, adults):
            FlightPageUtil.set_passenger_title_dropdwon(driver, index=index)
            dropdown_items = wait_for_elements(driver, css_select=FlightPageLocators.flight_page_passenger_title_items)
            wait_click(driver, css_select=FlightPageLocators.flight_page_passenger_title_items,
                       index=random.choice(range(0, len(dropdown_items))))

    @staticmethod
    def set_flight_page_continue_button(driver):
        wait_click_url(driver, css_select=FlightPageLocators.flight_page_continue_button)
