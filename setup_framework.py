"""
Setup script to initialize the test automation framework.
"""

import os
from pathlib import Path
from utils.excel_provider import ExcelDataProvider


def setup_framework():
    """Initialize the framework with required directories and sample data."""
    print("Setting up Test Automation Framework...")
    
    # Create all required directories
    directories = [
        "config",
        "pages", 
        "tests",
        "utils",
        "test_data",
        "reports/allure-results",
        "reports/allure-report",
        "reports/logs",
        "reports/screenshots"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {directory}")
    
    # Create __init__.py files
    init_files = [
        "config/__init__.py",
        "pages/__init__.py", 
        "tests/__init__.py",
        "utils/__init__.py"
    ]
    
    for init_file in init_files:
        Path(init_file).touch()
        print(f"✓ Created {init_file}")
    
    # Create sample Excel data
    # try:
    #     ExcelReader.create_sample_login_data()
    #     print("✓ Created sample login data Excel file")
    # except Exception as e:
    #     print(f"⚠ Warning: Could not create sample Excel data: {e}")

    print("\n✅ Framework setup completed!")
    print("\nNext steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Update config/config.yaml with your application URLs")
    print("3. Update page locators in pages/login_page.py")
    print("4. Run tests: pytest tests/ -v")


if __name__ == "__main__":
    setup_framework()
