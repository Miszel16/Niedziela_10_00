# # 1. Utwórz trzy zmienne, do których wpisz wartość 3 jako odpowiedni typ:
# # - x_int - jako liczba całkowita
# # - x_float - jako liczba z przecinkiem
# # - x_str - jako napis

# x_int = 3
# x_float = 3.0
# x_str = "3"

# print(x_int, type(x_int))
# print(x_float, type(x_float))
# print(x_str, type(x_str))

# #-----------------------------------------------------------------------------
# # 2. Utwórz zmienną napis_liczba, która przechowuje wartość "290".
# # Utwórz zmienną x. Użyj konwersji z typu str na typ int, aby zmienna x
# # przechowywała to co napis_liczba, ale jako typ liczby całkowitej

# napis_liczba = "290"
# x = int(napis_liczba)

# print(napis_liczba, type(napis_liczba))
# print(x, type(x))

# #-----------------------------------------------------------------------------
# # 3. Utwórz 3 zmienne:
# # - pole_trojkata
# # - podstawa_trojkata, wysokosc_trojkata
# # Do podstawa_trojkata oraz wysokosc_trojkata powinny trafić wartości odczytane z konsoli.
# # Oblicz pole takiego trójkąta i zapisz wynik w zmiennej pole_trojkata
# # Wyświetl wynik jako komunikat:
# # Pole trójkąta o podstawie XX oraz wysokości XX wynosi XX

# podstawa_trojkata = int(input("Podaj podstawę trójkąta: "))
# wysokosc_trojkata = int(input("Podaj wysokość trójkąta: "))
# pole_trojkata = podstawa_trojkata * wysokosc_trojkata / 2

# print(f"Pole trójkąta o podstawie {podstawa_trojkata} oraz wysokości {wysokosc_trojkata} wynosi {pole_trojkata}.")
# #-----------------------------------------------------------------------------
# # 4. Zapytaj użytkownika o jego wiek i na tej podstawie wyświetla w konsoli 
# # jeden z komunikatów:
# # - Jesteś pełnoletni/a
# # - Nie jesteś jeszcze pełnoletni/a. Brakuje Ci XX lat do 18 roku życia
# # Zamiast XX powinna pojawić się wartość liczbowa

# wiek = int(input("Podaj mi swój wiek: "))

# if wiek < 18:
#     print(f"Nie jesteś jeszcze pełnoletni/a. Brakuje Ci {18-wiek} lat do 18 roku życia.")
# else:
#     print("Jesteś pełnoletni/a.")
# #-----------------------------------------------------------------------------
# # 5. Cena atrakcji turystycznej zależy od miesiąca. Napisz program, który zapyta
# # użytkownika o liczbę biletów oraz miesiąc, w którym chce odwiedzić park
# # rozrywki i na tej podstawie obliczy koszt transakcji.
# # Koszt biletu w danym miesiącu (miesiąc jako numer -> koszt biletu):
# # - 1 -> 50 zł
# # - 2 -> 50 zł
# # - 3 -> 100 zł
# # - 4 -> 100 zł
# # - 5 -> 200 zł
# # - 6 -> 200 zł
# # - 7 -> 250 zł
# # - 8 -> 200 zł
# # - 9 -> 200 zł
# # - 10 -> 100 zł
# # - 11 -> 100 zł
# # - 12 -> 50 zł
# # Wyświetl komunikat:
# # "Cena biletów: XX zł"

# # Jeśli wprowadzono niepoprawny numer miesiąc program powinien wyświetlić
# # informację:
# # "Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie"

# liczba_biletow = int(input("Podaj liczbę biletów: "))
# miesiac = int(input("Podaj miesiąc: "))

# if miesiac == (1 or 2 or 12):
#     cena = 50
# elif miesiac == (3 or 4 or 10 or 11):
#     cena = 100
# elif miesiac == (5 or 6 or 8 or 9):
#     cena = 200
# elif miesiac == (7):
#     cena = 250
# else:
#     print("Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie.")

# if 1 <= miesiac <= 12:
#     print(f"Cena biletów: {cena * liczba_biletow} zł")

# #-----------------------------------------------------------------------------
# # 6. Napisz program, który zapyta użytkownika o liczbę, a następnie wypisze na
# # ekranie tyle wyników z rzutu kością sześcienną.
# # Rzut kością sześcienną to wynik z losowania liczby od 1 do 6 (włącznie).
# # Zaawansowane: wyniki zapisać do listy i na koniec wyświetlić
# import random

