stworz plik zawierajacy w kolejnych linijkach dane:
Marian 25
Zenobiusz 31
Kunegunda 17
nazwij go wiek.txt
przeczytaj plik uzywajac konstrukcji with - as
wpisz dane do slownika (wymysl co ma byc kluczem a co wartoscia)
wypisz na ekran osoby i ich wiek w kolejnosci, od najmlodszej do najstarszej






# with open("wiek.txt", "r") as f:
#     age_name_dict = dict()
#     for line in f.readlines():
#         splitted = line.split()
#         age_name_dict[splitted[1]] = splitted[0]
#     for key in sorted(age_name_dict.keys()):
#         print(age_name_dict[key], key)
