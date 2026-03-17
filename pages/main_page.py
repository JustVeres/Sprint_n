import allure
from pages.base_page import BasePage
from data.data_urls import MAIN_URL
from locators import MainPageLocators as MPL
from helpers import *

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

    @allure.step("Клик по табу 'Оптимальный'")
    def click_tab_optimal_tariff(self):
        self.click(MPL.OPTIMAL_TARIFF_TAB_NOT_ACTIVE)

    @allure.step("Таб 'Оптимальный' активен")
    def tab_optimal_tariff_is_visible(self):
        return self.wait_visible_return(MPL.OPTIMAL_TARIFF_TAB_ACTIVE)

    @allure.step("Клик по табу 'Быстрый'")
    def click_tab_fast_tariff(self):
        self.click(MPL.FAST_TARIFF_TAB_NOT_ACTIVE)

    @allure.step("Таб 'Быстрый' активен")
    def tab_fast_tariff_is_visible(self):
        return self.wait_visible_return(MPL.FAST_TARIFF_TAB_ACTIVE)

    @allure.step("Получаем стоимость маршрута")
    def get_route_price(self):
        return self.wait_visible_return(MPL.ROUTE_PRICE).text

    @allure.step("Получаем время пути")
    def get_route_duration(self):
        return self.wait_visible_return(MPL.ROUTE_DURATION).text

    @allure.step("Клик по табу 'Свой'")
    def click_tab_mine_tariff(self):
        self.click(MPL.MINE_TARIFF_TAB_NOT_ACTIVE)

    @allure.step("Таб 'Свой' активен")
    def tab_mine_tariff_is_visible(self):
        return self.wait_visible_return(MPL.MINE_TARIFF_TAB_ACTIVE)

    @allure.step("Клик по иконке транспорта")
    def click_transport(self, transport):
        self.click(transport_icon(transport))

    @allure.step("Иконка транспорта активна")
    def is_transport_active(self, transport):
        return self.wait_visible_return(transport_icon_active(transport))

    @allure.step("Получаем текст транспорта")
    def get_transport_text(self, transport_name):
        return self.wait_visible_return(transport_text(transport_name)).text

    @allure.step("Ожидаем видимость кнопки 'Вызвать такси'")
    def call_taxi_button_visible(self):
        return self.wait_visible_return(MPL.CALL_TAXI_BUTTON)

    @allure.step("Ожидаем видимость кнопки 'Забронировать'")
    def drive_reserve_button_visible(self):
        return self.wait_visible_return(MPL.DRIVE_RESERVE_BUTTON)
