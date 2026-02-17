import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

def create_courier(data):
    return requests.post(BASE_URL, json=data)

def login_courier(login, password):
    return requests.post(f"{BASE_URL}/login", json={
        "login": login,
        "password": password
    })

def delete_courier(courier_id):
    return requests.delete(f"{BASE_URL}/{courier_id}")
