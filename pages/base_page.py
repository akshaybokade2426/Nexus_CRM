from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from utils.logger import get_logger

class BasePage:
    import allure

    def __init__(self, driver):
        self.driver = driver
        # Use a consistent wait instance
        self.wait = WebDriverWait(self.driver, 15)
        self.logger = get_logger()

    def is_visible(self, locator, timeout=10):
        """Checks if an element is visible and returns a boolean."""
        try:
            # We wrap this in bool() to ensure it always returns True or False, never None
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return bool(element)
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
            self.logger.warning(f"Element not visible: {locator}")
            return False
        # Catching the specific error you saw earlier
        except AttributeError:
            self.logger.error(f"Internal Selenium error (NoneType) for locator: {locator}")
            return False

    @allure.step("Clicking Element: {locator}")
    def do_click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Clicked: {locator}")
        except TimeoutException:
            self.logger.error(f"Failed to click {locator}: Timeout")
            raise

    @allure.step("Entering text into Element: {locator}")
    def do_send_keys(self, locator, text, clear_first=True):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            if clear_first:
                element.clear()
            element.send_keys(text)
            self.logger.info(f"Entered text into {locator}")
        except TimeoutException:
            self.logger.error(f"Could not enter text into {locator}")
            raise

    @allure.step("Switching to Frame: {locator}")
    def switch_to_frame(self, locator):
        try:
            # This is a much safer way to switch to frames
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
            self.logger.info(f"Switched to frame: {locator}")
        except TimeoutException:
            self.logger.error(f"Could not switch to frame: {locator}")
            raise

    @allure.step("Getting text from element: {locator}")
    def get_element_text(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            text = element.text
            self.logger.info(f"Retrieved text '{text}' from element: {locator}")
            return text
        except TimeoutException:
            self.logger.error(f"Timeout: Could not get text from element as it was not visible: {locator}")
            raise

    @allure.step(f"Getting page title")
    def get_title(self):
        title = self.driver.title
        self.logger.info(f"Current page title: {title}")
        return title

    @allure.step("Navigating to URL: {url}")
    def navigate_to(self, url):
        try:
            self.driver.get(url)
            self.logger.info(f"Successfully navigated to URL: {url}")
        except Exception as e:
            self.logger.error(f"Exception while navigating to URL: {url}")
            raise


#-----------------------------------------------------------------------------------
    def select_by_index(self, locator, index):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_index(index)

    def select_by_value(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_value(value)

    def select_By_VisibleText(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        select = Select(element)
        select.select_by_visible_text(text)

    def hover_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()

    def drag_and_Drop(self, locator1, locator2):
        drag = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator1))
        drop = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator2))
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(drag, drop).perform()

    def contextClick(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        action_chains = ActionChains(self.driver)
        action_chains.context_click(element).perform()

    def doubleClick(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        action_chains = ActionChains(self.driver)
        action_chains.double_click(element).perform()


    def switch_to_alert_accept(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def switch_to_alert_dismiss(self):
        self.driver.switch_to.alert().dismiss()

    def switch_to_alert_sendKeys(self, text):
        self.driver.switch_to.alert().send_keys(text)

    def scroll_To_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)




