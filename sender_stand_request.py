import requests
import configuration

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)

def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO_BY_TRACK + track)
