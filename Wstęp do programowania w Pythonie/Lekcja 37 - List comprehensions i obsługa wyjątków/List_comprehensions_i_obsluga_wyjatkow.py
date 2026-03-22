# Pytania powtórzeniowe
# 1. Jakie struktury znamy?
# 2. Porównanie i ich własności.


# 1. LIST COMPREHENSIONS 
# - krótki i czytelny sposób tworzenia nowej listy
#   na podstawie istniejącej kolekcji/iterowalnego źródła


# 1️⃣ Lista — kwadraty liczb 1–10
lista1 = []
for i in range(1,6):
    lista1.append(i**2)


lista2 = [i**2 for i in range(1,6)]

print(lista1)
print(lista2)




lista3 = []
for i in range(1,11):
    if i%2==0:
        lista3.append(i)

lista4 = [i for i in range(1,11) if i%2==0]

print(f"{lista3}\n")
print(lista4)







print("\n\n\n\n")
lista_bazowa = [1,2,3,4,5,6,7,8,9,10]
lista = [i**2 for i in lista_bazowa]
print(lista)

# ----------------------------------------------------------
# 2️⃣ Inne struktury: generator, zbiór, słownik
zbior = {i**2 for i in lista_bazowa}
print(zbior)

slownik = {i : i**2 for i in lista_bazowa}
print(slownik)

generator = (i**2 for i in lista_bazowa)
print(generator)

krotka = tuple([i**2 for i in lista_bazowa])
print(krotka)

# ----------------------------------------------------------
# 3️⃣ Warunek w list comprehension

lista_nieparzysta = [i for i in lista_bazowa if i%2!=0]
print(lista_nieparzysta)

# ----------------------------------------------------------
# 4 Łączenie elementów z kilku list — zip()

panstwa = ["Polska", "Hiszpania", "Francja", "Czechy", "Włochy"]
stolice = ["Warszawa", "Madryt", "Paryż", "Praga", "Rzym"]

informacje = [f"{miasto} to stolica {kraj}" for kraj, miasto in zip(panstwa, stolice)]

for i in informacje:
    print(i)



# ĆWICZENIA
# 1. Na podstawie podanej listy 
slowa = ["ala", "kot", "pies", "kamilslimak", "zebra", "madam", "Adam"]
# stwórz listę zawierającą same palindromy
# (wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej).

palindromy = [i for i in slowa if i[::1] == i[::-1]] # start, stop, step
print(palindromy)


# ---------------------------------------------------------------------------------
# 2. Na podstawie listy krotek zawierającej długości boków trójkąta 
# stwórz listę zawierającą tylko krotki z których można skonstruować trójkąt
# (warunek - najdłuższy bok musi być krótszy niż suma dwóch pozostałych).
trojkaty = [(1, 3, 5), (2, 2, 3), (3, 1, 8), (3, 4, 5)]




# ---------------------------------------------------------------------------------
# 3. Na podstawie listy z temperaturą podaną w stopniach Fahrenhaita
# stwórz listę zawierającą te same temperatury w stopniach Celcjusza
# (https://pl.farnell.com/kalkulator-konwersji-temperatury)
# ((Fahrenhaita - 32)*5/9 = Celcjusza)
stopnie_fahrenheit = [32, 68, 104, 140]





# ---------------------------------------------------------------------------------
# 4. Z podanego ciągu znaków usuń znaki nie będące literami ani cyframi.
ciag_znakow = "hello@123world!456"

litery_i_cyfry = [znak for znak in ciag_znakow if(znak.isalpha() or znak.isdigit())]

print(f"{litery_i_cyfry}\n")

# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------

# 2. OBSŁUGA WYJĄTKÓW
# - „sygnał błędu”, który pojawia się, 
# gdy program nie może poprawnie kontynuować działania

# „Spróbuj wykonać ten kod. Jeśli pojawi się błąd → obsłuż go elegancko.”

try:
    # ryzykowny kod
    pass
except TypeError:
    # co zrobic gdy ten bląd się pojawi
    pass
except Exception:
    # co zrobić jak inny błąd
    pass
else: 
    # wykona sie jesli NIE było żadnego błędu
    pass
finally:
    # wykona się ZAWSZE
    pass



# Rodzaje błędów:

#1.
ZeroDivisionError
# Gdy próbujesz dzielić przez zero (także // albo %)


#2.
OverflowError
# Gdy wynik operacji liczbowej jest za duży, żeby go przedstawić w danym typie 
# (głównie przy funkcjach z math, np. ekstremalne math.exp()).


#3.
FloatingPointError
# Błędy obliczeń na liczbach zmiennoprzecinkowych, gdy włączone jest zgłaszanie takich błędów 
# (np. przez biblioteki naukowe). W „czystym” Pythonie praktycznie nie pojawia się sam z siebie.


#4.
AssertionError
# Gdy instrukcja assert jest fałszywa:
# assert x > 0   # jeśli x <= 0 → AssertionError


