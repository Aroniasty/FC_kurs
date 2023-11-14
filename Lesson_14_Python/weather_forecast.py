import requests
from geopy.geocoders import Nominatim
import json

def get_longitude_and_latitude_from_city(city):
    geolocator = Nominatim(user_agent="weather_forecast")
    location = geolocator.geocode(city)
    return location.latitude, location.longitude

def parse_response_to_find_rain(response):
    response_dict = json.loads(response)
    print(type(response_dict))
    print()
    pass

def search_weather_from_api(searched_date, city):
    longitude, latitude = get_longitude_and_latitude_from_city(city)
    url_address = (f"https://api.open-meteo.com/v1/forecast?daily=rain_sum&end_date={searched_date}&hourly=rain"
        f"&latitude={latitude}&longitude={longitude}&start_date={searched_date}&timezone=Europe%2FLondon")
    response = requests.post(url=url_address)
    if response.status_code == 200:
        parse_response_to_find_rain(response.text)
    else:
        print("Niestety, nie mogliśmy pobrać danych pogodowych twojego miasta")
    print(response)
    print(response.text)

def write_data_to_file(city, data, info):
    #otwieramy plik z opcja zapisu

#uruchamiamy to na poczatku
def read_data_from_file(file):

def find_data_in_file():
    for city, weather in data_in_file.items():
        if user_city == city:
            for date, info in data_in_file[city].items():
                if user_date == date:
                    return True
    return False

def search_data_in_file():
    pass

user_city = input("Podaj miasto, dla którego chcesz sprawdzić pogodę: ")
user_date = input("Podaj datę, dla której chcesz sprawdzić pogodę: ")
data_in_file = read_data_from_file(file="opady.json")
if find_data_in_file():
    search_data_in_file()
else:
    search_weather_from_api(searched_date="2023-11-10", city=city)