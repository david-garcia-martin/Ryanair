import random
import time

from common.common_functions import wait_write, password, email, \
    wait_click, phone_number, wait_for_elements, country, wait_for_element_text


class PaymentPageLocators:
    log_in_popup_email_password = '.auth-popup .date-placeholder'
    log_in_button = '.auth-submit__button'
    phone_number_text_field = '.contact-details__input-tel .date-placeholder'
    insurance_button = '.insurance__checkbox'
    payment_information_text_fields = '.b2 .date-placeholder'
    payment_expiration_dropdowns = '.modal__input .select'
    payment_dropdown_items = '.dropdown-item__link'
    payment_country_dropdown = '._autocomplete_input'
    terms_and_conditions = '.terms-and-conditions__checkbox ._background'
    pay_now_button = '.pay-button'
    currency_dropdown = '.currency-converter__select .dropdown__toggle'
    payment_error_message = '.alert--error'


class PaymentPageUtil(object):

    @staticmethod
    def set_email_log_in(driver):
        wait_write(driver, email, css_select=PaymentPageLocators.log_in_popup_email_password)

    @staticmethod
    def set_password_log_in(driver):
        wait_write(driver, password, css_select=PaymentPageLocators.log_in_popup_email_password)

    @staticmethod
    def set_log_in_button(driver):
        wait_click(driver, css_select=PaymentPageLocators.log_in_button)

    @staticmethod
    def set_phone_number(driver):
        wait_write(driver, phone_number, css_select=PaymentPageLocators.phone_number_text_field)

    @staticmethod
    def set_insurance(driver):
        wait_click(driver, css_select=PaymentPageLocators.insurance_button)

    @staticmethod
    def set_payment_text_fields_information(driver, information):
        for index in range(0, len(information)):
            wait_write(driver, information[index], css_select=PaymentPageLocators.payment_information_text_fields)

    @staticmethod
    def get_expiration_dropdowns(driver):
        return wait_for_elements(driver, css_select=PaymentPageLocators.payment_expiration_dropdowns)

    @staticmethod
    def get_dropdown_items(driver):
        return wait_for_elements(driver, css_select=PaymentPageLocators.payment_dropdown_items)

    @staticmethod
    def set_cc_expiration_month_and_year(driver):
        expiration_dropdown_menus = PaymentPageUtil.get_expiration_dropdowns(driver)
        for index in range(0, len(expiration_dropdown_menus)):
            wait_click(driver, css_select=PaymentPageLocators.payment_expiration_dropdowns, index=index)
            random_item = random.choice(range(0, len(PaymentPageUtil.get_dropdown_items(driver))))
            wait_click(driver, css_select=PaymentPageLocators.payment_dropdown_items, index=random_item)

    @staticmethod
    def set_payment_country_dropdown(driver):
        wait_write(driver, country, css_select=PaymentPageLocators.payment_country_dropdown)
        wait_write(driver, '\n', css_select=PaymentPageLocators.payment_country_dropdown)

    @staticmethod
    def set_terms_and_conditions(driver):
        wait_click(driver, css_select=PaymentPageLocators.terms_and_conditions)

    @staticmethod
    def set_pay_now_button(driver):
        wait_click(driver, css_select=PaymentPageLocators.pay_now_button)

    @staticmethod
    def set_currency_dropdown_menu(driver):
        wait_click(driver, css_select=PaymentPageLocators.currency_dropdown)

    @staticmethod
    def set_currency_dropdown_item(driver):
        wait_click(driver, css_select=PaymentPageLocators.payment_dropdown_items, index=1)

    @staticmethod
    def get_payment_error_message(driver):
        return wait_for_element_text(driver, css_select=PaymentPageLocators.payment_error_message)
