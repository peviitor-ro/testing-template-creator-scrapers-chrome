#
#
#
#  Chrome Driver Config
#
#
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
#
from .__config import DEFAULT_USER_AGENT


@pytest.fixture(scope="session")
def driver_config():
    """
    Config for ChromeDriver.
    """
    chrome_options = Options()

    # for chrome options
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # antibot
    chrome_options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument(
        '--disable-blink-features=AutomationControlled'
    )

    # set user_agent
    chrome_options.add_argument(
        DEFAULT_USER_AGENT,
    )

    service = Service(
        '/usr/bin/chromedriver',
    )
    driver = webdriver.Chrome(
        service=service,
        options=chrome_options,
    )

    #  use it everywhere
    yield driver

    driver.close()
