import allure

from locators.main_page_locators import MainPageLocators
from config import BASE_URL
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step(f'Открываем главную страницу: {BASE_URL}')
    def open_page(self):
        self.open_url(BASE_URL)

    @allure.step('Подтверждаем куки')
    def confirm_cookie(self):
        self.click_on_element(MainPageLocators.CONFIRM_COOKIE_BUTTON)

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self, order_button_locator):
        self.click_on_element(order_button_locator)

    @allure.step('Клик по вопросу в секции "Вопросы о важном"')
    def click_question_in_faq_section_to_open_answer(self, question_locator):
        self.click_on_element(question_locator)

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, answer_locator):
        return self.return_element_text(answer_locator)

    @allure.step('Кликаем на вопрос и получаем текст ответа')
    def click_question_and_get_answer_text(self, question_locator, answer_locator):
        self.click_question_in_faq_section_to_open_answer(question_locator)
        return self.get_answer_text(answer_locator)

    @allure.step('Проверяем, что текст ответа соответствует ожидаемому')
    def check_answer_text(self, question_locator, answer_locator, expected_answer):
        actual_answer = self.click_question_and_get_answer_text(question_locator, answer_locator)
        assert actual_answer == expected_answer