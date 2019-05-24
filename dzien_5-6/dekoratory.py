def add_stars(fun):   # tu tworzymy dekorator, ktory pobiera funkcje
    def inner():      # w jego ciele tworzymy nowa funkcje
        print("***")  # ktora dodaje jakies funkcjonalnosci i dodaje je do pobranej funkcji
        fun()         # w funkcji wewnetrznej musi znajdowac sie pobrana funkcja
        print("***")
    return inner      # a nastepnie ja zwraca

@add_stars #-> znajdz dekorator o takiej nazwie i przekaz do niego ponizsza funcje
def basic_function():  # oraz ja nadpisz
    print("I'm basic")

basic_function()

#ex68.py

# uzycie zapisu @add stars jest rownowazne z: basic_function = add_stars(basic_function)
