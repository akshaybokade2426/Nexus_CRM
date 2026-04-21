import pytest
import allure

from config.environment import Environment
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from pages.contact_list_page import ContactListPage
from pages.add_contact_page import AddContactPage

@allure.feature("Contact Management")
@allure.story("Add Contact")
class TestAddContact(BaseTest):


    @allure.title("Test successful add a new contact")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_successful_add_contact(self):

        login_page = LoginPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        add_contact_page = AddContactPage(self.driver)
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

        with allure.step("Clicking add new contact button"):
            contact_list_page_.click_add_new_contact()
            assert add_contact_page.is_visible_add_contact(), "Add contact page is not loaded properly"

        with allure.step("Entering data in the add contact page"):
            add_contact_page.fill_contact_form("Appu", "yadav", "1998-10-25", "apurvayadav@gmail.com", "1234567890", "Mahad", "Raigad", "Raigad", "Maharashtra", "480120", "India")
            assert contact_list_page_.is_visible_contact_list(), "contact list page did not load properly"


    @allure.title("Test Unsuccessful add a new contact")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail
    @pytest.mark.regression
    def test_failed_add_contact(self):
        login_page = LoginPage(self.driver)
        contact_list_page_ = ContactListPage(self.driver)
        add_contact_page = AddContactPage(self.driver)
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

        with allure.step("Clicking add new contact button"):
            # Making test script fail here because not clicking on the button
            assert add_contact_page.is_visible_add_contact(), "Add contact page is not loaded properly"

        # with allure.step("Entering data in the add contact page"):
        #     add_contact_page.fill_contact_form("Appu", "yadav", "1998-10-25", "apurvayadav@gmail.com", "1234567890",
        #                                        "Mahad", "Raigad", "Raigad", "Maharashtra", "480120", "India")
        #     assert contact_list_page_.is_visible_contact_list(), "contact list page did not load properly"
