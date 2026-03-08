# Dalsza część edukacji - nowy poziom
# https://www.canva.com/design/DAG7B-f2aQA/LXh-Sj_L600SWK_Zlo40Hg/view

# QUIZ
# https://quiz.giganciprogramowania.edu.pl/wdp-python-q8

# Wizja komputerowa (biblioteki, modele)
# Wyrażenia regularne (biblioteka, funkcje)
# API (postawowe operacje, protokół, biblioteka, refaktoryzacja, kody odpowiedzi)
# Web Scraping (biblioteka)

# VENV
# Zagadnienie 1 - Generowanie ciągu znaków
# Napisz program, który z ciągu w formacie: napis, liczba wygeneruje ciąg
# znaków. W wygenerowanym ciągu każdy napis powinien zostać powtórzony tyle
# razy ile wskazuje liczba go poprzedzająca.

#                        kot3ala3c11 -> kotkotkotalaalaalaccccccccccc

# Załóż, że dane zawsze zostaną dostarczone w
# prawidłowym formacie.

import re

def create_string(code: str):
    letter = re.findall(r'[^0-9]+', code)
    numbers = re.findall(r'\d+', code)
    print(f"Letters: {letter}")
    print(f"Numbers: {numbers}")

    wynik =""

    for l, n in zip(letter, numbers):
        wynik += l*int(n)
    print(wynik)

code = input("Podaj ciag: ")
create_string(code)

