import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def webdriver_instance():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

