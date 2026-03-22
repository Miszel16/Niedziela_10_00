import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

def scrap_pokemon_list():
    url = "https://pokemondb.net/pokedex/game/lets-go-pikachu-eevee"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, 'html.parser')
    pokemon_list = []

    cards_list = soup.find('div', class_='infocard-list')
    cards_data = cards_list.find_all('span', class_='infocard-lg-data')

    for data in cards_data:
        pokemon_name = data.find('a') #name
        pokemon_number = data.find('small') # numer
        pokemon = (pokemon_name.get_text(), pokemon_number.get_text())
        pokemon_list.append(pokemon)
    
    return pokemon_list


# https://pokeapi.co/
def get_pokemon_info(pokemon_name):
    pokemon_name = pokemon_name.replace('\'','') 
    pokemon_name = pokemon_name.replace('. ','-') 
    pokemon_name = pokemon_name.replace('♀','-f') 
    pokemon_name = pokemon_name.replace('♂','-m') 
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    return response.json()


def get_pokemon_image(pokemon_info):
    link = pokemon_info['sprites']['front_default']
    return link


pokemon_list = scrap_pokemon_list()
pdf = FPDF()
pdf.add_font("DejaVu", "", r"C:\Users\aplac\Documents\Giganci\Projekty Python\Lekcja 44 - Pokedex\Materiały do lekcji\DejaVuSans.ttf", uni=True)

for pokemon in pokemon_list:
    try:
        pokemon_info = get_pokemon_info(pokemon[0]) 
        image_url = get_pokemon_image(pokemon_info) # !!
        img_data = requests.get(image_url).content # !!
        print(f"{pokemon[1]} git")
    except:
        print(pokemon[0])
    else:
        pdf.add_page(format='A5')
        pdf.set_font("DejaVu", size=16)
        pdf.text(x=5, y=10, text=f"{pokemon[1]} {pokemon[0]}")
        pdf.image(img_data, x=30, y=10, w=100, h=100)

pdf.output("pokedex.pdf")
