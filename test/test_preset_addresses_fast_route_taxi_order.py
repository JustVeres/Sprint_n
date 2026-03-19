import allure
import pytest
import re

class TestPresetAddressesFastRouteTaxiOrder:

    @allure.story("5.Сценарий. Ввести два разных предустановленных адреса в поля \"Откуда\" и \"Куда\", выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси")
    @allure.description("Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать - Появляется окно ожидания машины (проверить элементы по ТЗ)")
    def test_work_tariff_notebook_table_waiting_screen_validation(self, open_main_page, input_all_address_fields, select_fast_route_and_click_call_taxi, main_page):

        with allure.step('Раскрываем Требования к заказу'):
            main_page.click_requirements_order_button()

        with allure.step('Активируем свитчер "Столик для ноутбука"'):
            main_page.click_laptop_table_switcher()

        with allure.step('Кликаем по кнопке заказа такси'):
            main_page.click_order_taxi_button()

        with allure.step('Проверка: заголовок Поиск машины'):
            assert main_page.find_text_search_car_title() == "Поиск машины"

        with allure.step('Проверка: таймер обратного отсчета в правом верхнем углу'):
            time_text = main_page.find_text_search_car_time()
            minutes, seconds = time_text.split(":")
            assert minutes.isdigit()
            assert seconds.isdigit()

        with allure.step('Проверка: видимость кнопки Отменить'):
            assert main_page.check_close_button_visible()
            assert main_page.check_cancel_div_visible()

        with allure.step('Проверка: видимость кнопки Детали'):
            assert main_page.check_detail_button_visible()
            assert main_page.check_detail_div_visible()


    @allure.story("5.Сценарий. Ввести два разных предустановленных адреса в поля \"Откуда\" и \"Куда\", выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси")
    @allure.description("Дождаться окончания таймера поиска машины - Отображается окно совершенного заказа (проверить элементы по ТЗ)")
    def test_search_timer_ends_shows_order_screen(self, open_main_page, input_all_address_fields, select_fast_route_and_click_call_taxi, order_taxi_final_screen_order, main_page):

        with allure.step('Проверка: заголовок "n мин. и приедет >"'):
            assert "мин. и приедет" in main_page.find_text_min_and_road()
            assert main_page.chevron_icon_visible()

        with allure.step("Проверяем, что номер заказа отображается и содержит цифры"):
            text = main_page.get_order_number_text()
            assert text != "", "Поле с номером пустое!"
            assert re.search(r"\d+", text), f"Текст не содержит цифр: '{text}'"

        with allure.step('Проверка: отображается иконка с авто'):
            assert main_page.car_icon_visible()

        with allure.step('Проверка: иконка водителя'):
            driver_info = main_page.get_driver_info()
            assert driver_info["name"], "Имя водителя пустое"
            assert driver_info["rating"], "Рейтинг пустой"
            assert any(c.isdigit() for c in driver_info["rating"]), "Рейтинг не содержит цифры"
            assert driver_info["photo"], "Фото водителя не найдено"

        with allure.step('Проверка: кнопка Отменить'):
            assert main_page.check_close_button_visible()
            assert main_page.check_cancel_div_visible()

        with allure.step('Проверка: видимость кнопки Детали'):
            assert main_page.check_detail_button_visible()
            assert main_page.check_detail_div_visible()


    @allure.story("5.Сценарий. Ввести два разных предустановленных адреса в поля \"Откуда\" и \"Куда\", выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси")
    @allure.description("Нажать кнопку Детали в блоке Еще про поездку - Указана стоимость, которая была при выборе тарифа")
    def test_trip_details_price_matches_selected_tariff(self, open_main_page, input_all_address_fields, select_fast_route_and_click_call_taxi, order_taxi_final_screen_order, main_page):

        with allure.step('Открываем Детали'):
            main_page.click_detail_button()

        with allure.step('Проверка: указана стоимость, которая была при выборе тарифа'):
            assert select_fast_route_and_click_call_taxi == main_page.get_order_cost_text()


    @pytest.mark.xfail(reason="BUG: модальное окно не закрывается после клика по кнопке Отменить")
    @allure.story("5.Сценарий. Ввести два разных предустановленных адреса в поля \"Откуда\" и \"Куда\", выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси")
    @allure.description("Нажать кнопку Отмена - Окно закрывается")
    def test_modal_closes_after_cancel_click(self, open_main_page, input_all_address_fields, select_fast_route_and_click_call_taxi, order_taxi_final_screen_order, main_page):

        with allure.step('Клик по кнопке Отменить'):
            main_page.click_cancel_button()

        with allure.step('Проверка: окно заказа такси закрывается'):
            assert main_page.order_modal_and_overlay_close()
