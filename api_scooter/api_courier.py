import requests
import random
import string
import allure
from url_s import URL


class ApiCourier:

    @staticmethod
    @allure.step('Генерация данных и регистрация курьера')
    def register_new_courier_and_return_login_password():

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(URL.create, data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass

    @staticmethod
    @allure.step('Логин курьера')
    def login_courier(login: str, password: str):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(URL.login_courier, data=payload)
        return response

    @staticmethod
    @allure.step('Удалить курьера')
    def delete_courier(id_courier):
        response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{id_courier}')
        return response

    @staticmethod
    @allure.step('Регистрация курьера')
    def registration_courier(login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(URL.create, data=payload)
        return response

    @staticmethod
    @allure.step('Получить ID курьера')
    def get_courier_id(login, password):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(URL.login_courier, data=payload)

        if response.status_code == 200:
            return response.json()['id']
        else:
            return 0