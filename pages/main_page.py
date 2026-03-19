import allure
import re
from pages.base_page import BasePage
from data.data_urls import MAIN_URL
from locators import MainPageLocators as MPL
from helpers import *
from selenium.webdriver.support import expected_conditions as EC

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

    @allure.step("Клик по 'Вызвать такси'")
    def click_call_taxi_button(self):
        self.click(MPL.CALL_TAXI_BUTTON)

    @allure.step("Отображение блока с выбором такси")
    def taxi_selection_block_are_displayed(self):
        return self.wait_visible_return(MPL.TAXI_SELECTION_BLOCK)

    @allure.step("Получаем список всех тарифов на странице")
    def get_all_tariff_titles(self):
        elements = self.find_elements(MPL.TAXI_SELECTION_CARD)
        return [el.text for el in elements]

    @allure.step("Получаем активный тариф")
    def get_active_tariff_title(self):
        return self.find_elements(MPL.TAXI_SELECTION_CARD_ACTIVE)

    @allure.step("Кликаем по тарифу такси")
    def click_tariff_taxi(self, tariff_name):
        self.click(taxi_tariff_card(tariff_name))

    @allure.step("Наведение курсора на i в тарифах такси")
    def pointing_cursor_at_i(self):
        self.cursor(MPL.TARIFF_INFO)

    @allure.step("Находим описание тарифа такси")
    def description_taxi_tariff_text_return(self):
        return self.find_element(MPL.TARIFF_DESCRIPTION).text

    @allure.step("Отображение элементов в тарифе такси")
    def field_visibility(self, field):
        container = self.wait_visible_return(MPL.TARIFF_BLOCK_CONTAINER)
        element = container.find_element(*element_tariff(field))
        self.scroll_to_element(element)
        return self.wait.until(EC.visibility_of(element))

    @allure.step("Клик по кнопке 'Требования к заказу'")
    def click_requirements_order_button(self):
        self.click(MPL.REQUIREMENTS_ORDER_BUTTON)

    @allure.step("Клик по тогглу 'Столик для ноутбука'")
    def click_laptop_table_switcher(self):
        self.click(MPL.SLIDER_SWITCH_LAPTOP_TABLE)

    @allure.step("Клик по кнопке 'Ввести номер и заказать'")
    def click_order_taxi_button(self):
        self.click(MPL.ORDER_TAXI_BUTTON)

    @allure.step("Заголовок 'Поиск машины'")
    def find_text_search_car_title(self):
        return self.find_element(MPL.SEARCH_CAR_TITLE).text

    @allure.step("Таймер обратного отсчета в правом верхнем углу'")
    def find_text_search_car_time(self):
        return self.find_element(MPL.SEARCH_CAR_TIME).text

    @allure.step("Проверка видимости кнопки отмены заказа")
    def check_close_button_visible(self):
        element = self.wait_visible_return(MPL.ORDER_CANCEL_BUTTON)
        return element.is_displayed()

    @allure.step("Проверка видимости текста 'Отменить'")
    def check_cancel_div_visible(self):
        element = self.wait_visible_return(MPL.CANCEL_DIV)
        return element.is_displayed()

    @allure.step("Проверка видимости кнопки с деталями")
    def check_detail_button_visible(self):
        element = self.wait_visible_return(MPL.DETAIL_BUTTON)
        return element.is_displayed()

    @allure.step("Проверка видимости текста 'Детали'")
    def check_detail_div_visible(self):
        element = self.wait_visible_return(MPL.DETAIL_DIV)
        return element.is_displayed()

    @allure.step("Ожидаем исчезновения блока с поиском такси")
    def wait_invisible_search_taxi(self):
        self.wait_invisible(MPL.SEARCH_CAR_TIME)

    @allure.step("Ищем текст в заголовке 'n мин. и приедет'")
    def find_text_min_and_road(self):
        return self.find_element(MPL.ORDER_HEADER_TITLE).text

    @allure.step("Ожидаем видимость иконки >")
    def chevron_icon_visible(self):
        return self.wait_visible_return(MPL.CHEVRON_ICON)

    @allure.step("Получить текст номера такси")
    def get_order_number_text(self):
        element = self.wait_visible_return(MPL.NUMBER_FIELD)
        return element.text.strip()

    @allure.step("Ожидаем видимость иконки авто")
    def car_icon_visible(self):
        return self.wait_visible_return(MPL.CAR_ICON)

    @allure.step("Возвращаем Имя, Рейтинг и фото водителя такси")
    def get_driver_info(self):
        container = self.find_element(MPL.DRIVER_BLOCK)
        rating = container.find_element(*MPL.DRIVER_RATING).text
        photo = container.find_element(*MPL.DRIVER_PHOTO).get_attribute("src")
        name = container.find_element(*MPL.DRIVER_NAME).text
        return {
            "name": name,
            "rating": rating,
            "photo": photo
        }

    @allure.step("Клик по кнопке Детали")
    def click_detail_button(self):
        self.click(MPL.DETAIL_BUTTON)

    @allure.step("Возвращаем стоимость такси для тарифа Рабочий в карточке заказов")
    def get_active_tariff_price(self):
        element = self.find_element(MPL.ACTIVE_CARD_PRICE)
        match = re.search(r"\d+", element.text)
        price = int(match.group())
        return price

    @allure.step("Возвращаем стоимость такси в Деталях")
    def get_order_cost_text(self):
        element = self.find_element(MPL.PRICE_DETAIL)
        match = re.search(r"\d+", element.text)
        price = int(match.group())
        return price

    @allure.step("Клик по кнопке Отменить")
    def click_cancel_button(self):
        self.click(MPL.ORDER_CANCEL_BUTTON)

    @allure.step("Ожидаем закрытие модалки заказа и оверлея")
    def order_modal_and_overlay_close(self):
        self.wait_invisible(MPL.ORDER_HEADER_TITLE, 3)
        self.wait_invisible(MPL.OVERLAY, 3)
