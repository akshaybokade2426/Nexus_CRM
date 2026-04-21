## 🤝 Contributing

We welcome contributions to improve this framework! To ensure consistency and maintain high quality, please read our **[Contributing Guide](CODING_STANDARDS.md)** before you get started.

The guide covers our coding standards, branch naming conventions, and the pull request process.
Here's the complete coding conventions section in one shot for copy-paste:

```markdown
## 📋 Coding Conventions & Standards

### 🐍 **Python Naming Conventions (PEP 8)**

#### Variables and Functions
```python
# ✅ Good - snake_case for variables and functions
user_name = "john_doe"
page_title = "Login Page"
test_data_file = "TestData_AppName.xlsx"

def get_user_credentials():
    pass

def navigate_to_login_page():
    pass

# ❌ Bad - avoid camelCase for variables/functions in Python
userName = "john_doe"  # Don't use
pageTitle = "Login Page"  # Don't use
```

#### Classes
```python
# ✅ Good - PascalCase for class names
class LoginPage:
    pass

class ExcelDataProvider:
    pass

class BaseTest:
    pass

# ❌ Bad - avoid snake_case for classes
class login_page:  # Don't use
    pass
```

#### Constants
```python
# ✅ Good - UPPER_CASE for constants
DEFAULT_TIMEOUT = 10
BASE_URL = "https://example.com"
EXCEL_FILE_PATH = "./data/TestData.xlsx"
MAX_RETRY_COUNT = 3

# ❌ Bad - avoid lowercase for constants
default_timeout = 10  # Don't use
```

#### Private Methods and Variables
```python
class LoginPage:
    def __init__(self):
        self._driver = None  # ✅ Single underscore for internal use
        self.__private_data = None  # ✅ Double underscore for private
    
    def _internal_helper_method(self):  # ✅ Internal method
        pass
    
    def public_method(self):  # ✅ Public method
        pass
```

### 🌐 **Selenium Naming Conventions**

#### Locator Constants
```python
# ✅ Good - Descriptive, UPPER_CASE locator names
class LoginPage:
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE_TEXT = (By.CLASS_NAME, "error-message")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot Password?")
    
    # Group related locators
    NAVIGATION_MENU = (By.CSS_SELECTOR, ".nav-menu")
    NAVIGATION_HOME_LINK = (By.CSS_SELECTOR, ".nav-menu .home-link")
    NAVIGATION_PROFILE_LINK = (By.CSS_SELECTOR, ".nav-menu .profile-link")

# ❌ Bad - unclear or inconsistent naming
class LoginPage:
    user = (By.ID, "username")  # Too short
    pwd_field = (By.ID, "password")  # Inconsistent abbreviation
    btn1 = (By.XPATH, "//button")  # Not descriptive
```

#### Page Object Method Names
```python
# ✅ Good - Action-based method names
class LoginPage(BasePage):
    def enter_username(self, username):
        """Enter username in the username field."""
        pass
    
    def enter_password(self, password):
        """Enter password in the password field."""
        pass
    
    def click_login_button(self):
        """Click the login button."""
        pass
    
    def get_error_message_text(self):
        """Get the error message text."""
        pass
    
    def is_login_successful(self):
        """Check if login was successful."""
        pass
    
    def wait_for_page_to_load(self):
        """Wait for the login page to fully load."""
        pass

# ❌ Bad - unclear or non-action based names
class LoginPage:
    def username(self, text):  # Not clear it's an action
        pass
    
    def login_btn(self):  # Abbreviated and unclear
        pass
    
    def check_login(self):  # Ambiguous - checking what?
        pass
```

### 🧪 **Test Naming Conventions**

#### Test Class Names
```python
# ✅ Good - Descriptive test class names
class TestLoginFunctionality:
    pass

class TestUserRegistration:
    pass

class TestShoppingCart:
    pass

class TestDataDrivenLogin:
    pass

# ❌ Bad - unclear test class names
class LoginTests:  # Less descriptive
    pass

class Test1:  # Not descriptive at all
    pass
```

#### Test Method Names
```python
# ✅ Good - Descriptive test method names that explain the scenario
def test_successful_login_with_valid_credentials():
    """Test successful login using valid username and password."""
    pass

