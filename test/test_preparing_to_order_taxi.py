import allure
import pytest

class TestPreparingToOrderTaxi:

    @allure.story(
        "3. Подготовка к заказу такси. Ввести два разных предустановленных адреса в поля \"Откуда\" и \"Куда\"")
    @allure.description(
        "При переключении между видами маршрута (Оптимальный\Быстрый) происходит смена активного таба и пересчет времени и стоимости маршрута")
    def test_route_tab_switching_recalculates_time_and_cost(self, open_main_page, input_all_address_fields, main_page):
        with allure.step('Открываем вкладку "Оптимальный"'):
            main_page.click_tab_optimal_tariff()
            price_optimal = main_page.get_route_price()
            duration_optimal = main_page.get_route_duration()

        with allure.step('Проверка: таб "Оптимальный" активен'):
            assert main_page.tab_optimal_tariff_is_visible()

        with allure.step('Открываем вкладку "Быстрый"'):
            main_page.click_tab_fast_tariff()
            price_fast = main_page.get_route_price()
            duration_fast = main_page.get_route_duration()

        with allure.step('Проверка: таб "Быстрый" активен'):
            assert main_page.tab_fast_tariff_is_visible()

        with allure.step('Проверка: происходит пересчет времени и стоимости маршрута'):
            assert duration_optimal != duration_fast
            assert int(price_optimal.split()[2]) != int(price_fast.split()[2])

    @allure.story(
        "3. Подготовка к заказу такси. Ввести два разных предустановленных адреса в поля \"Откуда\" и \"Куда\"")
    @allure.description(
        "При переключении на вид маршрута Свой происходит смена активного таба и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)")
    @pytest.mark.parametrize(
        "transport, transport_text",
        [
            pytest.param("car", "Машина", marks=pytest.mark.xfail(reason="BUG: отображается 'Авто' вместо 'Машина'")),
            ("walk", "Пешком"),
            ("taxi", "Такси"),
            ("bike", "Велосипед"),
            ("scooter", "Самокат"),
            ("drive", "Драйв")
        ]
    )
    def test_switch_to_own_route_tab(self, open_main_page, input_all_address_fields, main_page, transport, transport_text):
        with allure.step('Открываем вкладку "Свой"'):
            main_page.click_tab_mine_tariff()

        with allure.step('Проверка: таб "Свой" активен'):
            main_page.tab_mine_tariff_is_visible()

        with allure.step('Кликаем на каждую иконку транспорта'):
            main_page.click_transport(transport)

        with allure.step('Проверка: иконка транспорта активна'):
            assert main_page.is_transport_active(transport)

        with allure.step('Проверка: отображается текст транспорта'):
            text = main_page.get_transport_text(transport_text)
            assert transport_text in text

    @allure.story("3. Подготовка к заказу такси. Ввести два разных предустановленных адреса в поля \"Откуда\" и \"Куда\"")
    @allure.description('При выборе вида маршрута Быстрый активна кнопка Вызвать такси')
    def test_fast_route_taxi_button_enabled(self, open_main_page, input_all_address_fields, main_page):
        with allure.step('Проверка: отображается кнопка "Вызвать такси"'):
            assert main_page.call_taxi_button_visible()

    @allure.story("3. Подготовка к заказу такси. Ввести два разных предустановленных адреса в поля \"Откуда\" и \"Куда\"")
    @allure.description('При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать')
    def test_own_route_drive_booking_button_enabled(self, open_main_page, input_all_address_fields, main_page):
        with allure.step('Открываем вкладку "Свой"'):
            main_page.click_tab_mine_tariff()

        with allure.step('Кликаем по иконке Драйв'):
            main_page.click_transport("drive")

        with allure.step('Проверка: отображается кнопка "Забронировать"'):
            assert main_page.drive_reserve_button_visible()
