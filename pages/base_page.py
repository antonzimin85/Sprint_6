from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    TIMEOUT = 5

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))

    def click_on_element(self, locator, timeout=TIMEOUT):
        self.find_element(locator, timeout).click()

    def enter_text(self, locator, text, timeout=TIMEOUT):
        self.find_element(locator, timeout).send_keys(text)

    def return_element_text(self, locator, timeout=TIMEOUT):
        return self.find_element(locator, timeout).text

    def return_current_url(self):
        return self.driver.current_url

    def return_current_tab(self):
        return self.driver.current_window_handle

    def return_all_tabs(self):
        return self.driver.window_handles

    def switch_to_new_tab(self, new_tab):
        self.driver.switch_to.window(new_tab)

    def close_current_tab(self):
        self.driver.close()

    def wait_until_visible(self, element_locator, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(element_locator))

    def is_element_present(self, locator, timeout=TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False