def add(a,b): # 2 i 4
    return a+b

# ctrl+s

# Zadanie 1. Palindrom 
# Napisz funkcję sprawdzającą czy dane słowo jest palindromem (palindrom to 
# słowo które pisane od przodu i od tyłu jest identyczne). 
# Napisz testy, które sprawdzą, czy słowa “kamilslimak” i “ala” są palindromami, a 
# słowa “wiadro” i “kamyk” nimi nie są. 

def palindrom(slowo):
    return slowo == slowo[::-1]



# Zadanie 2. Boki trójkąta 
# Napisz program, który sprawdzi, czy można utworzyć trójkąt z boków o podanej 
# długości. Aby utworzyć trójkąt, suma dwóch krótszych boków musi być dłuższa 
# niż najdłuższy bok. 
# Należy przetestować sytuację, w której zachodzi prawidłowy stosunek między bokami (2,3,4) 
# sytuację, w której najdłuższy bok jest dłuższy od sumy dwóch pozostałych boków (1,1,2) i 
# sytuację w której jeden z boków ma długość niedodatnią (0,-1,1)

def if_valid_trojkat(a,b,c):
    if min(a,b,c) <= 0:
        return False
    najdluzszy = max(a,b,c)
    suma = a+b+c - najdluzszy # suma dwóch mnijeszych boków
    if suma <= najdluzszy:
        return False
    else:
        return True
