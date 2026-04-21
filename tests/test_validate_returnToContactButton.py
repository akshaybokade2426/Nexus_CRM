import allure
import pytest

from config.environment import Environment
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.contact_details_page import ContactDetailsPage
from pages.contact_list_page import ContactListPage

@allure.feature("Contact")
@allure.story("Return to contact")
class TestValidateReturnToContactButton(BaseTest):

    @allure.title("Successful return to contact list page")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_return_to_contact_button(self):

        login_page = LoginPage(self.driver)
        contact_details_page_ = ContactDetailsPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        env = Environment()
        email = env.get_email()
        password = env.get_password()
        base_url = env.get_base_url()

        with allure.step("Navigating to login page"):
            login_page.navigate_to(base_url)
            assert login_page.login_page_visible(), "Login page did not load properly"

        with allure.step("Logging to the application"):
            login_page.login(email, password)
            assert contact_list_page_.is_visible_contact_list(), "Login page did not load properly"

        with allure.step("Clicking on the contact first name link "):
            contact_list_page_.click_contact_link("Atul")
            assert contact_details_page_.is_visible_contact_details(), "Contact details page did not load properly"

        with allure.step("Clicking on the return to contact button"):
            contact_details_page_.click_return()
            assert contact_list_page_.is_visible_contact_list(), "Return to contact list page did not load properly"

        with allure.step("logging out of the application"):
            contact_list_page_.click_logout_button()
            assert login_page.login_page_visible(), "Login page did not load properly"