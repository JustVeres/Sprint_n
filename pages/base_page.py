import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    """Вспомогательные методы"""
    """Действие: открыть/кликнуть/выбрать/ввести/вернуть etc."""

    @allure.step('Открыть URL')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Кликаем на элемент')
    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.execute_script("arguments[0].click();", element)

    @allure.step('Вводим текст в поле')
    def input_text(self, locator, text):
        element = self.wait_visible_return(locator)
        element.send_keys(text)


    """Ожидание: видимость/исчезновение/поиск"""

    @allure.step('Ожидаем URL')
    def wait_url(self, url):
        self.wait.until(EC.url_to_be(url))

    @allure.step('Ожидаем и возвращаем видимый элемент')
    def wait_visible_return(self, locator): #
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидаем исчезновение элемента')
    def wait_invisible(self, locator, timeout=60):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Ищем элементы')
    def find_elements(self, locator):
        by, value = locator
        return self.driver.find_elements(by, value)

    @allure.step('Ищем элемент')
    def find_element(self, locator):
        by, value = locator
        return self.driver.find_element(by, value)

    """Скрипты"""

    @allure.step("Выполнение JavaScript")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Наведение курсором на элемент")
    def cursor(self, locator):
        element = self.wait_visible_return(locator)
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
