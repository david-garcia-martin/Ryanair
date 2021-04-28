from common.common_functions import wait_click_url, wait_click


class ExtrasPageLocators:
    extras_page_continue_button = '.ry-button--full'
    extras_page_basket = '.basket-total'
    basket_checkout_button = '.ry-button--full '


class ExtrasPageUtil(object):

    @staticmethod
    def set_extras_page_continue_button(driver):
        wait_click_url(driver, css_select=ExtrasPageLocators.extras_page_continue_button)

    @staticmethod
    def set_extras_final_page_basket(driver):
        wait_click(driver, css_select=ExtrasPageLocators.extras_page_basket)

    @staticmethod
    def set_basket_checkout(driver):
        wait_click_url(driver, css_select=ExtrasPageLocators.basket_checkout_button)
