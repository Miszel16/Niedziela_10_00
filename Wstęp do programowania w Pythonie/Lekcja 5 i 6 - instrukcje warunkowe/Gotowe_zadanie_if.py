# Zadanie 1 - czy dane słowo zawiera?
# Napisz program, który sprawdzi, czy w podanym przez użytkownika wyrazie
# znajduje się jedna z następujących liter lub ciągów znaków:
# ● litera „a”
# ● litera „d”
# ● ciąg znaków „as”
# ● ciąg znaków „zzz”

# Jeśli znajdzie choć jedno z nich, program powinien wyświetlić komunikat,
# że wyraz zawiera poszukiwany fragment.

slowo = input("Podaj słowo: ")

if ('a' in slowo) or ('d' in slowo) or ('as' in slowo) or ('zzz' in slowo):
    print("Znaleziono fragment.")
else:
    print("Nie znaleziono fragment.")

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

PIN = "1234"
HASLO = "Masło"

user_pin = input("Podaj pin: ")
if user_pin == PIN:
    user_haslo = input("Podaj hasło")
    if user_haslo == HASLO:
        print("Poprawnie zalogowano")
        print("Uzyskano dostęp do tajnych treści :D")
    else:
        print("Wprowadzono niepoprawne hasło")
else:
    print("Podano niepoprawny pin")

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
#   ➤ prostokątny – spełnia twierdzenie Pitagorasa
#   ➤ rozwartokątny – największy kąt > 90°
#   ➤ ostrokątny – wszystkie kąty < 90°

# ── 1. Wczytanie długości boków ───────────────────────────────────────────────
a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))

# ── 2. Sprawdzenie istnienia trójkąta ─────────────────────────────────────────
if a <= 0 or b <= 0 or c <= 0:
    print("Trójkąt nie może istnieć – wszystkie boki muszą być większe od zera.")
elif (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Trójkąt nie może istnieć – suma dwóch krótszych boków "
          "musi być większa od najdłuższego.")
else:
    # ── 3. Najkrótszy i najdłuższy bok ────────────────────────────────────────
    longest = a
    if b > longest:
        longest = b
    if c > longest:
        longest = c

    shortest = a
    if b < shortest:
        shortest = b
    if c < shortest:
        shortest = c

    print(f"Najkrótszy bok: {shortest}")
    print(f"Najdłuższy bok: {longest}")

    # ── 4. Rodzaj trójkąta ze względu na boki ────────────────────────────────
    if a == b and b == c:
        kind_sides = "równoboczny"
    elif a == b or b == c or a == c:
        kind_sides = "równoramienny"
    else:
        kind_sides = "różnoboczny"
    print(f"Trójkąt {kind_sides}")



    # ── 5. Obwód ─────────────────────────────────────────────────────────────
    print(f"Obwód: {a + b + c}")

    # ── 6. Rodzaj trójkąta ze względu na kąty ────────────────────────────────
    if longest == a:
        p, q = b, c
    elif longest == b:
        p, q = a, c
    else:
        p, q = a, b

    przeciw_prost = p*p + q*q

    if przeciw_prost == longest**2:
        rodzaj = "prostokątny"
    elif przeciw_prost > longest**2:
        rodzaj = "rozwartokątny"
    else:
        rodzaj = "ostrokątny"
    print(f"Trójkąt {rodzaj}")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Zadanie 5 - średnia ocen
# Napisz program, który wczyta od użytkownika oceny końcowe z pięciu przedmiotów:
# matematyka, polski, angielski, informatyka, wf. 
# Następnie wyliczy średnią ocen i wyświetli komunikat czy otrzymamy pasek na świadectwie
# (aby otrzymać czerwony pasek nasza średnia musi być większa lub równa 4.75).

# ── 1. Wczytanie ocen ────────────────────────────────────────────────────────
mat    = float(input("Ocena z matematyki: "))
pol    = float(input("Ocena z języka polskiego: "))
ang    = float(input("Ocena z języka angielskiego: "))
inf    = float(input("Ocena z informatyki: "))
wf     = float(input("Ocena z WF: "))

# ── 2. Obliczenie średniej ───────────────────────────────────────────────────
srednia = (mat + pol + ang + inf + wf) / 5

# ── 3. Komunikaty ────────────────────────────────────────────────────────────
print(f"Średnia ocen: {srednia}")

if srednia >= 4.75:
    print("Gratulacje! Otrzymujesz czerwony pasek na świadectwie.")
else:
    print("Niestety, pasek nie przysługuje.")