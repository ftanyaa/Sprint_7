import pytest
from api.courier_api import login_courier, delete_courier


@pytest.fixture
def created_courier():
    couriers = []

    yield couriers

    for courier in couriers:
        response = login_courier(courier["login"], courier["password"])
        if response.status_code == 200:
            courier_id = response.json()["id"]
            delete_courier(courier_id)
