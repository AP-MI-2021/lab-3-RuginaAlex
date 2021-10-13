def citire_lista():
    '''
    Functie folosita pentru citirea unei liste prin intermediul optiunii 1 .
    :return: Returneaza o lista de numere aleasa de programator .
    '''
    list = []
    n = int(input('Dati nr de elemente: '))
    for i in range(n):
        list.append(int(input('L[' + str(i) + ']= ')))
    return list


def elemente_pare(list):
    '''
    Functia determina  daca o lista are toate elementele numere pare .
    :param list: Lista de numere intregi .
    :return: True, daca toate elementele din lista sunt numere  pare sau False, daca elementele sunt impare .
    '''
    for i in list:
        if i % 2 != 0:
            return False
    return True


def test_elemente_pare():
    assert elemente_pare([9, 81, 73]) == False
    assert elemente_pare([100, 58, 2, 10]) == True


def get_longest_all_even(list):
    '''
    Determin cea mai lunga subsecventa in care toate elementele sunt numere pare .
    :param list: Reprezinta lista de numere intregi .
    :return: Returneaza cea mai lunga subsecventa in care toate elementele sunt numere pare din list .
    '''
    test_elemente_pare()
    subsecventa_max = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if elemente_pare(list[i:j + 1]) and len(subsecventa_max) < len(list[i:j + 1]):
                subsecventa_max = list[i:j + 1]
    return subsecventa_max


def test_get_longest_all_even():
    assert get_longest_all_even([5, 7]) is None
    assert get_longest_all_even([10, 20, 22]) == [10, 20, 22]
    assert get_longest_all_even([15, 12, 14, 55, 1000]) == [12, 14]


def medie_lista(list):
    '''
    Functia calculeaza media a tuturor elementelor din lista .
    :param list: Lista de nr intregi .
    :return: Returneaza media aritmetica a elementelor dintr-o lista .
    '''
    medie_elemente = 0
    suma_elemente = 0
    for i in list:
        suma_elemente += i
    medie_elemente = suma_elemente / len(list)
    return medie_elemente


def test_medie_lista ():
    assert medie_lista([4,2,3]) == 3
    assert medie_lista([7,6,10,22]) == 11.25


def get_longest_average_below (list , average):
    '''
    Functia determina cea mai lunga subsecventa in care toate elementele au media mai mica decat o valoare citita .
    :param list: Lista de nr intregi .
    :param average: Valoare citita care va fi comparata cu media elementelor listei .
    :return: Cea mai lunga subsecventa in care toate elementele din lista au media mai mica decat o valoare citita .
    '''
    test_medie_lista()
    subsecventa_max = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if medie_lista(list[i:j + 1]) < average and len(subsecventa_max) < len(list[i:j + 1]):
                subsecventa_max = list[i:j + 1]
    return subsecventa_max


def test_get_longest_average_below ():
    assert get_longest_average_below([5,7,10,30],9) == [5,7,10]
    assert get_longest_average_below([50],10) is None


def divizibil_k (list,k):
    '''
    Functia determina daca o lista are toate elementele divizibile cu k .
    :param list: Lista de nr intregi .
    :param k: Numarul cu care verificam daca elementele din lista sunt divizibile .
    :return: Returneaza True daca toate elementele sunt divizibile cu k sau False daca acestea nu sunt divizibile cu k .
    '''
    for i in list:
        if i % k != 0:
            return False
    return True


def get_longest_div_k (list,k):
    '''
     Functia determina cea mai lunga subsecventa in care toate elementele sunt divizibile cu un numar k .
    :param list: Lista de nr intregi .
    :param k: Numarul cu care verificam daca elementele din lista sunt divizibile .
    :return: Cea mai lunga subsecventa in care toate elementele sunt divizibile cu un numar k citit .
    '''
    subsecventa_max = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if divizibil_k(list[i:j + 1], k) is True and len(subsecventa_max) < len(list[i:j + 1]):
                subsecventa_max = list[i:j + 1]
    return subsecventa_max


def test_get_longest_div_k ():
    assert get_longest_div_k([10,20,30],10) == [10,20,30]
    assert get_longest_div_k([7,13,10],3) is None


def printMenu():
    print ('1. Citire date')
    print ('2. Determinare cea mai lungă subsecvență in care toate numerele sunt pare')
    print ('3. Determinare cea mai lungă subsecvență in care media a numerelor nu depășește o valoare citită')
    print ('4. Determinare cea mai lungă subsecvență in care toate numerele sunt divizibile cu un numar citit')
    print ('5. Iesire')

def main():
    list = []
    while True:
        printMenu()
        optiune = input('Alegeti optiunea: ')
        if optiune == '1':
            list = citire_lista()

        elif optiune == '2':
            print(get_longest_all_even(list))

        elif optiune == '3':
            average=int(input('Dati valoarea pentru a compara media: '))
            print(get_longest_average_below((list), average))

        elif optiune == '4':
            k = int(input("Valoarea cu care verificati daca numerele sunt divizibile: "))
            print(get_longest_div_k((list), k))

        elif optiune == '5':
            break
        else:
            print("Optiune gresita! Reincercati!")

main()