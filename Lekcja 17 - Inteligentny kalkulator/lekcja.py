# ETAP 1
# - baza danych
# - pobieranie tekst (pięc dodać siedem)
# - przetłumaczyć na znaki
# - wypisz przetłumaczone dzialanie "5+7"
# - tłumaczenie działania z tekstu na liczby 5 '+' 7
# - obliczyć wynik

# 0, 1 ... 20
# -, *
zero = ["0", "zero", "zera", "zerem"]
jeden = ["1", "jeden", "jedynka", "jedynkę"]
plus = ["+", "plus", "dodać", "dodaj"]

baza = [zero, jeden, plus]

# nazwa_listy[0]


def przetlumacz(slowo): #slowo = "jeden" , "1"
    for baza_symbolu in baza: # baza_symbolu = zero
        for slowo_bazy_symbolu in baza_symbolu:
            if slowo_bazy_symbolu == slowo:
                return baza_symbolu[0]
    return ''


# +, -, *, /(nie można dzielić przez 0)
def oblicz(liczba1, liczba2, znak): # 0, 1, "+"
    if znak == '+':
        return liczba1 + liczba2
    elif znak == "-":
        return liczba1 - liczba2
    elif znak == "*":
        return liczba1 * liczba2
    elif znak == "/":
        if liczba2 != 0:
            return liczba1 / liczba2
        else:
            return "Nie można dzielić przez zero"



def oblicz_z_tekstu(dzialanie_tekst): # " +1000"
    liczba1 = "" #1
    liczba2 = "" #0
    znak = "" #+

    for i in dzialanie_tekst: # i=+
        if i.isdigit(): 
            if znak == '':
                liczba1 += i
            else:
                liczba2 += i
        else:
            znak = i
    
    #liczba1 = "111"
    #liczba2 = "1000"
    #znak = "+"

    if liczba1 == "" or liczba2 == "" or znak == "":
        return "Nie rozumiem działania - sprawdź słowa."


    liczba1 = int(liczba1)
    liczba2 = int(liczba2)

    #liczba1 = 111
    #liczba2 = 1000
    #znak = "+"

    return oblicz(liczba1, liczba2, znak)



tekst = input("Podaj tekst: ").lower()
dzialanie = ""

for slowo in tekst.split(" "):
    slowo_przetlumaczone = przetlumacz(slowo)
    dzialanie += slowo_przetlumaczone

print(dzialanie)
print(oblicz_z_tekstu(dzialanie))

# testy: jeden jeden jeden plus jeden zero zero
#
