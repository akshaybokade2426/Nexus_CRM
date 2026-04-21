from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignUpPage(BasePage):

    FIRST_NAME_FIELD = (By.ID, "firstName")
    LAST_NAME_FIELD = (By.ID, "lastName")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
    CANCEL_BUTTON = (By.ID, "cancel")
    ADD_USER_TEXT = (By.XPATH, "//h1[text()='Add User']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'span[id="error"]')


    def __init__(self, driver):
        super().__init__(driver)

    def fill_sign_up_form(self, first_name, last_name, email, password):
        self.logger.info(f"Filling sign up form with {first_name} {last_name}")
        try:
            self.do_send_keys(self.FIRST_NAME_FIELD, first_name)
            self.do_send_keys(self.LAST_NAME_FIELD, last_name)
            self.do_send_keys(self.EMAIL_FIELD, email)
            self.do_send_keys(self.PASSWORD_FIELD, password)
            self.do_click(self.SUBMIT_BUTTON)
            self.logger.info(f"Successfully filled sign up form with {first_name} {last_name}")

        except Exception as e:
            self.logger.error(f"Error while filling sign up form with {first_name} {last_name}")
            self.logger.error(e)

    def click_cancel(self):
        self.logger.info(f"Cancelling sign up form")
        self.do_click(self.CANCEL_BUTTON)

    def is_visible_signup_page(self):
        return self.is_visible(self.ADD_USER_TEXT)

    def get_error_message(self):
        if self.is_visible(self.ERROR_MESSAGE, timeout=5):
            return self.get_element_text(self.ERROR_MESSAGE)
        return "No error message found"

