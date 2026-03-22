# 1) Super Zgadywanka „Do trzech razy sztuka”
# (biblioteka: random, pętle, warunki)

# a. Zaimportuj bibliotekę random.
# b. Wylosuj liczbę całkowitą z zakresu 1–20 i zapisz do zmiennej tajna.
# c. Ustaw licznik prób proby = 3.
# d. Uruchom pętlę, która działa dopóki są próby:
#      - Poproś użytkownika w konsoli o liczbę.
#      - Jeśli liczba jest mniejsza niż tajna, wypisz Za mało.
#      - Jeśli większa, wypisz Za dużo.
#      - Jeśli równa, wypisz Brawo, zgadłeś! i przerwij pętlę.
#      - Po każdym błędzie zmniejsz proby o 1 i wypisz, ile prób zostało.
# e. Gdy próby się skończą, a użytkownik nie trafił, wypisz: Koniec gry. Tajna liczba to: <tajna>.




# 2) Odliczanie Startu „Mała Rakieta”
# (biblioteka: time, pętle, warunki)

# a. Zaimportuj time.
# b. Poproś użytkownika w konsoli o liczbę startową (np. 5).
# c. W pętli wypisuj kolejne liczby w dół do zera.
# d. Pomiędzy kolejnymi liczbami wstaw time.sleep(1).
# e. Po dojściu do zera wypisz START!.





# 3) Kalendarz Urodzin — „Ile to już dni?”
# (biblioteka: datetime/date, operacje na datach, funkcje)

# a. Zaimportuj z datetime klasę date.
# b. Poproś użytkownika w konsoli o podanie daty urodzenia w trzech krokach: rok, miesiąc, dzień (jako liczby).
# c. Utwórz obiekt urodziny = date(rok, miesiac, dzien).
# d. Pobierz dzisiejszą datę: dzis = date.today().
# e. Oblicz różnicę dni: dni = (dzis - urodziny).days.
# f. Wypisz w konsoli: Od urodzin minęło <dni> dni.
# g. (Dla chętnych) Napisz funkcję ile_lat_miesiecy_dni(od, do),
#     która zwraca przybliżenie w latach i miesiącach
#     (np. lat = dni//365, mies = (dni%365)//30) i wypisz ładne podsumowanie.




# 4) „Dziennik Nastroju” 
# (biblioteki: datetime/date, zapis do pliku, pętle)

# a. Zaimportuj z datetime klasę date.
# b. Otwórz plik nastroje.txt w trybie dopisywania ('a') z kodowaniem utf-8.
# c. Pobierz dzisiejszą datę: dzis = date.today().
# d. W pętli:
#       - Poproś użytkownika w konsoli: Jaki dziś masz nastrój? (wpisz 'koniec' aby zakończyć)
#       - Jeśli wpisze koniec, przerwij pętlę.
#       - W przeciwnym razie dopisz do pliku linię: RRRR-MM-DD – <nastrój> i wypisz w konsoli Zapisano.
# e. Po zakończeniu pętli zamknij plik i wypisz Do zobaczenia jutro!.




# 5) Asystent Trójkątów „Matematyczny Pomocnik”
# (biblioteka: math, warunki, funkcje)

# a. Zaimportuj math.
# b. Napisz funkcję wczytaj_bok(nazwa),
#    która pyta w konsoli o dodatnią długość boku i zwraca tę liczbę (wymuś > 0 w pętli).
# c. Wczytaj trzy boki: a, b, c.
# d. Sprawdź warunek istnienia trójkąta (suma dwóch krótszych > najdłuższy).
#    Jeśli warunek nie jest spełniony, wypisz 'Z tych boków trójkąt nie istnieje' i zakończ program.
# e. Oblicz i wypisz:
#       - Najkrótszy i najdłuższy bok.
#       - Rodzaj trójkąta wg boków: równoboczny, równoramienny, różnoboczny.
#       - Obwód (suma boków).
# f. Wypisz rodzaj wg kątów, porównując a^2 + b^2 do c^2 (dla bezpieczeństwa najpierw ustaw c jako najdłuższy).
#       == → prostokątny, < → rozwartokątny, > → ostrokątny.
# g. (Dla chętnych) Policz pole z wzoru Herona:
#       p = (a+b+c)/2,
#       pole = math.sqrt(p*(p-a)*(p-b)*(p-c)),
#       Wypisz Pole = <pole>.



# 6) „Szkolny Sklepik” 
# (biblioteki: zapis do pliku, opcjonalnie datetime do daty, pętle, funkcje)

# a. Utwórz funkcję wczytaj_cene(nazwa), która:
#       - pyta w konsoli o cenę dodatnią (float),
#       - zwraca ją.
# b. Utwórz funkcję wczytaj_ilosc(nazwa), która:
#       - pyta w konsoli o ilość dodatnią (int),
#       - zwraca ją.
# c. Zapytaj użytkownika w konsoli o trzy produkty, które kupił kolega (np. „kanapka”, „sok”, „jabłko”).
#       - Dla każdego produktu pobierz cenę i ilość.
# d. Policz łączny koszt każdego produktu (cena * ilość).
# e. Dodaj wszystkie koszty i oblicz SUMĘ do zapłaty.
# f. Otwórz plik paragon.txt w trybie zapisu ('w', kodowanie 'utf-8').
#       - Wypisz do pliku ładną listę zakupów




# 7) „Dwustopniowe wejście” — mini-logowanie
# (warunki, pętle; opcjonalnie getpass dla chętnych)

# a. Ustal stałe: PIN = "1234" i HASLO = "maslo".
# b. W pętli najpierw poproś o PIN.
#       - Jeśli jest zły, wypisz Zły PIN i wróć do początku pętli.
#       - Jeśli dobry, poproś o hasło.
# c. Jeśli hasło jest poprawne, wypisz 'Zalogowano pomyślnie' i przerwij pętlę.
# d. (Dla chętnych) Zamiast zwykłego input dla hasła użyj getpass.getpass() 
#    — wymaga import getpass i działa w konsoli.



# 8) „Mnożymy wiedzę”
# (biblioteki: random, zapis do pliku; pętle, warunki)

# a. Zaimportuj random.
# b. Poproś użytkownika w konsoli o liczbę pytań n (np. 5).
# c. W pętli n razy:
#       - Wylosuj dwie liczby 2–9.
#       - Zadaj pytanie w konsoli: Ile to jest <a> * <b>?
#       - Jeśli odpowiedź dobra, wypisz 'Dobrze!'
#       - jeśli zła, wypisz 'Nie, poprawny wynik to <a*b>'.
#       - Zliczaj poprawne odpowiedzi.
# d. Po zakończeniu wypisz wynik w stylu Wynik: X/Y.
# e. Dopisz tę linię do pliku mnozenie_wyniki.txt (np. 2025-08-14 – 4/5).