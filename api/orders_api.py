import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/orders"

def create_order(firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
    return requests.post(BASE_URL, json={
        "firstName": firstName,
        "lastName": lastName,
        "address": address,
        "metroStation": metroStation,
        "phone": phone,
        "rentTime": rentTime,
        "deliveryDate": deliveryDate,
        "comment": comment,
        "color": color
    })

def get_order_by_track(track):
    return requests.get(f"{BASE_URL}/track?t={track}")

def accept_order(order_id, courier_id):
    return requests.put(f"{BASE_URL}/accept/{order_id}?courierId={courier_id}")

def cancel_order(track):
    return requests.put(f"{BASE_URL}/cancel", json={"track": track})

def finish_order(order_id):
    return requests.put(f"{BASE_URL}/finish/{order_id}", json={"id": order_id})
