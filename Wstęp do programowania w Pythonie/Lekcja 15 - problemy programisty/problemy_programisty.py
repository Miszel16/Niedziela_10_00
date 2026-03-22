# KOD BINARNY = SYSTEM DWÓJKOWY

# 🔘 system dziesiętny:
# - 10 cyfr: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# 🔘 system dwójkowy:
# - w cyfr: 0, 1

# Jak przeliczyć z dziesiętnego na binarny?

# 19 (s. 10) -> 10011 (s. 2)

# dzielenie | reszta
# 19 : 2    | 1       (19/2 = 9)
# 9 : 2     | 1       ( 9/2 = 4)
# 4 : 2     | 0       ( 4/2 = 2)
# 2 : 2     | 0       ( 2/2 = 1)
# 1 : 2     | 1       ( 1/2 = 0)
# 0 : 2     | 0       ( 0/2 = 0)


#   1   0   0   1   1
#   2⁴  2³  2²  2¹  2⁰
#   16  8   4   2   1

# 1*2⁴ + 0*2³ + 0*2² + 1*2¹ + 1*2⁰ = 16 + 2 + 1 = 19


# PRZYKŁADY:
# - 56
# - 80
# - 15
# - 10101
# - 11011
# - 00000011





# odp
# 56₁₀ = 111000₂
# 80₁₀ = 1010000₂
# 15₁₀ = 1111₂
# 10101₂ = 21₁₀
# 11011₂ = 27₁₀
# 00000011₂ = 3₁₀



# Zadanie 1 (dziesiętnie -> binarnie)
# Napisz funkcję, która otrzyma jeden argument określający liczbę dziesiętną. Funkcja ma
# wyświetlić ile wynosi podana liczba w zapisie binarnym.

def binary_code(number: int) -> str:
    binary_number = ""

    while number > 0:
        result = number % 2
        result = str(result)
        binary_number = result + binary_number
        number = number // 2
    return binary_number

number = int(input("Podja numer: "))
print(binary_code(number))

# 111000

# Zadanie 2 (binarnie -> dziesiętnie)
# Napisz funkcję, która otrzyma jeden argument określający liczbę binarną. Funkcja ma
# wyświetlić ile wynosi podana liczba w zapisie dziesiętnym.

number = str(111000)

# i=0, elem=1  potega = 5 (a - 0 - 1)
# i=1, elem=1  potega = 4 (a - 1 - 1)
# i=2, elem=1  potega = 3 (6 - 2 - 1)
# i=3, elem=0  potega = 2 (6 - 3 - 1)
# i=4, elem=0  potega = 1 (6 - 4 - 1)
# i=5, elem=0  potega = 0 (6 - 5 - 1)

a = len(number) #6

def decimal_number(number: str) -> int:
    decimal_number = 0
    a = len(number)
    for i, elem in enumerate(number):
        decimal_number = decimal_number + 2**(a - i - 1) * int(elem)

    return decimal_number

number = input("Podja numer binarnie: ")
print(decimal_number(number))



    







#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# LICZBY PIERWSZE

# Liczba pierwsza to taka, która dzieli się przez '1' i przez samą siebie.

# liczba | dzielniki  (czy liczba pierwsza?)
#   1    |           
#   2    | 
#   3    | 
#   4    | 
#   5    | 
#   6    | 
#   7    | 
#   8    | 
#   9    | 
#   10   | 


# Zadanie 3
# Waszym zadaniem jest napisać funkcję, która zwróci informacje 'prawda/fałsz' czy
# podana liczba jest liczbą pierwszą.


# Zadanie 4
# Napisz drugą funkcję, która ma wyświetlić wszystkie liczby pierwsze z podanego
# przedziału (możesz wykorzystać do tego funkcję, którą już napisałeś)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PALINDROMY

# Palindrom to takie słowo, liczba lub zdanie, które czytane od przodu i od tyłu brzmi tak samo.

# PRZYKŁADY:

# kajak
# anna
# oko
# 1331
# 44
# 12321
# „Kobyła ma mały bok”
# „A to idiota”

# Podpowiedź i przypominajka:

# text[start:stop:step]

# start – od którego znaku zacząć (domyślnie od początku)
# stop – na którym znaku skończyć (domyślnie do końca)
# step – co ile znaków skakać (np. co 1, co 2... lub wstecz!)

# Jak są porównywane zmienne typu string?


# Zadanie 5
# Napisz funkcję, która jako argument otrzymuje tekst i sprawdzi czy jest on palindromem
# wyświetlając: „{podane słowo} jest palindromem” lub „{podane słowo} nie jest palindromem”
# *ZAAWANSOWANE* ulepszyć program, tak aby ignorował wielkość liter 
# (podpowiedź: Wykorzystajcie metodę toUpper lub toLower)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ANAGRAMY

# Anagram to nowe słowo (lub zdanie), które powstaje przez przestawienie liter innego słowa.
# Litery są te same, tylko ułożone w innej kolejności.

# PRZYKŁADY:

# kot → tok, okt
# lama → mala, alma
# roma → amor
# nos → son


# Zadanie 6
# Napisz funkcję, która sprawdzi czy dwa podane wyrazy są anagramami


