from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By. ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
    SIGN_UP_BUTTON = (By.ID, "signup")
    HEADER_TEXT = (By.XPATH, "//h1[text()='Contact List App']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'span[id="error"]')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        self.logger.info(f"Attempting to log in with Email: {email}")
        self.do_send_keys(self.EMAIL_FIELD, email)
        self.do_send_keys(self.PASSWORD_FIELD, password)
        self.do_click(self.SUBMIT_BUTTON)

    def click_signup(self):
        self.logger.info(f"Attempting to sign up!!")
        self.do_click(self.SIGN_UP_BUTTON)

    def login_page_visible(self):
        return self.is_visible(self.HEADER_TEXT, timeout=5)

    def get_error_message(self):
        if self.is_visible(self.ERROR_MESSAGE, timeout=5):
            return self.get_element_text(self.ERROR_MESSAGE)
        return "No error message found."