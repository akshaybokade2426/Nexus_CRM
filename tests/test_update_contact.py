import allure
import pytest
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.contact_details_page import ContactDetailsPage
from pages.contact_list_page import ContactListPage
from pages.edit_contact_page import EditContactPage
from config.environment import Environment

@allure.feature("Contact")
@allure.story("Contact Update")
class TestUpdateContact(BaseTest):

    @allure.title("Successful update of contact")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_update_contact(self):

        login_page = LoginPage(self.driver)
        contact_details_page_ = ContactDetailsPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        edit_contact_page_ = EditContactPage(self.driver)
        env = Environment()
        email = env.get_email()
        password = env.get_password()
        base_url = env.get_base_url()

        with allure.step("Navigate to login page"):
            login_page.navigate_to(base_url)
            assert login_page.login_page_visible(), "Login page did not load properly"

        with allure.step("Login to the application"):
            login_page.login(email, password)
            assert contact_list_page_.is_visible_contact_list(), "contact list page did not load properly"

        with allure.step("Clicking on the contact name link"):
            contact_list_page_.click_contact_link("Atul")
            assert contact_details_page_.is_visible_contact_details(), "contact details page did not load properly"

        with allure.step("Navigating to the edit contact page"):
            contact_details_page_.click_edit_contact()
            assert edit_contact_page_.is_visible_edit_contact(), "edit contact page did not load properly"

        with allure.step("Editing the details of the contact"):
            edit_contact_page_.edit_phone("9876543210")
            edit_contact_page_.click_submit_button()
            assert contact_details_page_.is_visible_contact_details(), "edit contact page did not load properly"

        with allure.step("Logging out of the application from edit page"):
            contact_details_page_.click_logout()
            assert login_page.login_page_visible(), "Login page did not load properly"
