from selenium.webdriver.common.by import By

def get_point_locator(address_part):
    return By.XPATH, f"//ymaps[contains(text(), '{address_part}')]"