import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager


def get_firefox_driver():
    cache_path = os.path.expanduser("~/.wdm/drivers/geckodriver")
    for root, dirs, files in os.walk(cache_path):
        for f in files:
            if f == "geckodriver":
                return webdriver.Firefox(service=FirefoxService(os.path.join(root, f)))
    raise FileNotFoundError("geckodriver not found in cache")


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif request.param == "firefox":
        driver = get_firefox_driver()
    driver.maximize_window()
    yield driver
    driver.quit()
