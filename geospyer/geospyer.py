import json
from .utils import send_image_to_server, parse_response

def country(image_path):
    response_data = send_image_to_server(image_path)
    if response_data:
        return parse_response(response_data, 'country')
    else:
        return None

def city(image_path):
    response_data = send_image_to_server(image_path)
    if response_data:
        return parse_response(response_data, 'city')
    else:
        return None

def explanation(image_path):
    response_data = send_image_to_server(image_path)
    if response_data:
        return parse_response(response_data, 'explanation')
    else:
        return None

def coordinates(image_path):
    response_data = send_image_to_server(image_path)
    if response_data:
        return parse_response(response_data, 'coordinates')
    else:
        return None

def maps(image_path):
    response_data = send_image_to_server(image_path)
    if response_data:
        return parse_response(response_data, 'google_maps_link')
    else:
        return None

def locate(image_path):
    response_data = send_image_to_server(image_path)
    if response_data:
        result = {
            'country': parse_response(response_data, 'country'),
            'city': parse_response(response_data, 'city'),
            'explanation': parse_response(response_data, 'explanation'),
            'coordinates': parse_response(response_data, 'coordinates'),
            'google_maps_link': parse_response(response_data, 'google_maps_link'),
        }
        return result
    else:
        return None
