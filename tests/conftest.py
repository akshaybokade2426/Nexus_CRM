import allure
import pytest
import logging
import colorlog
from datetime import datetime
from selenium.common.exceptions import WebDriverException, InvalidSessionIdException
import urllib3

@pytest.fixture(scope="function", autouse=True)
def session_logger(request):
    """Sets up a worker-specific logger to prevent I/O errors during parallel runs."""
    # Get worker ID (gw0, gw1, etc.) or 'master' if not using xdist
    worker_id = getattr(request.config, "workerinput", {}).get("workerid", "master")

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M")
    project_root = request.config.rootpath
    log_dir = project_root / 'logs' / f"run_{timestamp}"
    log_dir.mkdir(parents=True, exist_ok=True)

    # Each worker gets its own log file to avoid I/O collisions
    log_file_path = log_dir / f"log_{worker_id}.log"

    logger = logging.getLogger("MyFrameworkLogger")
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    log_format = f'[%(asctime)s] [{worker_id}] - %(filename)s:[%(lineno)d] - [%(levelname)s] - %(message)s'

    # File Handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(file_handler)

    # Console Handler (Only show INFO and above to keep console clean)
    console_handler = colorlog.StreamHandler()
    console_formatter = colorlog.ColoredFormatter('%(log_color)s' + log_format)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    logger.info(f"--- Worker {worker_id} started ---")
    yield logger
    try:
        logger.info(f"--- Worker {worker_id} finished ---")
    except ValueError:
        pass  # File already closed by another worker, ignore.


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)

        # Only proceed if we have a driver and a session ID
        if driver and getattr(driver, "session_id", None):
            try:
                # Binary capture for Allure
                screenshot_bin = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot_bin,
                    name="Failure_Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except (WebDriverException, InvalidSessionIdException,
                    urllib3.exceptions.MaxRetryError, ConnectionRefusedError) as e:
                # Log the specific reason we skipped the screenshot
                logging.getLogger("MyFrameworkLogger").warning(
                    f"Screenshot skipped: Browser session was closed ({type(e).__name__})"
                )

    setattr(item, "rep_" + report.when, report)