def test_login_failure_with_invalid_password():
    """Test login failure when invalid password is provided."""
    pass

def test_login_failure_with_empty_username_field():
    """Test login failure when username field is left empty."""
    pass

def test_password_field_masks_input_characters():
    """Test that password field masks input characters for security."""
    pass

# ❌ Bad - unclear or non-descriptive names
def test_login():  # Too generic
    pass

def test_login_1():  # Numbers don't explain scenario
    pass

def test_bad_login():  # "bad" is too vague
    pass
```

### 📁 **File and Directory Naming**

#### File Names
```python
# ✅ Good - descriptive, snake_case file names
login_page.py
user_registration_page.py
shopping_cart_page.py
base_test.py
excel_data_provider.py
test_login_functionality.py
test_user_registration.py

# ❌ Bad - unclear or inconsistent naming
loginPage.py  # camelCase not recommended for files
login.py  # Too generic
test1.py  # Not descriptive
```

#### Directory Structure
```
# ✅ Good - clear, organized directory names
pages/
tests/
utils/
config/
data/
reports/
logs/

# ❌ Bad - unclear directory names
src/
lib/
misc/
temp/
```

### 🎯 **Selenium Best Practices**

#### Locator Strategy Priority
```python
# ✅ Preferred locator strategies (in order of preference)
# 1. ID - Most reliable and fast
USERNAME_FIELD = (By.ID, "username")

# 2. Name - Good for form elements
EMAIL_FIELD = (By.NAME, "email")

# 3. CSS Selector - Flexible and readable
SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
PRODUCT_PRICE = (By.CSS_SELECTOR, ".product .price")

# 4. XPath - Use sparingly, prefer relative XPath
DYNAMIC_ELEMENT = (By.XPATH, "//div[@data-testid='user-profile']")
RELATIVE_XPATH = (By.XPATH, ".//span[contains(text(), 'Add to Cart')]")