#5.
AttributeError
# Gdy próbujesz odczytać lub ustawić atrybut, którego obiekt nie ma:
# "tekst".append("a")   # string nie ma metody append


#6.
EOFError
# Gdy funkcja czekająca na dane (np. input() lub readline() z interaktywnego wejścia)
# dostaje koniec pliku zamiast danych – czyli dane skończyły się niespodziewanie.


#7.
ImportError
# Gdy import się nie udaje: moduł nie istnieje, nie da się go załadować


#8.
IndexError
# Gdy indeksujesz listę / krotkę / string poza zakresem:
# lista = [1, 2, 3]
# lista[5]          # IndexError


#9.
KeyError
# Gdy próbujesz odczytać z słownika klucz, którego nie ma:
# slownik = {"a": 1}
# slownik["b"]      # KeyError


#10.
KeyboardInterrupt
# Gdy użytkownik przerwie działanie programu, zwykle przez Ctrl+C w terminalu.


#11.
MemoryError
# Gdy Python nie może przydzielić więcej pamięci 
# (np. chcesz stworzyć gigantyczną listę) i system mówi „dość”.


#12.
NameError
# Gdy używasz zmiennej / nazwy, która nie została zdefiniowana:
# print(x)   # x nie istnieje → NameError


#13.
OSError
# Ogólny błąd systemu operacyjnego: problemy z plikami, katalogami, procesami, urządzeniami itp.
# Na przykład: próba operacji na pliku, gdy system zgłosi jakiś nietypowy błąd.


#14.
FileNotFoundError
# Gdy próbujesz otworzyć plik, który nie istnieje:
# open("nie_ma_takiego.txt")


#15.
PermissionError
# Gdy nie masz uprawnień do operacji na pliku / katalogu 
# (np. otwierasz tylko-do-odczytu do zapisu, brak praw dla użytkownika).


#16.
TimeoutError
# Gdy jakieś wywołanie systemowe lub operacja I/O jest ustawiona z limitem czasu i ten czas minie
# (np. socket z timeoutem).


#17.
TypeError
# Gdy typ argumentu jest zły albo operacja między typami nie ma sensu:
# "abc" + 5      # nie można dodać stringa i liczby
# len(10)        # len oczekuje obiektu z długością


#18.
ValueError
# Typ jest OK, ale wartość jest niepoprawna:
# int("abc")         # string jest, ale nie przedstawia liczby
# range(-1)          # zły argument dla range


#19.
RuntimeError
# Błąd „w czasie wykonania”, który nie pasuje do innych kategorii. 
# Np. niektóre błędy rekurencji czy nieprawidłowe użycie generatora.


#20.
SyntaxError
# Błąd składni – parser nie rozumie kodu:
# if x 5:
#     pass    # brak operatora porównania (>,<,==,!=) → SyntaxError


#21.
IndentationError
# Zła struktura wcięć – blok kodu nie jest poprawnie wcięty względem reszty 
# (np. za dużo albo za mało spacji).


#22.
TabError
# Szczególny przypadek błędów wcięć: mieszanie tabów i spacji w niekonsekwentny sposób we wcięciach.




# ĆWICZENIA
# 1. Napisz funkcję dzielenie i mnożenie przyjmującą dwie wartości a i b, 
# która wyświetli wynik działania a/b i a*b. 
# Co się wydarzy jeżeli nie zaimplementujemy obsługi wyjątków 
# i spróbujemy dzielić przez 0?

def dzielenie_i_mnozenie(a,b):
    try:
        a/b
    except Exception as e:
        print(e)
    else:
        print(f"Wynik dzielenia {a} / {b} = {a/b}")
    finally:
        print(f"Wynik mnożenia {a} * {b} = {a*b}\n")

dzielenie_i_mnozenie(5,2)
dzielenie_i_mnozenie(0,2)
dzielenie_i_mnozenie(5,0)

print(5/0)

# 2. Napisz funkcję dodawanie, która przyjmuje dwa argumenty a i b 
# oraz wyświetla ich sumę. 
# Co się wydarzy jeżeli jako argument podamy inta i stringa?





# ---------------------------------------------------------------------------------

# WŁASNE WYJĄTKI - RAISE
# „Tutaj coś jest nie tak → przerwij normalne działanie i zgłoś błąd”.

# raise Exception("komunikat")

# własne wyjątki:
# - za długa nazwa,
# - dane złych typów,

# Stwórzmy funkcję 'parzyste' która przyjmuje dwa argumenty i je do siebie dodaje
# jeżeli oba są parzyste. 
# Jeżeli chociaż jeden z argumentów jest nieparzysty funkcja
# powinna podnieść wyjątek.




# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------



# Zadanie
# Stwórz funkcję dzielącą zdanie na wyrazy. Prawidłowe zdanie powinno zaczynać
# się od wielkiej litery i kończyć kropką. W razie niespełnienia wymogów poprawnego
# zdania podniesiony powinien zostać wyjątek z informacją o wymaganej korekcie.