# n = int(input("Podaj liczbę rzutów kostką: "))
# wyniki = []

# for i in range(n):
#     wyniki.append(random.randint(1, 6))

# print(wyniki)
# #-----------------------------------------------------------------------------
# # 7. Napisz funkcję, która przyjmuje 2 argumenty:
# # - tekst, typu str
# # - n, typu int
# # a zwraca nowy napis, który powstaje poprzez połączenie text n razy.

# def nowy_napis(tekst: str, n: int) -> str:
#     nowy_tekst = tekst * n
#     # nowy_tekst = ""
#     # for i in range(n):
#     #     nowy_tekst += tekst
#     return nowy_tekst

# tekst = input("Podaj tekst: ")
# n = int(input("Podaj liczbę: "))

# nowy_tekst = nowy_napis(tekst, n)
# print(nowy_tekst)

# #-----------------------------------------------------------------------------
# # 8. Przygotuj funkcję, która otrzymuje jeden argument: n - liczbę elementów.
# # Funkcja ma zwrócić listę n - losowych elementów od 0 do 100
# # Wywołaj ją kilka razy, aby sprawdzić, czy za każdym razem zwraca różne wartości
# import random

# def losowa_lista(n: int) -> list:
#     wynik = []
#     for i in range(n):
#         liczba = random.randint(0, 100)
#         wynik.append(liczba)
#     return wynik

# for i in range(5):
#     x = int(input("Podaj liczbę elementów: "))
#     print(losowa_lista(x))



















# #-----------------------------------------------------------------------------
# # 9. Napisz program aplikacji graficznej, która co 3 sekundy zmienia kolor tła.
# # Nowy kolor tła powinien być losowany.
# # Pamiętaj o wykorzystaniu liczby klatek do wykrycia kiedy mijają kolejne 3 sekundy
# # Pamiętaj o budowaniu koloru RGB:
# # RGB składa się z trzech kolorów, każdy może przyjąć wartość od 0 do 255 (włącznie)
# # RGB = [R, G, B] możesz przechowywać to jako listę
# import random
# import pygame
# pygame.init()

# SCREEN_WIDTH = 200
# SCREEN_HEIGHT = 200

# screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Zmiana tła co 3 sekundy")
# clock = pygame.time.Clock()
# FPS = 60
# game_status = True

# background_color = [255, 255, 255]
# frame_counter = 0

# while game_status:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             game_status = False
#         pass
    
#     frame_counter += 1
#     if frame_counter >= FPS * 1.5:
#         background_color = [
#             random.randint(0, 255),
#             random.randint(0, 255),
#             random.randint(0, 255)
#         ]
#         frame_counter = 0

#     screen_surface.fill(background_color)

#     pygame.display.update()
#     clock.tick(FPS)
#     pass
# pygame.quit()
# quit()








# #-----------------------------------------------------------------------------
# # 10.Dodaj do swojego wykrywanie naciśnięcia klawisza 'b'.
# # Jeśli taki klawisz zostanie naciśnięty kolor tła powinien zmienić się na czarny - po
# # puszczeniu klawisza kolor:
# # - powinien zostać na nowo wylosowany - wersja podstawowa
# # - powinien wrócić poprzedni kolor - wersja rozszerzona
# import random
# import pygame
# pygame.init()

# SCREEN_WIDTH = 200
# SCREEN_HEIGHT = 200

# screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Zmiana tła co 3 sekundy")
# clock = pygame.time.Clock()
# FPS = 60
# game_status = True

# background_color = [255, 255, 255]
# frame_counter = 0

# while game_status:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             game_status = False
#         pass
    
#     pressed_keys = pygame.key.get_pressed()

#     if pressed_keys[pygame.K_b]:
#         screen_surface.fill([0, 0, 0])
#     else:
#         frame_counter += 1
#         if frame_counter >= FPS * 1.5:
#             background_color = [
#                 random.randint(0, 255),
#                 random.randint(0, 255),
#                 random.randint(0, 255)
#             ]
#             frame_counter = 0
#         screen_surface.fill(background_color)

#     pygame.display.update()
#     clock.tick(FPS)
#     pass
# pygame.quit()
# quit()