# ❌ Avoid these locator strategies
LINK_TEXT = (By.LINK_TEXT, "Click Here")  # Text can change
PARTIAL_LINK_TEXT = (By.PARTIAL_LINK_TEXT, "Click")  # Too generic
TAG_NAME = (By.TAG_NAME, "button")  # Too generic
CLASS_NAME = (By.CLASS_NAME, "btn")  # Often not unique
```

#### Wait Strategy Best Practices
```python
# ✅ Good - Explicit waits with meaningful conditions
def wait_for_element_to_be_clickable(self, locator, timeout=10):
    """Wait for element to be present and clickable."""
    return WebDriverWait(self.driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

def wait_for_text_to_be_present(self, locator, text, timeout=10):
    """Wait for specific text to be present in element."""
    return WebDriverWait(self.driver, timeout).until(
        EC.text_to_be_present_in_element(locator, text)
    )

# ❌ Bad - Hard-coded sleep statements
import time
time.sleep(5)  # Avoid this - unreliable and slow
```

### 🏗️ **Code Organization Best Practices**

#### Method Ordering in Classes
```python
class LoginPage(BasePage):
    """Login page object following standard organization."""
    
    # 1. Class constants/locators first
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    
    # 2. Constructor
    def __init__(self, driver):
        super().__init__(driver)
    
    # 3. Public methods (alphabetically ordered)
    def click_login_button(self):
        """Click the login button."""
        pass
    
    def enter_password(self, password):
        """Enter password."""
        pass
    
    def enter_username(self, username):
        """Enter username."""
        pass
    
    def is_login_successful(self):
        """Check if login was successful."""
        pass
    
    # 4. Private methods last
    def _validate_page_loaded(self):
        """Private method to validate page is loaded."""
        pass
```

#### Import Organization
```python
# ✅ Good - Organized imports following PEP 8
# 1. Standard library imports
import os
import time
from datetime import datetime
from pathlib import Path

# 2. Third-party imports
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 3. Local application imports
from pages.base_page import BasePage
from utils.excel_provider import ExcelDataProvider
from config.environment import Environment

# ❌ Bad - Unorganized imports
from selenium import webdriver
import os
from pages.base_page import BasePage
import pytest
from pathlib import Path
import allure
```

### 📝 **Documentation Standards**

#### Docstring Conventions
```python
# ✅ Good - Clear, descriptive docstrings
class LoginPage(BasePage):
    """
    Page Object Model for the login page.
    
    This class contains all locators and methods related to the login
    functionality of the application.
    """
    
    def login(self, username: str, password: str) -> bool:
        """
        Perform login with provided credentials.
        
        Args:
            username (str): The username to enter
            password (str): The password to enter
            
        Returns:
            bool: True if login appears successful, False otherwise
            
        Raises:
            TimeoutException: If elements are not found within timeout
        """
        pass

# ❌ Bad - Missing or unclear docstrings
def login(self, username, password):
    # logs in
    pass
```

#### Comment Standards
```python
# ✅ Good - Meaningful comments explaining WHY, not WHAT
def wait_for_ajax_to_complete(self, timeout=30):
    """Wait for all AJAX requests to complete."""
    # Wait longer for AJAX as some API calls can take 20+ seconds
    # due to complex backend processing
    WebDriverWait(self.driver, timeout).until(
        lambda driver: driver.execute_script("return jQuery.active === 0")
    )

# ❌ Bad - Comments that just repeat the code
def click_login_button(self):
    # Click the login button
    self.click(self.LOGIN_BUTTON)  # Clicks the button
```

### ✅ **General Python Best Practices**

#### Error Handling
```python
# ✅ Good - Specific exception handling
def read_excel_file(self, file_path: str) -> List[Dict]:
    """Read data from Excel file with proper error handling."""
    try:
        workbook = load_workbook(file_path)
        return self._process_workbook(workbook)
    except FileNotFoundError:
        self.logger.error(f"Excel file not found: {file_path}")
        raise
    except PermissionError:
        self.logger.error(f"Permission denied accessing: {file_path}")
        raise
    except Exception as e:
        self.logger.error(f"Unexpected error reading Excel: {e}")
        raise

# ❌ Bad - Generic exception handling
def read_excel_file(self, file_path):
    try:
        # ... code ...
        pass
    except Exception:
        pass  # Silently ignoring errors
```

#### Type Hints
```python
# ✅ Good - Use type hints for better code clarity
from typing import List, Dict, Optional, Union

def get_test_data(self, file_path: str, sheet_name: str) -> List[Dict[str, str]]:
    """Get test data with proper type hints."""
    pass

def find_element_with_retry(self, locator: tuple, max_retries: int = 3) -> Optional[WebElement]:
    """Find element with retry logic."""
    pass

# ❌ Bad - No type hints
def get_test_data(self, file_path, sheet_name):
    pass
```

### 🏷️ **Test Markers and Organization**

#### Pytest Markers
```python
# ✅ Good - Meaningful marker usage
@pytest.mark.smoke  # Critical tests that must pass
@pytest.mark.regression  # Full regression suite
@pytest.mark.critical  # High priority tests
@pytest.mark.slow  # Tests that take longer to execute
@pytest.mark.integration  # Integration tests
@pytest.mark.unit  # Unit tests

# Combining markers
@pytest.mark.smoke
@pytest.mark.critical
def test_user_can_login_with_valid_credentials():
    pass

# Parametrized markers
@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
@pytest.mark.cross_browser
def test_login_across_browsers(browser):
    pass
```

#### Test Data Organization
```python
# ✅ Good - Organized test data structure
# In conftest.py or test data files
LOGIN_VALID_DATA = [
    {"username": "admin", "password": "admin123", "expected": "success"},
    {"username": "user1", "password": "pass123", "expected": "success"}
]

LOGIN_INVALID_DATA = [
    {"username": "invalid", "password": "wrong", "expected": "failure"},
    {"username": "", "password": "pass123", "expected": "failure"},
    {"username": "user1", "password": "", "expected": "failure"}
]

# ❌ Bad - Mixed or unclear test data
TEST_DATA = [
    ("admin", "admin123", True),  # Not clear what True means
    ("wrong", "wrong", False),
    ("", "", None)  # Unclear expectation
]
