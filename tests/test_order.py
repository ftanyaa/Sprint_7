import pytest
import allure
from api.orders_api import create_order, get_order_by_track
from data.data import OrderData


@allure.epic("API Заказы")
class TestOrderApi:

    @allure.title("Создание заказа с разными цветами самоката")
    @pytest.mark.parametrize(
        "color",
        [
            OrderData.COLOR_BLACK,
            OrderData.COLOR_GREY,
            OrderData.COLOR_BOTH,
            []
        ]
    )
    def test_create_order(self, color):
        with allure.step("Создать заказ"):
            response = create_order(
                OrderData.FIRST_NAME,
                OrderData.LAST_NAME,
                OrderData.ADDRESS,
                OrderData.METRO_STATION,
                OrderData.PHONE,
                OrderData.RENT_TIME,
                OrderData.delivery_date(),
                OrderData.COMMENT,
                color
            )
        with allure.step("Проверить статус код 201 и наличие track"):
            assert response.status_code == 201
            assert "track" in response.json()

    @allure.title("Получение заказа по трек-номеру")
    def test_get_order_by_track(self):
        with allure.step("Создать заказ"):
            response = create_order(
                OrderData.FIRST_NAME,
                OrderData.LAST_NAME,
                OrderData.ADDRESS,
                OrderData.METRO_STATION,
                OrderData.PHONE,
                OrderData.RENT_TIME,
                OrderData.delivery_date(),
                OrderData.COMMENT,
                OrderData.COLOR_BLACK
            )
        track = response.json()["track"]
        with allure.step("Получить заказ по треку"):
            get_response = get_order_by_track(track)
        with allure.step("Проверить статус код 200 и наличие ключа 'order'"):
            assert get_response.status_code == 200
            assert "order" in get_response.json()

