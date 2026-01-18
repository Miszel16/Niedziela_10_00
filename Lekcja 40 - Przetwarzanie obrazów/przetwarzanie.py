# Wybranie obrazka z folderu grafiki
# https://drive.google.com/drive/folders/1_F2ncQA8--C-jghM7BjmsrUx1hTjucSL?usp=sharing
# - pobrać i zapisać do folderu projektu pod nazwą 'image.jpg'

import cv2
from PIL import Image
import numpy as np

# 1. Wczytanie grafiki z pliku i wyświetlenie obrazu

# a) funkcja do wyświetlania obrazu (opencv)
def show_image(img):
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# b) funkcja, która wczyta obraz z pliku i do wyświetli (opencv)
def read_image_cv(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print(img)
    print(img.shape)
    print(type(img))
    show_image(img)
    return img

image = read_image_cv("image.jpg")


# c) funkcja, ktora wczyta obraz z pliku i go wyświetli (pillow)

# def read_image_PIL(path):
#     im = Image.open(path)
#     try:
#         print(im)
#     except:
#         print(type(im))
#     im.show()
#     return im

# read_image_PIL("image.jpg")


# 2. Flip obrazka (odbicie) [do góry nogami]

# a) algorytm
def reverse_image(img):
    img_reverse = img[::-1]
    return img_reverse

# show_image(reverse_image(image))

# b) opencv-python
# show_image(cv2.flip(image,0))


# 3. Zmiana koloru na skalę szarości
# (175, 288, 3)
# RGB [0,0,0]

# a) algorytm
def gray_scale(img):
    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            gray = int(sum(img[row][column])/3)
            img[row][column][0] = gray
            img[row][column][1] = gray
            img[row][column][2] = gray
    return np.array(img)

show_image(gray_scale(image))





















# 5. Zadanie samodzielne - change_colors
# Napisz funkcję change_colors, która przyjmuje 4 argumenty:

# ● img -obraz w formacie np.array,
# ● R_scale - współczynnik zmiany koloru czerwonego piksela,
# ● G_scale - współczynnik zmiany koloru zielonego piksela,
# ● B_scale - współczynnik zmiany koloru niebieskiego piksela.

# Funkcja powinna dla każdego piksela ustalać nową wartość koloru jako stara wartość
# razy współczynnik dla odpowiedniej barwy oraz zwrócić przefiltrowany obraz.
# Przetestuj funkcję wpisując różne współczynniki jako parametry, co dzieje się z
# obrazem? Jak myślicie funkcja generuje nowy obraz czy modyfikuje stary?

