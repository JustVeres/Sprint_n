from selenium.webdriver.common.by import By

def get_point_locator(address_part):
    return By.XPATH, f"//ymaps[contains(text(), '{address_part}')]"

def transport_icon(transport):
    return By.XPATH, f"//img[contains(@src,'{transport}.')]"

def transport_icon_active(transport):
    return By.XPATH, f"//img[contains(@src,'{transport}-active')]"

def transport_text(transport_name):
    return By.XPATH, f"//div[contains(@class,'text') and contains(text(),'{transport_name}')]"

def taxi_tariff_card(tariff_name):
    return By.XPATH, f"//div[@class='tcard-title' and text()='{tariff_name}']"

def element_tariff(element):
    return By.XPATH, f".//div[text()='{element}'] | .//label[text()='{element}'] | //span[text()='{element}']"
