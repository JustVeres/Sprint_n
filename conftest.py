import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from locators import MainPageLocators as MPL
from data.data_page import MainPageData as MPD

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

@pytest.fixture
@allure.step("Предусловие для ввода адресов в поля Откуда и Куда")
def input_all_address_fields(main_page):
    main_page.input_text(MPL.FROM_FIELD, MPD.address_hamovnicheski_34)
    main_page.input_text(MPL.WHERE_FIELD, MPD.address_zubovski_37)

"""Фикстуры для страниц"""
@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page
