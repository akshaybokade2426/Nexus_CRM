from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactDetailsPage(BasePage):

    EDIT_CONTACT_BUTTON = (By.ID, "edit-contact")
    DELETE_CONTACT_BUTTON = (By.ID, "delete")
    RETURN_TO_CONTACT_BUTTON = (By.ID, "return")
    LOGOUT_BUTTON = (By.ID, "logout")
    FIRST_NAME_TEXT = (By.ID, "firstName")
    CONTACT_DETAILS_TEXT = (By.XPATH, "//h1[text()='Contact Details']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_edit_contact(self):
        try:
            self.logger.info(f"Attempting to click on edit contact button")
            self.do_click(self.EDIT_CONTACT_BUTTON)
            self.logger.info(f"Successfully clicked on edit contact button")
        except Exception as e:
            self.logger.error(f"Failed to click on edit contact button: {e}")

    def click_delete_contact(self):
        try:
            self.logger.info(f"Attempting to click on delete contact button")
            self.do_click(self.DELETE_CONTACT_BUTTON)
            self.logger.info(f"Successfully clicked on delete contact button")
            self.logger.info(f"Attempting to handle the pop-up")
            self.switch_to_alert_accept()
            self.logger.info(f"Successfully handled the pop-up")
        except Exception as e:
            self.logger.error(f"Failed to click on delete contact button: {e}")

    def click_return(self):
        try:
            self.logger.info(f"Attempting to click on return button")
            self.do_click(self.RETURN_TO_CONTACT_BUTTON)
            self.logger.info(f"Successfully clicked on return button")
        except Exception as e:
            self.logger.error(f"Failed to click on return button: {e}")

    def click_logout(self):
        try:
            self.logger.info(f"Attempting to click on logout button")
            self.do_click(self.LOGOUT_BUTTON)
            self.logger.info(f"Successfully clicked on logout button")
        except Exception as e:
            self.logger.error(f"Failed to click on logout button: {e}")

    def is_visible_firstname(self):
        return self.is_visible(self.FIRST_NAME_TEXT)

    def is_visible_contact_details(self):
        return self.is_visible(self.CONTACT_DETAILS_TEXT)
