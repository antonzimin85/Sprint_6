import allure

from config import DZEN_URL_WITH_REDIRECT, BASE_URL
from locators.track_order_status_page_locators import TrackOrderStatusPageLocators
from pages.base_page import BasePage


class TrackOrderStatusPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клип по логотипу "Яндекс"')
    def click_on_yandex_logo_in_header(self):
        self.click_on_element(TrackOrderStatusPageLocators.YANDEX_LOGO_IN_HEADER)

    @allure.step('Клип по логотипу "Самокат"')
    def click_on_scooter_logo_in_header(self):
        self.click_on_element(TrackOrderStatusPageLocators.SCOOTER_LOGO_IN_HEADER)

    @allure.step('Проверяем, что отрылась страница Дзен через редирект')
    def check_dzen_page_is_opened(self):
        new_tab = self.return_all_tabs()[1]
        self.switch_to_new_tab(new_tab)
        self.wait_until_visible(TrackOrderStatusPageLocators.DZEN_SEARCH_BUTTON, 15)
        new_tab_url = self.return_current_url()
        assert new_tab_url == DZEN_URL_WITH_REDIRECT

    @allure.step('Проверяем, что открылась главная страница при клике на логотип "Самокат"')
    def check_main_page_is_opened(self):
        assert self.return_current_url() == BASE_URL




