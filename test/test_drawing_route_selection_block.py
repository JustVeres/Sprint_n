import allure
from data.data_page import MainPageData as MPD

class TestDrawingRouteSelectionBlock:

    @allure.story('2. Отрисовка блока с выбором маршрута')
    @allure.description('При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута')
    def test_different_preset_addresses_show_route_block(self, open_main_page, input_all_address_fields, main_page):
        with allure.step('Проверка: отображается блок с выбором маршрута'):
            assert main_page.route_selection_block_are_displayed()

    @allure.story('2. Отрисовка блока с выбором маршрута')
    @allure.description('При вводе одинакового адреса в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута с текстом "Авто Бесплатно В пути 0 мин."')
    def test_same_address_shows_route_block_with_zero_time(self, open_main_page, main_page):
        with allure.step('Заполняем поле "Откуда" одинаковым адресом'):
            main_page.input_from_address(MPD.address_hamovnicheski_34)

        with allure.step('Заполняем поле "Куда" одинаковым адресом'):
            main_page.input_where_address(MPD.address_hamovnicheski_34)

        with allure.step('Проверка: отображается текст "Авто Бесплатно"'):
            assert main_page.cars_for_free_text_visibility()

        with allure.step('Проверка: отображается текст "В пути 0 мин."'):
            assert main_page.travel_time_zero_text_visibility()
