# https://github.com/Miszel16/Niedziela_11_45

# 1. Co to jest instrukcja warunkowa i do czego służy w języku Python?

# 2. Jak działają instrukcje if-elif-else? W jakiej sytuacji ich użyjemy?

# 3. Dlaczego w Pythonie ważne są wcięcia (ang. indentation) w instrukcjach warunkowych?

# 4. Ile instrukcji elif możemy dodać?

# 5. Jakie operatory logiczne możemy wykorzystać do tworzenia bardziej złożonych warunków?

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Zadanie 1 - czy dane słowo zawiera?
# Napisz program, który sprawdzi, czy w podanym przez użytkownika wyrazie
# znajduje się jedna z następujących liter lub ciągów znaków:
# ● litera „a”
# ● litera „d”
# ● ciąg znaków „as”
# ● ciąg znaków „zzz”

# Jeśli znajdzie choć jedno z nich, program powinien wyświetlić komunikat,
# że wyraz zawiera poszukiwany fragment.

slowo = input("Podaj dowolne słowo: ")

if ('a' in slowo) or ('d' in slowo) or ('as' in slowo) or ('zzz' in slowo):
    print("Znaleziono fragment")
else:
    print('Nie znaleziono.')

# if ('a' or 'd' or 'as' or 'zzz' in slowo):


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 2 - system logowania
# Napisz program, który będzie działał jak podstawowy system logowania.
# Wykonaj poniższe kroki:

# import getpass

# # 1. Zapisz dane do logowania w zmiennych:
# LOGIN = "gigant@trener.pl"
# HASLO = "qwerty"

# # 2. Pobrac login i hasło od uzytkownika

# login_podany = input("Podaj login: ")
# haslo_podane = getpass.getpass("Podaj haslo: ")

# # 3. Sprawdzamy zgodnosc danych (if)

# if login_podany == LOGIN and haslo_podane == HASLO:
#     print("Zalogowano pomyślnie")
# else:
#     print("Błąd logowania")




#Dodatkowo: getpass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 3 - logowanie dwuetapowe
# Stwórz program, który obsłuży proces dwuetapowego logowania. Użytkownik
# zostanie poproszony o wprowadzenie czterocyfrowego PINu. Jeśli poda błędny
# PIN, program wyświetli odpowiedni komunikat o błędzie. W przypadku poprawnego
# PINu, użytkownik zostanie następnie poproszony o podanie hasła słownego.

PIN = "1234"
Haslo = "Masło"

# PIN powinien być przechowywany jako tekst czy liczba?

PIN_podany = input("Podaj PIN: ")

if PIN_podany == PIN:
    haslo_podane = input("Podaj hasło: ")
    if haslo_podane == Haslo:
        print("Zalogowano poprawnie.")
    else:
        print("Złe hasło")
else:
    print("Zły PIN")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 4 - matematyczny pomocnik do trójkątów.
# Napisz program, który wczyta od użytkownika długości trzech boków trójkąta, a
# następnie:

# 1. Sprawdzi, czy taki trójkąt może istnieć:
# ○ Każdy bok musi być większy od zera.
# ○ Suma długości dwóch krótszych boków musi być większa niż długość najdłuższego.
# ○ Jeśli te warunki nie są spełnione – wyświetl odpowiedni komunikat i zakończ program.

# 2. Wyświetli:
# ○ Najkrótszy i najdłuższy bok.
# ○ Rodzaj trójkąta ze względu na długości boków:
#   ➤ równoboczny – wszystkie boki równe
#   ➤ równoramienny – dwa boki równe
#   ➤ różnoboczny – wszystkie boki różne
# ○ Obwód trójkąta.
# ○ Rodzaj trójkąta ze względu na kąty:
# a b c - najdłuższy

# a**2 + b**2 = c**2

#   ➤ prostokątny –  a**2 + b**2 = c**2
#   ➤ rozwartokątny – a**2 + b**2 < c**2
#   ➤ ostrokątny – a**2 + b**2 > c**2

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 5 - średnia ocen
# Napisz program, który wczyta od użytkownika oceny końcowe z pięciu
# przedmiotów: matematyka, polski, angielski, informatyka, wf. Następnie wyliczy
# średnią ocen i wyświetli komunikat czy otrzymamy pasek na świadectwie
# (aby otrzymać czerwony pasek nasza średnia musi być większa lub równa 4.75).

