from selenium.webdriver.common.by import By

class MainPageLocators:
    FROM_FIELD = (By.ID, "from")
    WHERE_FIELD = (By.ID, "to")
    ROUTE_SELECTION_BLOCK = (By.CLASS_NAME, "type-picker")

    OPTIMAL_TARIFF_TAB_NOT_ACTIVE = (By.XPATH, "//div[@class='mode' and text()='Оптимальный']")
    OPTIMAL_TARIFF_TAB_ACTIVE = (By.XPATH, "//div[@class='mode active' and text()='Оптимальный']")
    FAST_TARIFF_TAB_NOT_ACTIVE = (By.XPATH, "//div[@class='mode' and text()='Быстрый']")
    FAST_TARIFF_TAB_ACTIVE = (By.XPATH, "//div[@class='mode active' and text()='Быстрый']")
    MINE_TARIFF_TAB_NOT_ACTIVE = (By.XPATH, "//div[@class='mode' and text()='Свой']")
    MINE_TARIFF_TAB_ACTIVE = (By.XPATH, "//div[@class='mode active' and text()='Свой']")

    CALL_TAXI_BUTTON = (By.XPATH, "//button[normalize-space()='Вызвать такси']")
    DRIVE_RESERVE_BUTTON = (By.XPATH, "//button[normalize-space()='Забронировать']")
    ROUTE_PRICE = (By.XPATH, "//div[contains(@class,'text')]")
    ROUTE_DURATION = (By.XPATH, "//div[contains(@class,'duration')]")
    CARS_FOR_FREE_TEXT = (By.XPATH, "//div[text()='Авто Бесплатно']")
    TRAVEL_TIME_IS_ZERO_TEXT = (By.XPATH, "//div[text()='В пути 0 мин.']")
    TAXI_SELECTION_BLOCK = (By.CLASS_NAME, "tariff-cards")
    TAXI_SELECTION_CARD = (By.CSS_SELECTOR, ".tcard-title")
    TAXI_SELECTION_CARD_ACTIVE = (By.CSS_SELECTOR, ".tcard.active .tcard-title")
    TARIFF_INFO = (By.CSS_SELECTOR, ".tcard.active .tcard-i")
    TARIFF_DESCRIPTION = (By.XPATH, "//div[contains(@class,'tcard active')][.//div[contains(@class,'i-dPrefix')]]")
    TARIFF_BLOCK_CONTAINER = (By.CSS_SELECTOR, "div.tariff-picker.shown")
    TELEPHONE_FIELD = (By.XPATH, "//div[text()='Телефон']")
    ORDER_TAXI_BUTTON = (By.XPATH, "//span[contains(@class,'smart-button-main')]")
