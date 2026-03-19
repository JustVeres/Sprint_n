import allure
import pytest
from data.data_page import MainPageData as MPD

class TestOrderingTaxiFare:

    @allure.story("4. Заказ тарифа Такси. Ввести два разных предустановленных адреса в поля 'Откуда' и 'Куда', выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси")
    @allure.description('Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный')
    def test_order_form_displays_six_tariffs_one_active(self, open_main_page, input_all_address_fields, select_fast_route_and_click_call_taxi, main_page):

        with allure.step('Проверка: отображается блок с выбором такси'):
            assert main_page.taxi_selection_block_are_displayed()

        with allure.step("Проверка всех тарифов на странице"):
            tariffs_on_page = main_page.get_all_tariff_titles()
            for tariff in MPD.expected_tariffs:
                assert tariff in tariffs_on_page

        with allure.step("Проверка, что один тариф активный"):
            active_tariff = main_page.get_active_tariff_title()
            assert len(active_tariff) == 1


    @allure.story("4. Заказ тарифа Такси. Ввести два разных предустановленных адреса в поля 'Откуда' и 'Куда', выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси")
    @allure.description('При наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ')
    @pytest.mark.parametrize("tariff_name, tariff_description",
        [
            ("Рабочий", "Для деловых особ, которых отвлекают"),
            pytest.param("Сонный", "Для тех, кто не выспался", marks=pytest.mark.xfail(reason="BUG: отображается 'Если мысли не выходят из головы' вместо 'Для тех, кто не выспался' в тарифе Сонный")),
            ("Отпускной", "Если пришла пора отдохнуть"),
            pytest.param("Разговорчивый", "Если мысли не выходят из головы", marks=pytest.mark.xfail(reason="BUG: отображается 'Для тех, кто не выспался' вместо 'Если мысли не выходят из головы' в тарифе Разговорчивый")),
            ("Утешительный", "Если хочется свернуться калачиком"),
            ("Глянцевый", "Если нужно блистать")
        ])
    def test_tariff_info_tooltip_content(self, open_main_page, input_all_address_fields, select_fast_route_and_click_call_taxi, main_page, tariff_name, tariff_description):

        with allure.step("Кликаем по тарифу такси"):
            main_page.click_tariff_taxi(tariff_name)

        with allure.step("Наводим курсом на i"):
            main_page.pointing_cursor_at_i()

        with allure.step("Проверка: описание тарифа такси"):
            description_text = main_page.description_taxi_tariff_text_return()
            assert tariff_name in description_text
            assert tariff_description in description_text


    @allure.story("4. Заказ тарифа Такси. Ввести два разных предустановленных адреса в поля 'Откуда' и 'Куда', выбрать вид маршрута Быстрый, нажать кнопку Вызвать такси")
    @allure.description('Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси')
    @pytest.mark.parametrize("element", ['Телефон',
                                         'Способ оплаты',
                                         pytest.param('Комментарий водителю', marks=pytest.mark.xfail(reason="BUG: поле называется 'Комментарий водителю...'")),
                                         'Требования к заказу',
                                         'Ввести номер и заказать'])
    def test_order_form_fields_visibility(self, open_main_page, input_all_address_fields, select_fast_route_and_click_call_taxi, main_page, element):

        with allure.step("Проверка отображения элемента"):
            assert main_page.field_visibility(element)
