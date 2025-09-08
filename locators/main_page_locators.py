from selenium.webdriver.common.by import By


class MainPageLocators:

    ORDER_BUTTON_IN_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_ON_PAGE = (By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")
    FAQ_SECTION_TITLE = (By.XPATH, ".//div[@class='Home_FourPart__1uthg']/div[@class='Home_SubHeader__zwi_E']")
    CONFIRM_COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    FAQ_QUESTIONS_1 = (By.ID, 'accordion__heading-0')
    FAQ_QUESTIONS_2 = (By.ID, 'accordion__heading-1')
    FAQ_QUESTIONS_3 = (By.ID, 'accordion__heading-2')
    FAQ_QUESTIONS_4 = (By.ID, 'accordion__heading-3')
    FAQ_QUESTIONS_5 = (By.ID, 'accordion__heading-4')
    FAQ_QUESTIONS_6 = (By.ID, 'accordion__heading-5')
    FAQ_QUESTIONS_7 = (By.ID, 'accordion__heading-6')
    FAQ_QUESTIONS_8 = (By.ID, 'accordion__heading-7')
    FAQ_ANSWERS_1 = (By.XPATH, ".//div[@id='accordion__panel-0']/p")
    FAQ_ANSWERS_2 = (By.XPATH, ".//div[@id='accordion__panel-1']/p")
    FAQ_ANSWERS_3 = (By.XPATH, ".//div[@id='accordion__panel-2']/p")
    FAQ_ANSWERS_4 = (By.XPATH, ".//div[@id='accordion__panel-3']/p")
    FAQ_ANSWERS_5 = (By.XPATH, ".//div[@id='accordion__panel-4']/p")
    FAQ_ANSWERS_6 = (By.XPATH, ".//div[@id='accordion__panel-5']/p")
    FAQ_ANSWERS_7 = (By.XPATH, ".//div[@id='accordion__panel-6']/p")
    FAQ_ANSWERS_8 = (By.XPATH, ".//div[@id='accordion__panel-7']/p")
