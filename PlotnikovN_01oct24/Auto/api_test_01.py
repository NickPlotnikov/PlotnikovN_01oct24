# Тест 1: Проверка добавления товара в корзину
import requests

def test_add_to_cart():
    url = "https://altaivita.ru/api/cart/add"  # Замените на реальный API для добавления в корзину
    payload = {
        "product_id": 123,  # ID товара
        "quantity": 1
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 200
    assert response.json().get("message") == "Товар добавлен в корзину"
