# NIESTANDARDOWE STRUKTURY 

# 1. STOS
# - elementy w określonej kolejności
# - LIFO (Last In First Out)
# - np. historia przeglądania

# *(można zrobić za pomocą listy)

stack = []

stack.append("A") # dodajemy na koniec
stack.append("B")
stack.append("C")

print(f"Stos po dodaniu elementów: {stack}")

element_top = stack.pop() # zdejmujemy ostatni element

print(f"Stos po zdjęciu elementu: {stack}") # A B


# 1.1. wizualizacja w paintcie

# 1.2. uwtorzenie własnej wersji struktury
# - dodawanie na stos +
# - zdejmowanie ze stosu +
# - co jest na wierzchu? +
# - czy stos jest pusty? +
# - ile rzeczy na stosie (rozmiar)? +

class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop() # domyślnie usuwa ostatni element

    def show_top(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0 # True/False
        # if len(self.stack) == 0:
        #     return True
        # else:
        #     return False

    def show_size(self):
        return len(self.stack)


print("\n")

stos = Stack()
stos.push(1)
stos.push(2)
stos.push(3)

print(stos.pop()) # 3

print(stos.show_top()) # 2

print(stos.is_empty()) # False (1, 2)

print(stos.show_size()) # 2

# ---------------------------------------------------------------------
# 2. KOLEJKA
# - elementy w koleności dodania
# - FIFO (First In First Out)
# - np. kolejka w sklepie

# 2.1. wizualizacja w paintcie

# 2.2. uwtorzenie własnej wersji struktury
# - dodawanie na koniec +
# - usuwanie z początku +
# - co jest na początku? +
# - czy kolejka jest pusty? +
# - ile rzeczy jest w kolejce (rozmiar)?


#  1   2   3   4   5
# -4  -3  -2  -1

class Queue():
    def __init__(self):
        self.queue = []
    
    def add(self, item):
        self.queue.append(item)
    
    def delete(self):
        if not self.is_empty():
            return self.queue.pop(0) # usuwamy pierwszy z kolejki
    
    def show_first(self):
        if not self.is_empty():
            return self.queue[0]
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def show_size(self):
        return len(self.queue)
    
print("\n")

kolejka = Queue()

kolejka.add("A")
kolejka.add("B")
kolejka.add("C")

print(kolejka.delete()) # A
print(kolejka.show_first()) # B
print(kolejka.is_empty()) # False (B, C)
print(kolejka.show_size()) # 2