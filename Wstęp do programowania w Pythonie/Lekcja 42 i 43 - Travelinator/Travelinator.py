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
    #city = response.json()[0]['name']
    country = response.json()[0]['country']
    return lat, lon, country # [!]



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


# Dokumentacja API - kraje i waluta:
# # https://restcountries.com/
# https://pl.wikipedia.org/wiki/ISO_3166-1 - kody krajów
def get_country_full_name(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    try:
        response = requests.get(url)
        country_name = response.json()[0]['name']['common']
    except:
        return country_code
    else:
        return country_name


def get_currency_code(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code.upper()}"
    response = requests.get(url)
    currency_code = list(response.json()[0]['currencies'].keys())[0]
    return currency_code


def print_weather_info(place):
    lat, lon, _ = check_coordinates(place, API_KEY)
    weather, temperature, pressure, humidity = get_weather_info(lat, lon, API_KEY)
    print(f"Pogoda dla miasta {place}: {weather}")
    print(f"Temperatura: {round(temperature - 273.15)} st. Celcjusza")
    print(f"Ciśnienie: {pressure} hPa")
    print(f"Wilgotność: {humidity} %")



origin_place = None
destination_place = None

while True:
    print('''Jaką akcję chcesz wykonać?
          1. Podaj/zmień miejsce startowe
          2. Podaj/zmień miejsce docelowe
          3. Sprawdź lokalizację miejsca startowego
          4. Sprawdź lokalizację miejsca docelowego
          5. Sprawdź pogodę miejsca startowego
          6. Sprawdź pogodę mijesca docelowego
          7. Dowiedz się o walucie
          8. Koniec''')
    
    option = int(input())

    if option == 1:
        origin_place = input("Podaj miasto startowe.\n")

    elif option == 2:
        destination_place = input("Podaj miasto docelowe.\n")

    elif option == 3:
        if origin_place is not None:
            lat, lon, country = check_coordinates(origin_place, API_KEY)
            country_name = get_country_full_name(country)
            print(f'''Miasto {origin_place} lezy w kraju {country_name}\n 
                  Długość geogrficzna: {lon}, szerokość geograficzna: {lat}''')
        else:
            print("Najpierw musisz podać miasto startowe")

    elif option == 4:
        if destination_place is not None:
            lat, lon, country = check_coordinates(destination_place, API_KEY)
            country_name = get_country_full_name(country)
            print(f'''Miasto {destination_place} lezy w kraju {country_name}\n 
                  Długość geogrficzna: {lon}, szerokość geograficzna: {lat}''')
        else:
            print("Najpierw musisz podać miasto docelowe")

    elif option == 5:
        if origin_place is not None:
            print_weather_info(origin_place)
        else:
            print("Najpierw musisz podać miasto startowe")

    elif option == 6:
        if destination_place is not None:
            print_weather_info(destination_place)
        else:
            print("Najpierw musisz podać miasto docelowe")

    elif option == 7:
        print("W budowie...")
        
        pass

    elif option == 8:
        quit()
    else:
        print("Podano błędną opcję")
    print("Naciśnij enter, aby kontynuować...")
    input()