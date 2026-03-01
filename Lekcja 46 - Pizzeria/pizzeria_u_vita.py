import json
import pprint
import time

with open('menu.json', 'r', encoding='utf-8') as file:
    menu = json.load(file)

pizzas_full_info = menu['menu']

# pprint.pprint(pizzas_full_info)

list_of_pizzas_name = []
for pizza in pizzas_full_info:
    list_of_pizzas_name.append(pizza['pizza'])

# print(list_of_pizzas_name)
# ---------------------------------------------------------

def display_menu():
    for index, pizza in enumerate(pizzas_full_info):
        print(f"{index+1}. ")
        print(f"Pizza {pizza['pizza']}")
        print(f"Składniki {', '.join(pizza['dodatki'])}")
        print(f"Cena: Mała(S): {pizza['ceny']['S']}zł, Średnia(M): {pizza['ceny']['M']}zł, Duża(L): {pizza['ceny']['L']}zł")
        print(" ")
    input("Wciśnij Enter, aby wrócić do ekranu głównego")
    main_page()


# +: numer: 4, ilość: 2, rozmiar: S 
# -: numer: 4, ilość: 2, rozmiar: SM
def add_to_order():
    print("Którą pizzę chcesz zamówić: ")
    for pizza_name in list_of_pizzas_name:
        print(f"{list_of_pizzas_name.index(pizza_name)+1}.{pizza_name}")
    
    pizza_name_number = int(input("Podaj numer pizzy: "))
    pizza_amount = int(input("Ile pizz chcesz zamówić: "))
    pizza_size = input("Jaki rozmiar mają miec pizze (S/M/L): ")

    order.append({'size': pizza_size,
                  'pizza_amount': pizza_amount,
                  'pizza_name': list_of_pizzas_name[pizza_name_number-1]})

    print(f"Dodano {pizza_amount} x {list_of_pizzas_name[pizza_name_number-1]} [{pizza_size}] do zamówienia.")
    time.sleep(2)
    main_page()


def calculate_cost(ordered_pizza):
    for pizza in pizzas_full_info:
        if pizza['pizza'] == ordered_pizza['pizza_name']:
            cost = int(ordered_pizza['pizza_amount']) * int(pizza['ceny'][ordered_pizza['size']])
    return cost

def send_order():
    tekst = "Dziękujemy za wybranie pizzeri u Vita, podsumowanie:\n"
    total_cost = 0
    for pizza in order:
        cost = calculate_cost(pizza)
        tekst+=f"{pizza['pizza_amount']} x {pizza['pizza_name']}[{pizza['size']}] : {cost}zł\n"
        total_cost += cost
    tekst += f"Łączny koszt: {total_cost}zł"
    print(tekst)

    print("Zamówienie zostało złożone")
    input("Wciśnij Enter, aby kontynuować")
# ---------------------------------------------------------
order = []

def main_page():
    print("Witaj na stronie pizzeri u Vita!")
    print("1. Wyświelt menu")
    print("2. Dodaj pizze do zamówienia")
    print("3. Wyczyść zamówienie")
    print("4. Wyślij zamówienie")
    print("5. Zakończ")

    option = int(input("Wybierz co chcesz zrobić: "))

    if option == 1:
        display_menu()
        pass
    elif option == 2:
        add_to_order()
        pass
    elif option == 3:
        order.clear()
        print("Zamówienie wyczyszczone.")
        main_page()
        pass
    elif option == 4:
        send_order()
        main_page()
        pass
    elif option == 5:
        quit()
    else:
        print("Proszę wpisać poprawny numer opcji :)")

main_page()

