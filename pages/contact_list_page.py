from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactListPage(BasePage):
    ADD_NEW_CONTACT_BUTTON = (By.ID, "add-contact")
    CONTACT_LINK = (By.CSS_SELECTOR, 'table[id="myTable"]>tr>td:nth-child(2)')
    LOGOUT_BUTTON = (By.ID, "logout")
    CONTACT_LIST_TEXT = (By.XPATH, "//h1[text()='Contact List']")


    def __init__(self, driver):
        super().__init__(driver)

    def click_add_new_contact(self):
        try:
            self.logger.info(f"Attempting to click add new contact button")
            self.do_click(self.ADD_NEW_CONTACT_BUTTON)
            self.logger.info(f"Successfully clicked on add new contact button")
        except Exception as e:
            self.logger.error(f"Failed to click on add new contact button: {e}")

    def click_contact_link(self, first_name):
        try:
            self.logger.info(f"Attempting to click on contact link: {first_name}")
            dynamic_contact = (By.XPATH, f"//tr[contains(.,'{first_name}')]")
            self.do_click(dynamic_contact)
            self.logger.info(f"Successfully clicked on contact link: {first_name}")
        except Exception as e:
            self.logger.error(f"Failed to click on contact link: {e}")


    def click_logout_button(self):
        try:
            self.logger.info(f"Attempting to click on logout button")
            self.do_click(self.LOGOUT_BUTTON)
            self.logger.info(f"Successfully clicked on logout button")
        except Exception as e:
            self.logger.error(f"Failed to click on logout button: {e}")

    def is_visible_contact_list(self):
        return self.is_visible(self.CONTACT_LIST_TEXT, timeout=5)