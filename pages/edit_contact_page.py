from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class EditContactPage(BasePage):
    FIRST_NAME_FIELD = (By.ID, "firstName")
    LAST_NAME_FIELD = (By.ID, "lastName")
    DATE_OF_BIRTH_FIELD = (By.ID, "birthdate")
    EMAIL_FIELD = (By.ID, "email")
    PHONE_FIELD = (By.ID, "phone")
    STREET1_FIELD = (By.ID, "street1")
    STREET2_FIELD = (By.ID, "street2")
    CITY_FIELD = (By.ID, "city")
    STATE_FIELD = (By.ID, "stateProvince")
    POSTAL_CODE_FIELD = (By.ID, "postalCode")
    COUNTRY_FIELD = (By.ID, "country")
    SUBMIT_BUTTON = (By.ID, "submit")
    CANCEL_BUTTON = (By.ID, "cancel")
    LOGOUT_BUTTON = (By.ID, "logout")
    EDIT_CONTACT_TEXT = (By.XPATH, "//h1[text()='Edit Contact']")

    def __init__(self,driver):
        super().__init__(driver)

    def edit_first_name(self, first_name):
        try:
            self.logger.info(f"Attempting to edit first name!!")
            self.do_send_keys(self.FIRST_NAME_FIELD, first_name)
            self.logger.info(f"Successfully edited first name!!")
        except Exception as e:
            self.logger.error(f"Attempt to edit first name unsuccessful due to {e}")

    def edit_last_name(self, last_name):
        try:
            self.logger.info(f"Attempting to edit last name!!")
            self.do_send_keys(self.LAST_NAME_FIELD, last_name)
            self.logger.info(f"Successfully edited last name!!")
        except Exception as e:
            self.logger.error(f"Attempt to edit last name unsuccessful due to {e}")

    def edit_date_of_birth(self, date_of_birth):
        try:
            self.logger.info(f"Attempting to edit date of birth!!")
            self.do_send_keys(self.DATE_OF_BIRTH_FIELD, date_of_birth)
            self.logger.info(f"Successfully edited date of birth!!")
        except Exception as e:
            self.logger.error(f"Attempt to edit date of birth unsuccessful due to {e}")

    def edit_email(self, email):
        try:
            self.logger.info(f"Attempting to edit email!!")
            self.do_send_keys(self.EMAIL_FIELD, email)
            self.logger.info(f"Successfully edited email!!")
        except Exception as e:
            self.logger.error(f"Attempt to edit email unsuccessful due to {e}")

    def edit_phone(self, phone):
        try:
            self.logger.info(f"Attempting to edit phone!!")
            self.do_send_keys(self.PHONE_FIELD, phone)
            self.logger.info(f"Successfully edited phone!!")
        except Exception as e:
            self.logger.error(f"Attempt to edit phone unsuccessful due to {e}")

    def edit_street1(self, street1):
        try:
            self.logger.info(f"Attempting to edit street1!!")
            self.do_send_keys(self.STREET1_FIELD, street1)
            self.logger.info(f"Successfully edited street1!!")
        except Exception as e:
            self.logger.error(f"Attempt to edit street1 unsuccessful due to {e}")

    def edit_street2(self, street2):
        try:
            self.logger.info(f"Attempting to edit street2!!")
            self.do_send_keys(self.STREET2_FIELD, street2)
            self.logger.info(f"Successfully edited street2!!")
        except Exception as e:
            self.logger.error(f"Attempt to edit street2 unsuccessful due to {e}")

    def edit_city(self, city):
        try:
            self.logger.info(f"Attempting to edit city!!")
            self.do_send_keys(self.CITY_FIELD, city)
            self.logger.info(f"Successfully edited city!!")
        except Exception as e:
            self.logger.error(f"Attempt to edit city unsuccessful due to {e}")

    def edit_state(self, state):
        try:
            self.logger.info(f"Attempting to edit state!!")
            self.do_send_keys(self.STATE_FIELD, state)
            self.logger.info(f"Successfully edited state!!")
        except Exception as e:
            self.logger.error(f"Attempt to edit state unsuccessful due to {e}")

    def edit_postal_code(self, postal_code):
        try:
            self.logger.info(f"Attempting to edit postal code!!")
            self.do_send_keys(self.POSTAL_CODE_FIELD, postal_code)
            self.logger.info(f"Successfully edited postal code!!")
        except Exception as e:
            self.logger.error(f"Attempt to edit postal code unsuccessful due to {e}")

    def edit_county(self, county):
        try:
            self.logger.info(f"Attempting to edit county!!")
            self.do_send_keys(self.COUNTRY_FIELD, county)
            self.logger.info(f"Successfully edited county!!")
        except Exception as e:
            self.logger.error(f"Attempt to edit county unsuccessful due to {e}")

    def click_submit_button(self):
        try:
            self.do_click(self.SUBMIT_BUTTON)
            self.logger.info(f"Successfully clicked submit button!!")
        except Exception as e:
            self.logger.error(f"Unable to click submit button: {e}")

    def click_cancel_button(self):
        try:
            self.logger.info(f"Attempting to click cancel button!!")
            self.do_click(self.CANCEL_BUTTON)
            self.logger.info(f"Successfully clicked cancel button!!")
        except Exception as e:
            self.logger.error(f"Unable to click cancel button: {e}")

    def click_logout_button(self):
        try:
            self.do_click(self.LOGOUT_BUTTON)
            self.logger.info(f"Successfully clicked logout button!!")
        except Exception as e:
            self.logger.error(f"Unable to click logout button: {e}")

    def is_visible_edit_contact(self):
        return self.is_visible(self.EDIT_CONTACT_TEXT, timeout=5)
