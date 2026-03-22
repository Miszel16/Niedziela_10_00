import re

print("Funkcja re.match()")
# re.match(pattern, string, flags=0)

# szuka wzorca od początku teksu
# zwraca obiekt typu Match/None

zdanie = "Ala ma kota"

# -- match/none ---
wynik1 = re.match(r"Ala", zdanie)
print(wynik1) # Match

wynik2 = re.match(r"kota", zdanie)
print(wynik2) # None



# -- informacje ---
print(f"Znaleziono: {wynik1.group()}")
print(f"Początek dopasowania pod indeksem: {wynik1.start()}")
print(f"Koniec dopasowania pod indeksem: {wynik1.end()}")
print(f"Krotka przedziału: {wynik1.span()}")


# -- flaga --
wynik3 = re.match(r"ala", zdanie)
print(wynik3) # None

wynik4 = re.match(r"ala", zdanie, re.IGNORECASE)
print(wynik4)



#-----------------------------------------------------------
print("Fucnkja re.search()\n\n\n\n")
# re.search(pattern, string, flags=0)

# sprawdza czy wzorzec wystepuje gdziekolwiek w tekscie (do pierwszego wystąpienia)
# zwraca obiekt Match/None

zdanie = "Antonio ma 123 jabłka 123."
wynik = re.search(r"\d+", zdanie)
print(wynik)



#-----------------------------------------------------------
print("Funkcja re.findall()\n\n\n\n")
# re.findall(pattern, string, flags=0)

# przeszukujemy cały string (wszytskie wystąpienia)
# Zwraca liste

zdanie = "Mateusz i Kacper jadą na wycieCzkę do Dubaju."

wynik = re.findall(r"\b[A-Z][a-z]+", zdanie)
print(wynik)


#-----------------------------------------------------------
print("Funkcja re.sub()\n\n\n\n")
# re.sub(pattern, repl, string, count=0, flags=0)

# repl - ciąg znaków lub funkcja, którą zastąpimy znalezione
# dopasowania. ( "Piotrek" , \1)
# 
# count(opcjonalny) -maksymalna liczba zmian
# domyślnie jest 0: zmienia wszytskie

text = "Valorant to najlepsza gra."
print(text)
pattern = "Valorant"
replacement = "TFT"

new_text = re.sub(pattern, replacement, text)
print(new_text)

print("\n\n\n\n\n\n\n\n\n\n\n")
#----------------------------------------------------------------------------
# ĆWICZENIA 
#----------------------------------------------------------------------------

#1 Sprawdz czy w tekscie "Uczę się programowania w języku python3" występuje cyfra
sentence = "Uczę się programowania w języku python3"

wynik = re.search(r"\d", sentence)

if wynik is not None:
    print(f"W zdaniu {sentence} występuje cyfra.")
else:
    print(f"W zdaniu {sentence} nie występuje cyfra.")




#2 Znajdź wszystkie daty w zdaniu 
# "Juliusz Słowacki herbu Leliwa (ur. 4 września 1809 w Krzemieńcu, zm. 3 kwietnia 1849 w Paryżu[1])
# – polski poeta, dramaturg i epistolograf. Obok Adama Mickiewicza i Zygmunta Krasińskiego określany 
# jako jeden z polskich wieszczów narodowych. Twórca filozofii genezyjskiej (pneumatycznej), 
# epizodycznie związany z mesjanizmem polskim, był też mistykiem. 
# Obok Adama Mickiewicza uznawany powszechnie za największego przedstawiciela polskiego romantyzmu."
sentence = "Juliusz Słowacki herbu Leliwa (ur. 4 września 1809 w Krzemieńcu, zm. 3 kwietnia 1849 w Paryżu[1]) " \
"– polski poeta, dramaturg i epistolograf. Obok Adama Mickiewicza i Zygmunta Krasińskiego określany " \
"jako jeden z polskich wieszczów narodowych. Twórca filozofii genezyjskiej (pneumatycznej), " \
"epizodycznie związany z mesjanizmem polskim, był też mistykiem. Obok Adama Mickiewicza uznawany " \
"powszechnie za największego przedstawiciela polskiego romantyzmu."

pattern = r"\d+\s\w+\s\d{4}"
wynik = re.findall(pattern, sentence)
print(wynik)



#3 Zamień wszystkie lata z tekstu wyżej na rok 2137.
pattern = r"\d{4}"
wynik = re.sub(pattern, "2137", sentence)
print(wynik)




#4 Znajdź wszystkie daty w formacie  DD-MM-YYYY z tekstu "Dzisiaj jest 20-10-2024, a jutro będzie 21-10-2024."
sentence = "Dzisiaj jest 20-10-2024, a jutro będzie 21-10-2024."



#5 Znajdź liczby nieparzyste spośród podanych
sentence = "Podane liczby to 5 12 442 321 45 20 77"



#6 Znajdź wszystkie wyrazy zawierające przynajmniej 3 samogłoski
sentence = "start script level loop debug player server tournament map speedrun quest socket"



#7 Znajdź wszystkie słowa zaczynające się na literę 's' i kończące na literę 't'
sentence = "start script level loop debug player server tournament map speedrun quest socket"


#----------------------------------------------------------------------------
# ZADANIA
#----------------------------------------------------------------------------
# https://drive.google.com/file/d/1ILqEGuZJPfuM3kdrfWs1BijGP3rfH3Im/view?usp=sharing

with open("dane.txt", "r", encoding='utf-8') as file:
    data = file.read()
#print(data)

#1. Znajdź wszystkie adresy email


#2. Znajdź wszystkie osoby zaproszone na spotkania (Imie + Nazwisko)


#3. Znajdź wszystkie numery telefonów


#4. Zamień wszystkie numery telefonów na xxx - xxx - xxx


#5. Znajdź pierwszą datę 


#6. Znajdź wszystkie godziny o których rozpoczynają się spotkania


#7. Sprawdź ile spotkań zostało zaplanowanych
