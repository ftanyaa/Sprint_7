import pytest
import allure
from api.courier_api import create_courier, login_courier
from helpers.courier_generator import CourierGenerator


@allure.epic("API Курьеры")
class TestCourierApi:

    @allure.title("Создание курьера с валидными данными")
    def test_create_courier_success(self, created_courier):
        courier = CourierGenerator.generate()
        response = create_courier(courier)
        created_courier.append(courier)
        assert response.status_code == 201

    @allure.title("Создание дубликата курьера")
    def test_create_courier_duplicate(self, created_courier):
        courier = CourierGenerator.generate()
        create_courier(courier)
        created_courier.append(courier)
        response = create_courier(courier)
        assert response.status_code == 409

    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login(self):
        courier = CourierGenerator.generate_without_login()
        response = create_courier(courier)
        assert response.status_code == 400

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password(self):
        courier = CourierGenerator.generate_without_password()
        response = create_courier(courier)
        assert response.status_code == 400

    @allure.title("Авторизация курьера с валидными данными")
    def test_login_courier_success(self, created_courier):
        courier = CourierGenerator.generate()
        create_courier(courier)
        created_courier.append(courier)
        response = login_courier(courier["login"], courier["password"])
        assert response.status_code == 200

    @allure.title("Авторизация курьера с неверным паролем")
    def test_login_wrong_password(self, created_courier):
        courier = CourierGenerator.generate()
        create_courier(courier)
        created_courier.append(courier)
        response = login_courier(courier["login"], "wrongpassword")
        assert response.status_code == 404

    @allure.title("Авторизация курьера без логина")
    def test_login_without_login(self, created_courier):
        courier = CourierGenerator.generate()
        create_courier(courier)
        created_courier.append(courier)
        response = login_courier("", courier["password"])
        assert response.status_code == 400

