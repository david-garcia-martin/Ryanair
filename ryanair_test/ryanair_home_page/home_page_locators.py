import random

from common.common_functions import origin, destination, adults, children, wait_write, wait_click, wait_for_elements, \
    wait_click_url


class HomePageLocators:
    home_page_flight_departure = '#input-button__departure'
    home_page_flight_destination = '#input-button__destination'
    home_page_flight_airport = '.airport-item'
    home_page_one_way_trip = '.trip-type__button'
    home_page_calendar_dates = '.calendar-body__cell'
    home_page_calender_date_disabled = 'calendar-body__cell--disabled'
    home_page_passenger_type = '.passengers-picker__passenger-type'
    home_page_adult_passenger = 'passengers-picker__adults'
    home_page_children_passenger = 'passengers-picker__children'
    home_page_passenger_counter_button = '.counter__button-wrapper--enabled'
    home_page_passenger_confirm_button = '.passengers__confirm-button'
    home_page_search_button = '.flight-search-widget__start-search'
    home_page_cookie_popup = '.cookie-popup-with-overlay__button'
    home_page_increment_buttons = 'counter.counter__increment'


class HomePageUtil(object):

    @staticmethod
    def set_cookie_popup(driver):
        wait_click(driver, css_select=HomePageLocators.home_page_cookie_popup)

    @staticmethod
    def set_flight_airport(driver):
        wait_click(driver, css_select=HomePageLocators.home_page_flight_airport)

    @staticmethod
    def set_one_way_trip(driver):
        one_way_button = [x for x in wait_for_elements(driver, css_select=HomePageLocators.home_page_one_way_trip) if
                          'One way' in x.get_attribute('aria-label')]
        one_way_button[0].click()

    @staticmethod
    def set_flight_departure(driver):
        wait_write(driver, origin, css_select=HomePageLocators.home_page_flight_departure)
        HomePageUtil.set_flight_airport(driver)

    @staticmethod
    def set_flight_destination(driver):
        wait_write(driver, destination, css_select=HomePageLocators.home_page_flight_destination)
        HomePageUtil.set_flight_airport(driver)

    @staticmethod
    def set_departure_date(driver):
        all_dates = wait_for_elements(driver, css_select=HomePageLocators.home_page_calendar_dates)
        # I'm removing today's date
        available_dates = [x for x in all_dates if
                           HomePageLocators.home_page_calender_date_disabled not in x.get_attribute('class')][1:]
        selected_date = random.choice(available_dates)
        wait_click(driver, css_select=HomePageLocators.home_page_calendar_dates, index=all_dates.index(selected_date))

    @staticmethod
    def set_adults_passengers(driver):
        all_passenger_types = [x for x in
                               wait_for_elements(driver, css_select=HomePageLocators.home_page_passenger_type)]
        adult_passenger = [x for x in all_passenger_types
                           if HomePageLocators.home_page_adult_passenger in x.get_attribute('data-ref')][0]
        for i in range(1, adults):
            wait_click(driver, css_select=HomePageLocators.home_page_passenger_counter_button,
                       index=all_passenger_types.index(adult_passenger))

    @staticmethod
    def set_children_passengers(driver):
        all_passenger_types = [x for x in
                               wait_for_elements(driver, css_select=HomePageLocators.home_page_passenger_type)]
        children_passenger = [x for x in all_passenger_types if
                              HomePageLocators.home_page_children_passenger in x.get_attribute('data-ref')][0]
        all_buttons = [x for x in
                       wait_for_elements(driver, css_select=HomePageLocators.home_page_passenger_counter_button)]
        increment_buttons = [x for x in all_buttons if
                             HomePageLocators.home_page_increment_buttons in x.get_attribute('data-ref')]

        for i in range(children):
            increment_buttons[all_passenger_types.index(children_passenger)].click()

    @staticmethod
    def set_passenger_confirm_button(driver):
        wait_click(driver, css_select=HomePageLocators.home_page_passenger_confirm_button)

    @staticmethod
    def set_search_button(driver):
        wait_click_url(driver, css_select=HomePageLocators.home_page_search_button)
