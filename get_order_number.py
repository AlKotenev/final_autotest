
import requests

URL_SERVICE = "https://56492389-0841-4b9d-abb9-7c338d2274d6.serverhub.praktikum-services.ru"
CREATE_ORDER = "/api/v1/orders"
ORDER_INFORMATION = "/api/v1/orders/track?t="


def test_create_order():
    # Создание заказа
    order_body = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
    response = requests.post(URL_SERVICE + CREATE_ORDER, json=order_body)
    assert response.status_code == 201

    # Получение номера трека заказа
    order_track = response.json()["track"]

    # Получение информации о заказе по номеру трека
    response = requests.get(URL_SERVICE + ORDER_INFORMATION + str (order_track))
    assert response.status_code == 200
    print("тест пройден")
# Алексей Котенев 7 когорта Финальный проект.
