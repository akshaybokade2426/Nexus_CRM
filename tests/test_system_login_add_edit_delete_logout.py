from time import sleep

import allure
import pytest

from config.environment import Environment
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.add_contact_page import AddContactPage
from pages.contact_details_page import ContactDetailsPage
from pages.contact_list_page import ContactListPage
from pages.edit_contact_page import EditContactPage

@allure.epic("end-to-end")
@allure.feature("System")
@allure.story("login-logout")
class TestSystemLoginAddEditDeleteLogout(BaseTest):

    @allure.title("System scenario for login to logout")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.login
    def test_login_logout(self):
        login_page = LoginPage(self.driver)
        add_contact_page_ = AddContactPage(self.driver)
        contact_details_page_ = ContactDetailsPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        edit_contact_page_ = EditContactPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()
        email = env.get_email()
        password = env.get_password()

        with allure.step("Navigate to login page"):
            login_page.navigate_to(base_url)
            assert login_page.login_page_visible(), "Login page did not load properly"

        with allure.step("Login to the application"):
            login_page.login(email, password)
            assert contact_list_page_.is_visible_contact_list(), "contact list page did not load properly"

        with allure.step("Clicking on add new contact button"):
            contact_list_page_.click_add_new_contact()
            assert add_contact_page_.is_visible_add_contact(), "add new contact page did not load properly"

        with allure.step("filling the add contact form"):
            add_contact_page_.fill_contact_form("Mansi", "Maheshwari", "1997-02-21",
                                                "mansimah@gmail.com", "1234512345", "Ajni",
                                                "Nagpur", "Nagpur", "Maharashtra", "440012", "India")
            assert contact_list_page_.is_visible_contact_list(), "contact list page did not load properly"

        with allure.step("Clicking on the Firstname of contact created"):
            contact_list_page_.click_contact_link("Mansi")
            assert contact_details_page_.is_visible_contact_details(), "contact details page did not load properly"

        with allure.step("Verifying the contact created"):
            contact_details_page_.is_visible_firstname()

        with allure.step("Navigating to the edit contact page and editing the details"):
            contact_details_page_.click_edit_contact()
            assert edit_contact_page_.is_visible_edit_contact(), "edit contact page did not load properly"
            edit_contact_page_.edit_email("newemail@gmai.com")
            edit_contact_page_.click_submit_button()
            assert contact_details_page_.is_visible_contact_details(), "contact details page did not load properly"

        with allure.step("Deleting the created contact"):
            contact_details_page_.click_delete_contact()
            assert contact_list_page_.is_visible_contact_list(), "contact list page did not load properly"

        with allure.step("Logging out of the session"):
            contact_list_page_.click_logout_button()
            assert login_page.login_page_visible()


