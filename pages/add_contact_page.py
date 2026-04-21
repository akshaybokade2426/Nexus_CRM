from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class AddContactPage(BasePage):

    FIRST_NAME_FIELD = (By.ID, "firstName")
    LAST_NAME_FIELD = (By.ID, "lastName")
    DATE_OF_BIRTH_FIELD = (By.ID, "birthdate")
    EMAIL_FIELD = (By.ID, "email")
    PHONE_FIELD = (By.ID, "phone")
    ADDRESS1_FIELD = (By.ID, "street1")
    ADDRESS2_FIELD = (By.ID, "street2")
    CITY_FIELD = (By.ID, "city")
    STATE_FIELD = (By.ID, "stateProvince")
    POSTAL_CODE_FIELD = (By.ID, "postalCode")
    COUNTRY_FIELD = (By.ID, "country")
    SUBMIT_BUTTON =(By.ID, "submit")
    CANCEL_BUTTON =(By.ID, "cancel")
    LOGOUT_BUTTON =(By.ID, "logout")
    ADD_CONTACT_TEXT = (By.XPATH, "//h1[text()='Add Contact']")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_contact_form(self, first_name, last_name, date_of_birth, email, phone, address1, address2, city, state, postal_code, country):
        self.logger.info(f"Filling contact form..............")
        try:

            self.do_send_keys(self.FIRST_NAME_FIELD, first_name)
            self.do_send_keys(self.LAST_NAME_FIELD, last_name)
            self.do_send_keys(self.DATE_OF_BIRTH_FIELD, date_of_birth)
            self.do_send_keys(self.EMAIL_FIELD, email)
            self.do_send_keys(self.PHONE_FIELD, phone)
            self.do_send_keys(self.ADDRESS1_FIELD, address1)
            self.do_send_keys(self.ADDRESS2_FIELD, address2)
            self.do_send_keys(self.CITY_FIELD, city)
            self.do_send_keys(self.STATE_FIELD, state)
            self.do_send_keys(self.POSTAL_CODE_FIELD, postal_code)
            self.do_send_keys(self.COUNTRY_FIELD, country)
            self.do_click(self.SUBMIT_BUTTON)
        except Exception as e:
            self.logger.error(f"{e}")

    def click_cancel_button(self):
        self.logger.info(f"Cancelling contact form..............")
        self.do_click(self.CANCEL_BUTTON)

    def click_logout_button(self):
        self.logger.info(f"Logging out contact form..............")
        self.do_click(self.LOGOUT_BUTTON)

    def is_visible_add_contact(self):
        return self.is_visible(self.ADD_CONTACT_TEXT, timeout=5)