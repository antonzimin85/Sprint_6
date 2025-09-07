import allure
import pytest

from config import BASE_URL
from data.data_for_faq_section import DataForFaqSection
from pages.main_page import MainPage


class TestFaqSection:

    @allure.title('Проверка FAQ секции')
    @allure.description('Проверка текста ответов на вопросы в секции "Вопросы о важном"')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_answer', DataForFaqSection.FAQ_TEST_DATA
    )
    def test_faq_accordion_opens_correct_answer(self, webdriver_instance, question_locator, answer_locator, expected_answer):
        main_page = MainPage(webdriver_instance)
        main_page.open_page()
        main_page.confirm_cookie()

        main_page.check_answer_text(question_locator, answer_locator, expected_answer)
