import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from locators import MainPageLocators as MPL
from data.data_page import MainPageData as MPD
from data.data_urls import MAIN_URL

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
@allure.step("Открытие главной страницы")
def open_main_page(main_page):
    main_page.open_main_page()
    main_page.wait_url(MAIN_URL)

@pytest.fixture
@allure.step("Предусловие для ввода адресов в поля Откуда и Куда")
def input_all_address_fields(main_page):
    from_address = MPD.address_hamovnicheski_34
    where_address = MPD.address_zubovski_37
    main_page.input_text(MPL.FROM_FIELD, from_address)
    main_page.input_text(MPL.WHERE_FIELD, where_address)
    main_page.route_points_are_displayed(from_address, where_address)

@pytest.fixture
@allure.step("Предусловие для выбора маршрута Быстрый и нажатие на Вызвать такси") # маршрут Быстрый выбран по умолчанию
def select_fast_route_and_click_call_taxi(main_page):
    main_page.click_call_taxi_button()

"""Фикстуры для страниц"""
@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page
