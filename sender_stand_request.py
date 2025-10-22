import configuration
import requests


def create_new_order(order_body, headers):
    return requests.post(configuration.CREATE_ORDER, json=order_body, headers=headers)
    

def get_order(track_number):
    return requests.get(configuration.GET_ORDER_BY_TRACK, params={"t": track_number})