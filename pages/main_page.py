import allure
from pages.base_page import BasePage
from data.data_urls import MAIN_URL
from locators import MainPageLocators as MPL
from helpers import get_point_locator

class MainPage(BasePage):

    @allure.step('Открыть сайт Яндекс Маршруты')
    def open_main_page(self):
        self.open(MAIN_URL)

    @allure.step('Вводим адрес в поле Откуда')
    def input_from_address(self, address):
        self.input_text(MPL.FROM_FIELD, address)

    @allure.step('Вводим адрес в поле Куда')
    def input_where_address(self, address):
        self.input_text(MPL.WHERE_FIELD, address)

    @allure.step("Отображение точек маршрута")
    def route_points_are_displayed(self, from_address, where_address):
        point_from = self.wait_visible_return(get_point_locator(from_address))
        point_to = self.wait_visible_return(get_point_locator(where_address))
        return point_from.is_displayed() and point_to.is_displayed()

    @allure.step("Отображение блока с выбором маршрута")
    def route_selection_block_are_displayed(self):
        return self.wait_visible_return(MPL.ROUTE_SELECTION_BLOCK)

    @allure.step("Отображение текста 'Авто Бесплатно'")
    def cars_for_free_text_visibility(self):
        return self.wait_visible_return(MPL.CARS_FOR_FREE_TEXT)

    @allure.step("Отображение текста 'В пути 0 мин.'")
    def travel_time_zero_text_visibility(self):
        return self.wait_visible_return(MPL.TRAVEL_TIME_IS_ZERO_TEXT)