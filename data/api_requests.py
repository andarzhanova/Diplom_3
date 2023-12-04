import requests
from data.api_constants import ApiConstants


class Requests:
    @staticmethod
    def get_token(payload):
        token = requests.post(ApiConstants.CREATE_USER, data=payload).json()['accessToken']
        return token

    @staticmethod
    def delete_user(token):
        requests.delete(ApiConstants.DELETE_USER, headers={'Authorization': token})

    @staticmethod
    def create_order(token):
        requests.post(ApiConstants.ORDER, headers={'Authorization': token}, data=ApiConstants.INGREDIENTS)

    @staticmethod
    def get_user_orders(token):
        user_orders = requests.get(ApiConstants.ORDER, headers={'Authorization': token}).json()["orders"]
        return user_orders
