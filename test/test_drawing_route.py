import pytest
import allure
from data.data_page import MainPageData as MPD

class TestDrawingRoute:

    @allure.story('1. Отрисовка маршрута')
    @allure.description('При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" на карте отображаются две точки начала и конца маршрута')
    @pytest.mark.parametrize(
        "from_address, where_address",
        [
            pytest.param(MPD.address_hamovnicheski_34, MPD.address_zubovski_37, id="route_1"),
            pytest.param(MPD.address_zubovski_37, MPD.address_hamovnicheski_34, id="route_2")
        ]
    )
    def test_route_points_are_displayed(self, open_main_page, main_page, from_address, where_address):
        with allure.step('Заполняем поле "Откуда"'):
            main_page.input_from_address(from_address)
        with allure.step('Заполняем поле "Куда"'):
            main_page.input_where_address(where_address)
        with allure.step('Проверка: на карте отображаются две точки начала и конца маршрута'):
            assert main_page.route_points_are_displayed(from_address, where_address)
