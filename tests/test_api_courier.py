import pytest
import allure
from api.courier_api import create_courier, login_courier, delete_courier
from helpers.courier_generator import CourierGenerator


@allure.epic("API Курьеры")
class TestCourierApi:

    @allure.title("Создание курьера с валидными данными")
    @allure.description("Проверяем успешное создание курьера и возможность авторизации")
    def test_create_courier_success(self):
        courier = CourierGenerator.generate()
        with allure.step("Создать курьера"):
            response = create_courier(courier)
        with allure.step("Проверить статус код 201"):
            assert response.status_code == 201
        with allure.step("Авторизоваться и удалить курьера"):
            login_response = login_courier(courier["login"], courier["password"])
            courier_id = login_response.json()["id"]
            delete_courier(courier_id)

    @allure.title("Создание дубликата курьера")
    def test_create_courier_duplicate(self):
        courier = CourierGenerator.generate()
        create_courier(courier)
        with allure.step("Попытка создать того же курьера повторно"):
            response = create_courier(courier)
        with allure.step("Проверить статус код 409"):
            assert response.status_code == 409
        with allure.step("Удалить курьера"):
            login_response = login_courier(courier["login"], courier["password"])
            courier_id = login_response.json()["id"]
            delete_courier(courier_id)

    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login(self):
        courier = CourierGenerator.generate_without_login()
        with allure.step("Попытка создать курьера без логина"):
            response = create_courier(courier)
        with allure.step("Проверить статус код 400"):
            assert response.status_code == 400

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password(self):
        courier = CourierGenerator.generate_without_password()
        with allure.step("Попытка создать курьера без пароля"):
            response = create_courier(courier)
        with allure.step("Проверить статус код 400"):
            assert response.status_code == 400

    @allure.title("Авторизация курьера с валидными данными")
    def test_login_courier_success(self):
        courier = CourierGenerator.generate()
        create_courier(courier)
        with allure.step("Авторизация курьера"):
            response = login_courier(courier["login"], courier["password"])
        with allure.step("Проверить статус код 200"):
            assert response.status_code == 200
        with allure.step("Удалить курьера"):
            courier_id = response.json()["id"]
            delete_courier(courier_id)

    @allure.title("Авторизация курьера с неверным паролем")
    def test_login_wrong_password(self):
        courier = CourierGenerator.generate()
        create_courier(courier)
        with allure.step("Авторизация с неверным паролем"):
            response = login_courier(courier["login"], "wrongpassword")
        with allure.step("Проверить статус код 404"):
            assert response.status_code == 404
        with allure.step("Удалить курьера"):
            login_response = login_courier(courier["login"], courier["password"])
            courier_id = login_response.json()["id"]
            delete_courier(courier_id)

    @allure.title("Авторизация курьера без логина")
    def test_login_without_login(self):
        courier = CourierGenerator.generate()
        create_courier(courier)
        with allure.step("Авторизация без логина"):
            response = login_courier("", courier["password"])
        with allure.step("Проверить статус код 400"):
            assert response.status_code == 400
        with allure.step("Удалить курьера"):
            login_response = login_courier(courier["login"], courier["password"])
            courier_id = login_response.json()["id"]
            delete_courier(courier_id)
