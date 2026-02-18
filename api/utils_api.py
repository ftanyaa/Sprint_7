import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

def ping_server():
    return requests.get(f"{BASE_URL}/ping")

def search_metro(station_name):
    return requests.get(f"{BASE_URL}/stations/search?s={station_name}")
