from time import sleep

import allure
import pytest

from config.environment import Environment
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.contact_details_page import ContactDetailsPage
from pages.contact_list_page import ContactListPage

@allure.feature("Contact Management")
@allure.story("Delete contact")
class TestDeleteContact(BaseTest):

    @allure.title("Successful deletion of contact")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.xfail(reason = "only if contact not present")

    def test_delete_contact(self):

        login_page = LoginPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        contact_details_page_ = ContactDetailsPage(self.driver)
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

        with allure.step(f"Clicking on the Name_Link which has to be deleted"):
            contact_list_page_.click_contact_link("Akshay")
            assert contact_details_page_.is_visible_contact_details(), "contact details page did not load properly"

        with allure.step("Deleting the contact"):
            contact_details_page_.click_delete_contact()
            assert contact_list_page_.is_visible_contact_list(), "contact list page did not load properly"

        with allure.step("Logging out of the application"):
            contact_list_page_.click_logout_button()
            assert login_page.login_page_visible(), "Login page did not load properly"

    @allure.title("Unsuccessful deletion of contact")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.xfail
    def test_unsuccessful_delete_contact(self):

        login_page = LoginPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        contact_details_page_ = ContactDetailsPage(self.driver)
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

        with allure.step("Clicking on the Name_Link which has to be deleted"):
            contact_list_page_.click_contact_link("Akshay")
            assert contact_details_page_.is_visible_contact_details(), "contact details page did not load properly"

        with allure.step("Deleting the contact"):
            # Making Test script fail here..............
            assert contact_list_page_.is_visible_contact_list(), "contact list page did not load properly"

        # with allure.step("Logging out of the application"):
        #     contact_list_page_.click_logout_button()
        #     assert login_page.login_page_visible(), "Login page did not load properly"



    @allure.title("Unsuccessful deletion of contact")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.xfail
    def test_delete_not_exist_contact(self):

        login_page = LoginPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        contact_details_page_ = ContactDetailsPage(self.driver)
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

        with allure.step("Clicking on the Name_Link which has to be deleted"):
            contact_list_page_.click_contact_link("XYZ") # This contact does not exist
            assert contact_details_page_.is_visible_contact_details(), "contact details page did not load properly"

        # with allure.step("Deleting the contact"):
        #     contact_details_page_.click_delete_contact()
        #     assert contact_list_page_.is_visible_contact_list(), "contact list page did not load properly"
        #
        # with allure.step("Logging out of the application"):
        #     contact_list_page_.click_logout_button()
        #     assert login_page.login_page_visible(), "Login page did not load properly"
