from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class DataForOrderCreation:
    ORDER_TEST_DATA = [
        (MainPageLocators.ORDER_BUTTON_ON_PAGE, 'Антон', 'Пальчиков', 'Ленинский проспект 20-56', 'Царицыно',
         '9898989898989', '14.10.2025', 4,
         OrderPageLocators.BLACK_SCOOTER_COLOR_CHECKBOX, 'код от домофона 4289'),
        (MainPageLocators.ORDER_BUTTON_IN_HEADER, 'Иван', 'Капустин', 'Кутузовский проспект, дом 3, квартира 6',
         'Свиблово',
         '1234567891234', '07.11.2025', 6, OrderPageLocators.GREY_SCOOTER_COLOR_CHECKBOX, 'звонок не работает')

    ]