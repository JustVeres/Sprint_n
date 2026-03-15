import pytest
from selenium import webdriver
from pages.main_page import MainPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def open_main_page(main_page):
    main_page.open_main_page()

"""Фикстуры для страниц"""
@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page
