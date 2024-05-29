import requests
import allure
from url_s import URL

class ApiOrder:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(order: dict):
        response = requests.post(URL.create_an_order, data=order)

        return response

    @staticmethod
    @allure.step('Подтверждение заказа')
    def accept_order(courier_id, order_id):
        payload = {
            "courierId": int(courier_id)
        }
        response = requests.put(
            f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}', params=payload)

        return response

    @staticmethod
    @allure.step('Получить ID заказа по track (Track: {track_order})')
    def get_id_order(track_order):
        payload = {
            "t": track_order
        }
        response = requests.get(URL.get_track, params=payload)

        return response.json()['order']['id']

    @staticmethod
    @allure.step('Вернуть список заказов (ID курьера: {courier_id})')
    def get_list_orders(courier_id):
        payload = {
            "courierId": int(courier_id)
        }
        response = requests.get(URL.create_an_order, params=payload)

        return response