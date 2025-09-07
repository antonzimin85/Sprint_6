from selenium.webdriver.common.by import By


class OrderPageLocators:

    ORDER_PAGE_TITLE = (By.CLASS_NAME, 'Order_Header__BZXOb')
    FIRST_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Имя']")
    SECOND_NAME_FIELD = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, ".//div[@class='select-search__value']")
    METRO_STATION_FIELD_HAS_FOCUS = (By.XPATH, ".//div[@class='select-search has-focus']//input[@placeholder='* Станция метро']")
    METRO_STATION_VALUE_IN_DROPDOWN = (By.XPATH, ".//ul[@class='select-search__options']/li[@data-index='0']")
    PHONE_NUMBER_FIELD = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    ORDER_DATE_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    ORDER_DATE_ON_DATEPICKER = (By.XPATH, ".//div[@class='react-datepicker__week']/div[@tabindex='0']")
    ORDER_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-control')
    ORDER_PERIOD_VALUES = (By.CLASS_NAME, 'Dropdown-option')
    BLACK_SCOOTER_COLOR_CHECKBOX = (By.ID, 'black')
    GREY_SCOOTER_COLOR_CHECKBOX = (By.ID, 'grey')
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    CONFIRM_ORDER_MODAL_WINDOW_TITLE = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    NO_BUTTON_ON_CONFIRM_ORDER_MODAL_WINDOW = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']//button[text()='Нет']")
    YES_BUTTON_ON_CONFIRM_ORDER_MODAL_WINDOW = (By.XPATH, ".//div[@class='Order_Modal__YZ-d3']//button[text()='Да']")
    SUBMIT_ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    WATCH_ORDER_STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")
