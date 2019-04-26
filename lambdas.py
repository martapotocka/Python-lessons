# lambdy nazywane sa tez funkcjami anonimowymi, poniewaz nie posiadaja nazwy
# do zdefiniowania lambdy uzywamy slowa kluczowego 'lambda'
# lambda argument:expression

# square_x = lambda x:x**2  # niezalecane, lepiej uzyc def i zrobic normalna funkcje
#
# lambda x:x**2 # taki zapis absolutnie nic nie robi
#
# def square_x(x):
#     return x**2
#
# print(square_x(5))

# uzycie lambd:

# list comprehension

# D = [(lambda x: x*x)(x) for x in range(10)] # ???!!!
# R = [x**2 for x in range(10)]
#
# print(D)
# print(R)

# filter()
# funkcja filter() pobiera dwa argumenty: funkcje oraz liste
# dla elementu listy sprawdza czy funkcja dla tego elementu zwroci True
# jesli tak to przepuszcza ten element przez filtr

# def check_if_divisor_of_3(num):
#     return num%3 == 0
#
# N = list(filter(lambda num : num%3 == 0, range(15)))
# N = list(filter(check_if_divisor_of_3, range(15))) # alternatywa dla lambdy
# print(N)

# ex31

# map()
# funkcja map() pobiera dwa argumenty: funkcje oraz liste (lub string)
# stosuje funkcje na kazdym elemencie listy

N = list(map(lambda num : num/2, range(20)))
N = list(map(lambda num : num/2, [1,2,3,4,5,6,7,8,9,0]))
print(N)

# ex32
