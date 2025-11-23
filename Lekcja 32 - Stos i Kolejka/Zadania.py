# 1. Utwórz symulator przeglądarki gdzie historia przeglądania 
# będzie zapisywana w formie stosu. Użytkownik może wchodzić 
# na różne strony w programie i cofać się w historii przeglądania.

# - historia stron
# - dodanie strony do historii (przejście na jakąś stronę)
# - COFNIJ (przejście do strony poprzedniej)

from Stos_i_Kolejka import Stack, Queue

class BrowserHistory():
    def __init__(self):
        self.history = Stack()
        self.current_page = None
    
    def visit(self, strona):
        self.history.push(self.current_page)
        self.current_page = strona
    
    def back(self):
        previous_page = self.history.pop()
        if previous_page is not None:
            self.current_page = previous_page
    
    def print_history(self):
        print(f"Current page:  {self.current_page}")
        print(f"History: ")
        

print("\n")
Historia = BrowserHistory()
Historia.visit("Giagnci programowania")
Historia.visit("Roblox")
Historia.visit("Tiktok")


print("\n")
Historia.print_history()
Historia.back()
print("\n")
Historia.print_history()
Historia.back()
print("\n")
Historia.print_history()
Historia.back()













# ---------------------------------------------------------------------
# 2. Utwórz symulator kolejki do kasy kina gdzie elementami kolejki
# są klienci razem z ich zamówieniem. Do utworzenia symulatora kolejki
# użyj naszej struktury Kolejki, którą stworzyliśmy wcześniej.

# - czy są jeszcze jacyś klienci? (czy pusta)
# - dodaj klienta do kolejki
# - usuń klienta z kolejki
# - kto następny? (zwraca zamówienie klienta, który jest pierwszy w kolejce)










# ----------------------------DODATKOWE--------------------------------
# Napisz funkcję, która sprawdzi, czy dany ciąg znaków jest palindromem,
# korzystając z naszej implementacji stosu.

# palindrom - np. kajak, ala
# od przodu i od tyłu ten sam wyraz

# * wizualizacja w paintcie









# ---------------------------------------------------------------------
# PODSUMOWANIE
# ● Nauczyliśmy się implementować stos oraz kolejkę w Pythonie przy użyciu listy lub klas.
# ● Stos jest strukturą LIFO, a kolejka FIFO.
# ● Implementowaliśmy metody push, pop i peek.

# Pytania powtórzeniowe:
# ● Jakie są cechy stosu?
# ● Jakie są cechy kolejki?
# ● Jakie metody stosu/kolejki poznaliśmy i do czego służą?   