# 1. Co to jest instrukcja warunkowa i do czego służy w języku Python?

# 2. Jak działają instrukcje if-elif-else? W jakiej sytuacji ich użyjemy?

# 3. Dlaczego w Pythonie ważne są wcięcia (ang. indentation) w instrukcjach warunkowych?

# 4. Ile instrukcji elif możemy dodać?

# 5. Jakie operatory logiczne możemy wykorzystać do tworzenia bardziej złożonych warunków?


# Zadanie 1 - czy dane słowo zawiera?
# Napisz program, który sprawdzi, czy w podanym przez użytkownika wyrazie
# znajduje się jedna z następujących liter lub ciągów znaków:
# ● litera „a”
# ● litera „d”
# ● ciąg znaków „as”
# ● ciąg znaków „zzz”

# Jeśli znajdzie choć jedno z nich, program powinien wyświetlić komunikat,
# że wyraz zawiera poszukiwany fragment.

# slowo = input("Podaj słowo: ")

# if ('a' in slowo) or ('d' in slowo) or ('as' in slowo) or ('zzz' in slowo):
#     print("Znaleziono fragment.")
# else:
#     print("Nie znaleziono fragment.")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 2 - system logowania
# Napisz program, który będzie działał jak podstawowy system logowania.
# Wykonaj poniższe kroki:
# 1. Zapisz dane do logowania w zmiennych:
# ○ LOGIN = "gigant@trener.pl"
# ○ HASLO = "qwerty"

# 2. Poproś użytkownika o podanie loginu (za pomocą input()).

# 3. Poproś użytkownika o podanie hasła.

# 4. Sprawdź, czy wprowadzone dane są zgodne z zapisanymi loginem i hasłem:
# ○ jeśli tak – wyświetl komunikat: "Poprawnie zalogowano"
# ○ jeśli nie – wyświetl komunikat: "Niepoprawny login lub hasło"

#Dodatkowo: getpass
import getpass

LOGIN = "TrenerAlicja"
HASLO = "zaq12wsx"

user_login = input("Podaj login: ")
user_haslo = getpass.getpass("Podaj haslo: ")

if user_login == LOGIN and user_haslo == HASLO:
    print("Zalogowano poprawnie.")

else:
    print("Niepoprawny login lub hasło.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 3 - logowanie dwuetapowe
# Stwórz program, który obsłuży proces dwuetapowego logowania. Użytkownik
# zostanie poproszony o wprowadzenie czterocyfrowego PINu. Jeśli poda błędny
# PIN, program wyświetli odpowiedni komunikat o błędzie. W przypadku poprawnego
# PINu, użytkownik zostanie następnie poproszony o podanie hasła słownego.

# PIN: „1234”
# Hasło: „Masło”

# PIN powinien być przechowywany jako tekst czy liczba?

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 4 - matematyczny pomocnik do trójkątów.
# Napisz program, który wczyta od użytkownika długości trzech boków trójkąta, a
# następnie:
# 1. Sprawdzi, czy taki trójkąt może istnieć:
# ○ Każdy bok musi być większy od zera.
# ○ Suma długości dwóch krótszych boków musi być większa niż długość
# najdłuższego.
# ○ Jeśli te warunki nie są spełnione – wyświetl odpowiedni komunikat i
# zakończ program.

# 2. Wyświetli:
# ○ Najkrótszy i najdłuższy bok.
# ○ Rodzaj trójkąta ze względu na długości boków:
#   ➤ równoboczny – wszystkie boki równe
#   ➤ równoramienny – dwa boki równe
#   ➤ różnoboczny – wszystkie boki różne
# ○ Obwód trójkąta.
# ○ Rodzaj trójkąta ze względu na kąty:
#   ➤ prostokątny – spełnia twierdzenie Pitagorasa
#   ➤ rozwartokątny – największy kąt > 90°
#   ➤ ostrokątny – wszystkie kąty < 90°

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zadanie 5 - średnia ocen
# Napisz program, który wczyta od użytkownika oceny końcowe z pięciu
# przedmiotów: matematyka, polski, angielski, informatyka, wf. Następnie wyliczy
# średnią ocen i wyświetli komunikat czy otrzymamy pasek na świadectwie
# (aby otrzymać czerwony pasek nasza średnia musi być większa lub równa 4.75).