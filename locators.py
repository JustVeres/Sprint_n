from selenium.webdriver.common.by import By

class MainPageLocators:
    FROM_FIELD = (By.ID, "from")
    WHERE_FIELD = (By.ID, "to")
    ROUTE_SELECTION_BLOCK = (By.CLASS_NAME, "type-picker")
    CARS_FOR_FREE_TEXT = (By.XPATH, "//div[text()='Авто Бесплатно']")
    TRAVEL_TIME_IS_ZERO_TEXT = (By.XPATH, "//div[text()='В пути 0 мин.']")

    #text = "Travel time is 0 min."
    #print(text.upper())