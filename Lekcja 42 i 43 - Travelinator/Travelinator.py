# Program sprawdzający pogodę w dowolnym miejscu na ziemi 
# na podstawie podanego kodu pocztowego, lub szerokości i długości geograficznej.

# 1. Założenie konta: https://home.openweathermap.org/users/sign_in 
# (pdf: https://drive.google.com/file/d/1ybH5wHtecswEcLCLJ8_GNDNGrSJAzczu/view?usp=sharing)

# 2. Utworzenie środowiska wirtualnego 
# (pdf: https://drive.google.com/file/d/140pa_4EQM77eCtlimsrexo6sbAyzPqoS/view?usp=sharing)
# - instalacja biblioteki 'requests'
# - wybieramy nasze nowe venv jako Python Interpreter dla projektu

# 3. Kopiujemy klucz API

import requests
from pprint import pprint

API_KEY = "62a5baf7f44e76a6b77b95d6357197f4"

# Dokumentacja API - pozyskanie geolokalizacji: 
# https://openweathermap.org/api/geocoding-api?collection=other

def check_coordinates(city, API_KEY):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}")
    print(response.status_code)
    pprint(response.json())
    lat = response.json()[0]['lat'] # szerokość geograficzna
    lon = response.json()[0]['lon'] # długość geograficzna
    city = response.json()[0]['name']
    country = response.json()[0]['country']
    return lat, lon, city, country



# Dokumentacja API - pozyskanie pogody:
# https://openweathermap.org/current?collection=current_forecast

def get_weather_info(lat, lon, API_KEY):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
    response_json = response.json()
    weather = response_json['weather'][0]['description'] # pogoda
    temperature = response_json['main']['temp'] # temperatura
    pressure = response_json['main']['pressure'] # ciśnienie
    humidity = response_json['main']['humidity'] # wilgotność
    return weather, temperature, pressure, humidity


print("Witaj, jestem Travelinator, twój inteligentny asystent podróży")

org_city = input("Podaj nazwę miasta, z którego podróżujesz: ")
org_lat, org_lon, org_city, org_country = check_coordinates(org_city, API_KEY)

desc_city = input("Podaj nazwę miasta, do którego podróżujesz: ")
desc_lat, desc_lon, desc_city, desc_country = check_coordinates(desc_city, API_KEY)

print(f"Miasto z ktorego podróżujesz: {org_city}")
print(f"Miasto do ktorego podróżujesz: {desc_city}")
print(f"Współrzędne miasta docelowego to:\n{desc_lat} szerokosci geograficznej i \n{desc_lon} długości geograficznej")

weather, temperature, pressure, humidity = get_weather_info(desc_lat,desc_lon, API_KEY)

print(f"Pogoda : {weather}")
print(f"Temperatura: {round(temperature - 273.15)} st.Celcjusza")
print(f"wilgotność: {humidity}%")
print(f"ciśnienie atmosferyczne {pressure}hPa")
