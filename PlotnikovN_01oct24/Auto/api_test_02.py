# Тест 2: Проверка получения содержимого корзины
import requests

def test_get_cart_contents():
    url = "https://altaivita.ru/api/cart"  # Замените на реальный API для получения корзины
    response = requests.get(url)

    assert response.status_code == 200
    cart_contents = response.json()
    assert isinstance(cart_contents, list)  # Проверяем, что содержимое корзины — это список
