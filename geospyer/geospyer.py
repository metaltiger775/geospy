import json
from .utils import send_image_to_server, display_map

def country(image_path):
    response_data = send_image_to_server(image_path)
    return response_data.get("country")

def city(image_path):
    response_data = send_image_to_server(image_path)
    return response_data.get("city")

def coordinates(image_path):
    response_data = send_image_to_server(image_path)
    return response_data.get("coordinates")

def explanation(image_path):
    response_data = send_image_to_server(image_path)
    return response_data.get("explanation")

def maps(image_path):
    response_data = send_image_to_server(image_path)
    coordinates = response_data.get("coordinates")
    return display_map(coordinates)

def locate(image_path):
    response_data = send_image_to_server(image_path)
    result = {
        "country": response_data.get("country"),
        "city": response_data.get("city"),
        "coordinates": response_data.get("coordinates"),
        "explanation": response_data.get("explanation"),
        "maps_link": display_map(response_data.get("coordinates"))
    }
    return json.dumps(result, indent=4)
