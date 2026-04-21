import time

import allure
import pytest
from openpyxl.xml.constants import WORKBOOK

from config.environment import Environment
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.contact_list_page import ContactListPage
from utils.data_providers import get_all_test_data


@allure.feature("Authentication")
@allure.story("Logging in")
class TestLogin(BaseTest):
    WORKBOOK = "TestData_NexusCRM.xlsx"
    SHEET = "SIGN_UP"

    @allure.title("Log in to the application!")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.parametrize("data_row", get_all_test_data(WORKBOOK, SHEET))
    def test_successful_log_in(self, data_row):

        login_page = LoginPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()
        email = data_row.get("Email")
        password = data_row.get("Password")

        with allure.step("Navigate to login page"):
            login_page.navigate_to(base_url)
            assert login_page.login_page_visible(), "Login page did not load properly"

        with allure.step("Login to the application"):
            login_page.login(email, password)
            assert contact_list_page_.is_visible_contact_list(), "contact list page did not load properly"

    @allure.title("Logging in with incorrect email")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @allure.issue("BUG-123", "Login error message validation")
    @pytest.mark.xfail(reason="Intentionally failing to verify error message handling")
    def test_unsuccessful_log_in_email(self):

        login_page = LoginPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()
        password = env.get_password()

        with allure.step("Navigate to login page"):
            login_page.navigate_to(base_url)
            assert login_page.login_page_visible(), "Login page did not load properly"

        with allure.step("Login to the application"):
            login_page.login("Incorrect_mail", password) #making test script fail here by passing wrong email
            assert login_page.get_error_message(), "The error message is not present"


    @allure.title("Logging in with incorrect password")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    @allure.issue("BUG-123", "Login error message validation")
    @pytest.mark.xfail(reason="Intentionally failing to verify error message handling")
    def test_unsuccessful_log_in_pass(self):
        login_page = LoginPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        env = Environment()
        base_url = env.get_base_url()
        email = env.get_email()

        with allure.step("Navigate to login page"):
            login_page.navigate_to(base_url)
            assert login_page.login_page_visible(), "Login page did not load properly"

        with allure.step("Login to the application"):
            login_page.login(email, "Incorrect_password")  #making test script fail here by passing wrong password
            assert login_page.get_error_message(), "The error message is not present"
