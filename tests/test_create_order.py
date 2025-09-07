import allure
import pytest

from data.data_for_order_creation import DataForOrderCreation
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.track_order_status_page import TrackOrderStatusPage


class TestOrderCreation:

    @allure.title('Проверка оформление заказа самоката')
    @allure.description('Проверка полного позитивного флоу оформления заказа самоката с разными тестовыми данными с проверкой корректности урлов при переходах')
    @pytest.mark.parametrize(
        'order_button, first_name, second_name, address, metro_station, phone_number, order_date, order_period_index, '
        'scooter_color_checkbox, order_comment', DataForOrderCreation.ORDER_TEST_DATA
    )
    def test_order_creation_valid_order_data_order_created(
            self, webdriver_instance, order_button, first_name, second_name, address, metro_station, phone_number,
            order_date, order_period_index, scooter_color_checkbox, order_comment
    ):

        main_page = MainPage(webdriver_instance)
        main_page.open_page()
        main_page.confirm_cookie()
        main_page.click_order_button(order_button)

        order_page = OrderPage(webdriver_instance)
        order_page.place_order(
            first_name, second_name, address, metro_station, phone_number, order_date, order_period_index,
            scooter_color_checkbox, order_comment
        )

        order_page.check_order_confirmation_title_is_displayed()
        order_page.check_order_confirmation_title_include_expected_text()
        order_page.click_on_watch_order_status_button()

        track_order_status_page = TrackOrderStatusPage(webdriver_instance)
        track_order_status_page.click_on_yandex_logo_in_header()
        current_tab = track_order_status_page.return_current_tab()

        track_order_status_page.check_dzen_page_is_opened()
        track_order_status_page.close_current_tab()
        track_order_status_page.switch_to_new_tab(current_tab)

        track_order_status_page.click_on_scooter_logo_in_header()
        track_order_status_page.check_main_page_is_opened()



