# stworz wlasny wyjatek: ZbytDlugaLista
# stworz funkcje ktora pobiera kolejne elementy listy, mnozy je przez 2 i dodaje do siebie
# funkcja ma dzialac tylko na listach nie dluzszych niz 5
# jesli lista jest dluzsza niz 5 rzuc wyjatkiem ZbytDlugaLista
# uruchom funkcje w bloku try/except/finally i podaj userowi odpowiednie komunikaty

class ZbytDlugaLista(Exception):
    pass

def sum_doubled_list(my_list):
    if len(my_list) > 5:
        raise ZbytDlugaLista()
    my_sum = 0
    for element in my_list:
        if type(element) is not int:
            raise TypeError("Lista miala zawierac inty!")
        my_sum += element * 2
    return my_sum

try:
    sum_doubled_list([1,2,3,4,'a'])
except ZbytDlugaLista:
    print("Sorry lista byla zbyt dluga")
except TypeError:
    print("W liscie znaleziono element, ktory nie byl intem!")
finally:
    print("Konczymy, wychodzimy.")
