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

    REQUIREMENTS_ORDER_BUTTON = (By.XPATH, "//div[@class='reqs-head' and text()='Требования к заказу']")
    SLIDER_SWITCH_LAPTOP_TABLE = (By.CSS_SELECTOR, "span.slider.round")

    SEARCH_CAR_TITLE = (By.XPATH, "//div[contains(@class,'order-header-title')]")
    SEARCH_CAR_TIME = (By.XPATH, "//div[contains(@class,'order-header-time')]")
    ORDER_CANCEL_BUTTON = (By.XPATH, "//button[contains(@class,'order-button') and .//img[@alt='close']]")
    CANCEL_DIV = (By.XPATH, "//div[text()='Отменить']")
    DETAIL_BUTTON = (By.XPATH, "//button[contains(@class,'order-button') and .//img[@alt='burger']]")
    DETAIL_DIV = (By.XPATH, "//div[text()='Детали']")

    ORDER_HEADER_TITLE = (By.XPATH, "//div[contains(@class,'order-header-title')]")
    CHEVRON_ICON = (By.CSS_SELECTOR, "img[src*='chewron']")
    NUMBER_FIELD = (By.XPATH, "//div[contains(@class,'order-number')]")
    CAR_ICON = (By.XPATH, "//img[@alt='Car' and contains(@src, *)]")

    DRIVER_BLOCK = (By.XPATH, "//div[contains(@class,'order-btn-group')][1]")
    DRIVER_RATING = (By.XPATH, ".//div[contains(@class,'order-btn-rating')]")
    DRIVER_PHOTO = (By.XPATH, ".//img[@alt='close']")
    DRIVER_NAME = (By.XPATH, ".//div[not(@class) and normalize-space(text())]")

    ACTIVE_CARD_PRICE = (By.XPATH, "//div[contains(@class,'tcard active')]//div[contains(@class,'tcard-price')]")
    PRICE_DETAIL = (By.XPATH, "//div[contains(@class,'o-d-sh') and contains(text(),'Стоимость')]")

    OVERLAY = (By.CSS_SELECTOR, "div.overlay")
