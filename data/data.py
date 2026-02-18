import random
import string
from datetime import datetime, timedelta

class CourierData:
    @staticmethod
    def random_login():
        return "courier_" + "".join(random.choices(string.ascii_lowercase + string.digits, k=8))

    @staticmethod
    def random_password():
        return "".join(random.choices(string.ascii_letters + string.digits, k=10))

    @staticmethod
    def random_first_name():
        names = ["Naruto", "Sasuke", "Sakura", "Kakashi", "Hinata"]
        return random.choice(names)


class OrderData:
    FIRST_NAME = "Naruto"
    LAST_NAME = "Uchiha"
    ADDRESS = "Konoha, 142 apt."
    METRO_STATION = 4
    PHONE = "+7 800 355 35 35"
    RENT_TIME = 5
    COMMENT = "Saske, come back to Konoha"
    COLOR_BLACK = ["BLACK"]
    COLOR_GREY = ["GREY"]
    COLOR_BOTH = ["BLACK", "GREY"]

    @staticmethod
    def delivery_date(days=1):
        return (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
