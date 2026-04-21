# Professional Python Test Automation Framework

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.15%2B-green.svg)](https://selenium.dev)
[![Pytest](https://img.shields.io/badge/Pytest-7.4%2B-orange.svg)](https://pytest.org)
[![Allure](https://img.shields.io/badge/Allure-2.13%2B-purple.svg)](https://docs.qameta.io/allure/)

A robust and scalable UI test automation framework built with Python. This framework demonstrates a professional-grade architecture incorporating the Page Object Model, data-driven testing, advanced logging, and rich, multi-format reporting.

---

## ✨ Key Features

#### 🏗️ **Architecture & Design Patterns**
-   **Page Object Model (POM):** Clean separation of UI elements (`Pages`) and test logic (`Tests`).
-   **Centralized `BasePage`:** Contains reusable, robust UI actions with smart waiting mechanisms.
-   **`BaseTest` Class:** Manages common test setup and teardown, including browser lifecycle and failure capture.
-   **Modular & Scalable Structure:** Organized into distinct packages for configuration, data, pages, reports, tests, and utilities.

#### 📊 **Data-Driven Testing**
-   **Excel Integration:** Powered by a custom `ExcelDataProvider` for reading and filtering data from `.xlsx` files.
-   **Advanced Data Filtering:** Supports SQL-like filtering for single or multiple `AND` conditions.
-   **Parameterized Tests:** Dynamically generates test cases based on data from Excel.

#### 🌍 **Multi-Environment Support**
-   **Dynamic Environment Management:** Easily switch test execution between different environments (`demo`, `dev`, `staging`) using an environment variable.
-   **YAML Configuration:** All environment details (URLs, credentials) are managed in a clean `config.yaml` file.

#### 📝 **Advanced Logging**
-   **Timestamped Log Directories:** Automatically creates a unique, timestamped folder for each test run.
-   **Rich Log Format:** Logs include timestamp, filename, and line number for precise debugging.
-   **Colored Console Output:** Uses `colorlog` for enhanced readability of log levels in the console.

#### 📈 **Comprehensive Reporting**
-   **Allure Reports:** Generates detailed, interactive HTML reports.
    -   **Automatic Attachments:** Captures and attaches screenshots and test-specific logs on failure.
    -   **Environment Details:** Displays browser, platform, and URL on the report dashboard.
-   **`pytest-html` Reports:** Generates a simple, self-contained `.html` report with screenshots embedded on failure.

#### 🔧 **Automation Features**
-   **Automatic WebDriver Management:** Utilizes Selenium Manager to seamlessly download and manage browser drivers.
-   **Designed for Cross-Browser Support:** Framework is structured to easily extend testing to Firefox, Edge, etc.
-   **Parallel Execution Ready:** Supports concurrent test execution via `pytest-xdist` (tests must be independent).

---

## 🛠️ Tech Stack

| Component               | Technology    | Purpose                              |
|-------------------------|---------------|--------------------------------------|
| **Language** | Python 3.10+  | Core programming language            |
| **Test Runner** | Pytest        | Test execution and framework         |
| **Browser Automation** | Selenium      | Web UI interaction                   |
| **Reporting** | Allure Report | Primary interactive reporting        |
| **Secondary Reporting** | pytest-html   | Self-contained HTML reports          |
| **Data Processing** | openpyxl      | Excel file reading and manipulation  |
| **Logging** | colorlog      | Enhanced console logging             |
| **Configuration** | PyYAML        | Environment configuration management |

---

## 📂 Project Structure

```
Your_Project_Name/
├── 📁 config/                    # Environment configuration management
│   ├── config.yaml               # Multi-environment settings
│   └── environment.py            # Environment configuration handler
│
├── 📁 data/                      # Test data files (place your .xlsx files here)
│   └── TestData_AppName.xlsx
│
├── 📁 docs_images/               # For storing documentation images
│   └── framework_architecture.png
│
├── 📁 logs/                      # Generated log files
│   └── logs_DD_MM_YYYY_HHMMSS/   # Timestamped folders (auto-created)
│
├── 📁 pages/                     # Page Object Model classes
│   ├── base_page.py              # Reusable UI actions and utilities
│   └── login_page.py             # Example login page object
│
├── 📁 reports/                   # Test execution reports
│   ├── allure-results/           # Raw Allure data (auto-generated)
│   ├── screenshots/              # Failure screenshots (auto-captured)
│   └── html_report.html          # pytest-html report
│
├── 📁 tests/                     # Test scripts and framework setup
│   ├── conftest.py               # Pytest fixtures and hooks
│   ├── base_test.py              # Base test class with setup/teardown
│   └── test_*.py                 # Example test files
│
├── 📁 utils/                     # Reusable utility modules
│   ├── excel_provider.py         # Excel data reading and filtering
│   ├── data_providers.py         # Bridge functions for parametrization
│   └── logger.py                 # Logging configuration utility
│
├── 📄 pytest.ini                 # Pytest configuration file
├── 📄 requirements.txt           # Python package dependencies
├── 📄 CODING_STANDARDS.md         # Guidelines for code style and conventions
└── 📄 README.md                   # This project documentation
```

---

## 🏗️ Framework Architecture & Flow

For a visual overview of the framework's components and execution lifecycle, please see our architecture diagrams.

➡️ **[View Framework Architecture & Workflow Diagrams](ARCHITECTURE.md)**

---

## 🚀 Setup and Installation

### Prerequisites

Ensure you have the following installed on your system:

-   **Python 3.10 or higher**
-   **pip** (Python package installer, typically comes with Python)
-   **Allure Commandline Tool**

### Installation Guide

1.  **Clone the Repository**
    ```bash
    git clone <your-repository-url>
    cd Your_Project_Name/
    ```

2.  **Create and Activate a Virtual Environment** *(Highly Recommended)*
    ```bash
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Verify Installation**
    ```bash
    pytest --version
    allure --version
    ```
---

## ▶️ Execution Guide

> **Important:** Always run commands from the **project root directory**. Your `pytest.ini` file automates most of the configuration.

### Running Tests

```bash
# Run all tests using the default environment (dev)
pytest

# Run tests against a specific environment (e.g., staging)
# On Windows PowerShell:
$env:ENV="staging"; pytest

# On macOS/Linux:
ENV=staging pytest

# Run only tests with a specific marker (e.g., smoke)
pytest -m smoke
```

### Generating and Viewing Reports

The framework generates two types of reports automatically:

#### Allure Report *(Primary)*
Allure provides the most detailed, interactive report. The raw data is generated automatically by pytest.

```bash
# Generate and view the report in a browser
allure serve reports/allure-results
```

#### pytest-html Report *(Secondary)*
A simple, self-contained HTML file is also generated automatically. You can find it at `reports/html_report.html`.

---

## 📜 Coding Standards & Best Practices

To ensure consistency, readability, and maintainability across the project, we follow a detailed set of coding standards and best practices.

➡️ **[Read the Full Coding Standards Guide](CODING_STANDARDS.md)**
