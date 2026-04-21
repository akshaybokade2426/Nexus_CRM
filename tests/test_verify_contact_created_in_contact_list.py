from time import sleep

import allure
import pytest

from config.environment import Environment
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.add_contact_page import AddContactPage
from pages.contact_details_page import ContactDetailsPage
from pages.contact_list_page import ContactListPage
from utils.data_providers import get_filtered_test_data


@allure.feature("Contact")
@allure.story("Contact Creation")
class TestVerifyContact(BaseTest):
    WORKBOOK = "TestData_NexusCRM.xlsx"
    SHEET = "Add"

    @allure.title("Verifying successful creation of contact")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    @pytest.mark.parametrize("data_row", get_filtered_test_data(WORKBOOK, SHEET, "First_name", "Akshay"))
    def test_successful_verify_contact(self, data_row):

        login_page = LoginPage(self.driver)
        add_contact_page_ = AddContactPage(self.driver)
        contact_details_page_ = ContactDetailsPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)

        env = Environment()
        base_url = env.get_base_url()
        email = env.get_email()
        password = env.get_password()


        first_name = data_row.get("First_name")
        last_name = data_row.get("Last_name")
        dob = data_row.get("DOB")
        email_add = data_row.get("Email")
        phone = data_row.get("Phone")
        add1 = data_row.get("Address1")
        add2 = data_row.get("Address2")
        city = data_row.get("City")
        state = data_row.get("State")
        postal = data_row.get("Postal_code")
        country = data_row.get("Country")


        with allure.step("Navigating to the login page"):
            login_page.navigate_to(base_url)
            assert login_page.login_page_visible(), "Login page did not load"

        with allure.step("Logging in to the application"):
            login_page.login(email, password)
            assert contact_list_page_.is_visible_contact_list(), "Contact list page did not load"

        with allure.step("Navigating to the add contact page"):
            contact_list_page_.click_add_new_contact()
            assert add_contact_page_.is_visible_add_contact(), "Add new contact page did not load"

        with allure.step("Fill the contact details"):
            add_contact_page_.fill_contact_form(first_name,last_name,dob,email_add,phone,add1,add2,city,state,postal,country)
            assert contact_list_page_.is_visible_contact_list(), "Contact list page did not load"

        with allure.step("Verifying the contact created by clicking"):
            contact_list_page_.click_contact_link(first_name)
            assert contact_details_page_.is_visible_contact_details(), "Contact details page did not load"

        with allure.step("Verifying the contact created by checking the first name"):
            contact_details_page_.is_visible_firstname()


        with allure.step("Logging out of the application"):
            contact_details_page_.click_logout()
            assert login_page.login_page_visible(), "Login page did not load"
