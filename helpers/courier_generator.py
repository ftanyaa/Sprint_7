from data.data import CourierData

class CourierGenerator:
    @staticmethod
    def generate():
        login = CourierData.random_login()
        password = CourierData.random_password()
        first_name = CourierData.random_first_name()
        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }

    @staticmethod
    def generate_without_login():
        password = CourierData.random_password()
        first_name = CourierData.random_first_name()
        return {
            "password": password,
            "firstName": first_name
        }

    @staticmethod
    def generate_without_password():
        login = CourierData.random_login()
        first_name = CourierData.random_first_name()
        return {
            "login": login,
            "firstName": first_name
        }
