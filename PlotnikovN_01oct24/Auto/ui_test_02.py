# Тест 2: Проверка удаления товара из корзины через UI
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_remove_from_cart_ui(browser):
    browser.get("https://altaivita.ru/")
    # Добавляем товар в корзину
    product = browser.find_element(By.CSS_SELECTOR, ".product-item")  # Замените на реальный селектор
    product.click()
    
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".add-to-cart")  # Замените на реальный селектор
    add_to_cart_button.click()
    
    cart_icon = browser.find_element(By.CSS_SELECTOR, ".cart-icon")  # Замените на реальный селектор
    cart_icon.click()

    # Удаляем товар из корзины
    remove_button = browser.find_element(By.CSS_SELECTOR, ".remove-from-cart")  # Замените на реальный селектор
    remove_button.click()
    
    cart_items = browser.find_elements(By.CSS_SELECTOR, ".cart-item")  # Замените на реальный селектор
    assert len(cart_items) == 0  # Проверяем, что корзина пуста