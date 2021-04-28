from common.common_functions import wait_click, wait_click_url


class BagPageLocators:
    bag_selection = '.ry-radio-circle-button__label'
    bag_continue_button = '.ry-button--gradient-yellow'
    bag_dismiss_cta = '.enhanced-takeover__product-dismiss-cta'


class BagPageUtil(object):

    @staticmethod
    def set_bag_selection(driver):
        # index=0 no bags
        wait_click(driver, css_select=BagPageLocators.bag_selection)

    @staticmethod
    def set_bag_page_continue_button(driver):
        wait_click(driver, css_select=BagPageLocators.bag_continue_button)

    @staticmethod
    def set_bag_page_dismiss_cta(driver):
        wait_click_url(driver, css_select=BagPageLocators.bag_dismiss_cta)
