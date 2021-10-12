def citire_lista():
    '''
    Functie folosita pentru citirea unei liste prin intermediul optiunii 1 .
    :return: Returneaza o lista de numere aleasa de programator .
    '''
    list = []
    n = int(input('Dati nr de elemente: '))
    for i in range(n):
        list.append(int(input('L[' + str(i) + '] =')))
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


def test_elemente_pare(list):
    assert elemente_pare([9, 81, 73]) == False
    assert elemente_pare([100, 58, 2, 10]) == True


def get_longest_all_even(list):
    '''
    Determin cea mai lunga subsecventa in care toate elementele sunt numere pare .
    :param list: Reprezinta lista de numere intregi .
    :return: Returneaza cea mai lunga subsecventa in care toate elementele sunt numere pare din list .
    '''
    test_elemente_pare(list)
    subsecventa_max = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            if ToateElemSuntPare(list[i:j + 1]) and len(subsecventa_max) < len(list[i:j + 1]):
                subsecventa_max = list[i:j + 1]
    return subsecventa_max


def test_get_longest_all_even():
    assert get_longest_all_even([5, 7]) == None
    assert get_longest_all_even([10, 20, 22]) == [10, 20, 22]
    assert get_longest_all_even([15, 12, 14, 55, 1000]) == [12, 14]


def medie_lista (list):
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


def get_longest_average_below (lst , average):
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
            if mediaElem(list[i:j + 1]) < average and len(subsecventa_max) < len(list[i:j + 1]):
                subsecventa_max = lst[i:j + 1]
    return subsecventa_max


def printMenu():
    print ('1. Citire date')
    print ('2. Determinare cea mai lungă subsecvență in care toate numerele sunt pare')
    print ('3. Determinare cea mai lungă subsecvență in care media a numerelor nu depășește o valoare citită')


def main():
    list = []
    while True:
        printMenu()
        optiune = input('Alegeti optiunea: ')
        if optiune == '1':
            list = citire_lista()

        elif optiune == '2':
            print(get_longest_all_even(list))


main()