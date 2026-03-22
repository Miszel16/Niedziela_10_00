import funkcje
import pytest

# - funkcje muszą nazywać się od 'test' - automatyczne wykrywanie
def test_add():
    assert funkcje.add(2,4) == 6
    assert not funkcje.add(1,2) == 4


# kamilslimak, ala, wiadro, kamyk
def test_palindrom():
    assert funkcje.palindrom("kamilslimak") == True
    assert funkcje.palindrom("ala")

    assert funkcje.palindrom("wiadro") == False
    assert not funkcje.palindrom("kamyk")

# python -m <nazwa modułu> <nazwa pliku>
# python -m pytest test_with_pytest.py -v