a = set() # deklaracja pustego setu

a.add(5)
a.add(4)
a.add(3)
a.add(3) # set przechowuje po jednym egzemplarzu kazdej wartosci
a.remove(3) # usun element ze zbioru
print(a)
print(len(a)) # wydrukuj informacje o rozmiarze zbioru
print(5 in a) # sprawdz czy element jest w secie
print(10 not in a) # sprawdz czy elementu nie ma w secie

D = [1,1,2,3,4,5,32,3,6,1]
d = set(D)
