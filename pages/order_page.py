import allure

from locators.order_page_locators import OrderPageLocators
from config import ORDER_PAGE_URL
from pages.base_page import BasePage


class OrderPage(BasePage):

    ORDER_CONFIRMATION_TITLE = 'Заказ оформлен'

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step(f'Открываем страницу оформления заказа: {ORDER_PAGE_URL}')
    def open_page(self):
        self.open_url(ORDER_PAGE_URL)

    @allure.step('Вводим имя')
    def enter_first_name(self, first_name):
        self.enter_text(OrderPageLocators.FIRST_NAME_FIELD, first_name)

    @allure.step('Вводим фамилию')
    def enter_second_name(self, second_name):
        self.enter_text(OrderPageLocators.SECOND_NAME_FIELD, second_name)

    @allure.step('Вводим адрес')
    def enter_address(self, address):
        self.enter_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Выбираем станцию метро')
    def choose_metro_station(self, metro_station):
        self.click_on_element(OrderPageLocators.METRO_STATION_FIELD)
        self.enter_text(OrderPageLocators.METRO_STATION_FIELD_HAS_FOCUS, metro_station)
        self.click_on_element(OrderPageLocators.METRO_STATION_VALUE_IN_DROPDOWN)

    @allure.step('Вводим номер телефона')
    def enter_phone_number(self, phone_number):
        self.enter_text(OrderPageLocators.PHONE_NUMBER_FIELD, phone_number)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Вводим дату заказа')
    def enter_order_date(self, order_date):
        self.enter_text(OrderPageLocators.ORDER_DATE_FIELD, order_date)
        self.click_on_element(OrderPageLocators.ORDER_DATE_ON_DATEPICKER)

    @allure.step('Выбираем срок аренды')
    def choose_order_period(self, order_period_index):
        self.click_on_element(OrderPageLocators.ORDER_PERIOD_DROPDOWN)
        order_periods = self.find_elements(OrderPageLocators.ORDER_PERIOD_VALUES)
        order_periods[order_period_index].click()

    @allure.step('Выбираем цвет самоката')
    def choose_scooter_color(self, scooter_color_checkbox_locator):
        self.click_on_element(scooter_color_checkbox_locator)

    @allure.step('Вводим комментарий к заказу')
    def enter_order_comment(self, order_comment):
        self.enter_text(OrderPageLocators.COMMENT_FIELD, order_comment)

    @allure.step('Клик по кнопке "Заказать"')
    def click_submit_order_button(self):
        self.click_on_element(OrderPageLocators.SUBMIT_ORDER_BUTTON)

    @allure.step('Клик по кнопке "Да"')
    def click_yes_button_on_confirm_order_modal_window(self):
        self.click_on_element(OrderPageLocators.YES_BUTTON_ON_CONFIRM_ORDER_MODAL_WINDOW)

    @allure.step('Проверяем, что отображается заголовок страницы с подтверждением заказа')
    def check_order_confirmation_title_is_displayed(self):
        assert self.is_element_present(OrderPageLocators.CONFIRM_ORDER_MODAL_WINDOW_TITLE)

    @allure.step('Получаем текст заголовка страницы с подтверждением заказа')
    def get_text_of_order_confirmation_title(self):
        return self.return_element_text(OrderPageLocators.CONFIRM_ORDER_MODAL_WINDOW_TITLE)

    @allure.step(f'Проверяем, что заголовок страницы с подтверждением заказа содержит ожидаемый заголовок')
    def check_order_confirmation_title_include_expected_text(self):
        assert self.ORDER_CONFIRMATION_TITLE in self.get_text_of_order_confirmation_title()

    @allure.step('Оформляем заказ')
    def place_order(self, first_name, second_name, address, metro_station, phone_number, order_date, order_period_index, scooter_color_checkbox, order_comment):
        self.enter_first_name(first_name)
        self.enter_second_name(second_name)
        self.enter_address(address)
        self.choose_metro_station(metro_station)
        self.enter_phone_number(phone_number)
        self.click_next_button()
        self.enter_order_date(order_date)
        self.choose_order_period(order_period_index)
        self.choose_scooter_color(scooter_color_checkbox)
        self.enter_order_comment(order_comment)
        self.click_submit_order_button()
        self.click_yes_button_on_confirm_order_modal_window()

    @allure.step('Клип по кнопке "Посмотреть статус"')
    def click_on_watch_order_status_button(self):
        self.click_on_element(OrderPageLocators.WATCH_ORDER_STATUS_BUTTON)