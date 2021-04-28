import random

from common.common_functions import wait_click, adults, children, wait_for_elements, wait_click_url


class SeatingPageLocators:
    seating_page_modal = '.seats-modal__cta'
    seating_page_seats = '.seatmap__seat'
    seating_page_available_seats = '.seatmap__seat--standard'
    seating_page_continue_button = '.seats-action__button'
    seating_dismiss_cta = '.enhanced-takeover-beta__product-dismiss-cta'


class SeatingPageUtil(object):
    @staticmethod
    def set_seating_modal(driver):
        wait_click(driver, css_select=SeatingPageLocators.seating_page_modal)

    @staticmethod
    def get_seating_available_seats(driver):
        return wait_for_elements(driver, css_select=SeatingPageLocators.seating_page_available_seats)

    @staticmethod
    def set_seats(driver):
        available_seats = len(SeatingPageUtil.get_seating_available_seats(driver))
        random_position = random.choice(range(0, available_seats))
        for index in range(0, adults + children):
            wait_click(driver, css_select=SeatingPageLocators.seating_page_available_seats,
                       index=random_position)

    @staticmethod
    def set_seating_continue_button(driver):
        wait_click(driver, css_select=SeatingPageLocators.seating_page_continue_button)

    @staticmethod
    def set_seating_page_dismiss_cta(driver):
        wait_click_url(driver, css_select=SeatingPageLocators.seating_dismiss_cta)
