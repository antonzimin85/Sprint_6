from selenium.webdriver.common.by import By


class TrackOrderStatusPageLocators:

    YANDEX_LOGO_IN_HEADER = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    SCOOTER_LOGO_IN_HEADER = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    DZEN_SEARCH_BUTTON = (By.XPATH, ".//button[text()='Найти']")