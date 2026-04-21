import allure
import pytest

from config.environment import Environment
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.sign_up_page import SignUpPage
from pages.contact_list_page import ContactListPage
from utils.data_providers import get_all_test_data
import random
import string




@allure.feature("Authentication")
@allure.story("Sign Up")
class TestSIgnUp(BaseTest):

    WORKBOOK = "TestData_NexusCRM.xlsx"
    SHEET = "SIGN_UP"

    @allure.title("Signing up with new email")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.parametrize("data_row", get_all_test_data(WORKBOOK, SHEET))
    def test_successful_signup(self, data_row):

        login_page_ = LoginPage(self.driver)
        signup_page_ = SignUpPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        env = Environment()
        base_url = self.env.get_base_url()

        unique_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        first_name = data_row.get("First_name")
        last_name = data_row.get("Last_name")

        raw_email = data_row.get("Email", "user@test.com")
        email = raw_email.replace("@", f"_{unique_suffix}@")
        password = data_row.get("Password")

        with allure.step("Navigate to login page"):
            login_page_.navigate_to(base_url)
            assert login_page_.login_page_visible(), "Login page did not load properly"

        with allure.step("Clicking on the sign_up button"):
            login_page_.click_signup()
            assert signup_page_.is_visible_signup_page(), "Signup page did not load properly"

        with allure.step("Filling the sign-up form"):
            signup_page_.fill_sign_up_form(first_name, last_name, email, password)
            assert contact_list_page_.is_visible_contact_list(), "Contact list page did not load properly"


    @allure.title("Signing up using wrong email format")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @pytest.mark.xfail
    def test_unsuccessful_signup(self):

        login_page_ = LoginPage(self.driver)
        signup_page_ = SignUpPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        env = Environment()
        base_url = self.env.get_base_url()

        with allure.step("Navigate to login page"):
            login_page_.navigate_to(base_url)
            assert login_page_.login_page_visible(), "Login page did not load properly"

        with allure.step("Clicking on the sign_up button"):
            login_page_.click_signup()
            assert signup_page_.is_visible_signup_page(), "Signup page did not load properly"

        with allure.step("Filling the sign-up form"):
            signup_page_.fill_sign_up_form("Alpha", "gen-z", "akshaybokade", "Admin@123")
            assert signup_page_.get_error_message(), "error message is not present"
            #Making the script fail because the format of email given is wrong......



