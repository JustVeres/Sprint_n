import allure
from selenium.common import ElementClickInterceptedException
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

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

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


    """Ожидание: видимость/исчезновение"""

    @allure.step('Ожидаем URL')
    def wait_url(self, url):
        self.wait.until(EC.url_to_be(url))

    @allure.step('Ожидаем и возвращаем видимый элемент')
    def wait_visible_return(self, locator): #
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание видимости элемента')
    def wait_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидаем видимость элемента и возвращаем текст')
    def wait_element_text(self, locator):
        self.wait_visible(locator)
        return self.driver.find_element(*locator).text

    @allure.step("Ожидаем появление элементов")
    def wait_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    """Скрипты"""

    @allure.step("Выполнение JavaScript")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
