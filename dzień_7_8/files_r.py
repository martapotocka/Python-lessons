# odczyt plikow tekstowych
# https://www.tutorialspoint.com/python/python_files_io.htm


# f = open("some_text.txt",'r') # otwarcie pliku do odczytu (read)
# print(f) # wydrukuje nam tylko dane o pliku
# f.close() # plik po otwarciu nalezy zamknac aby nie zajmowal miejsca w pamieci

# f = open("some_text.txt",'r')
# # print(f.readline()) # zwraca kolejna linijke i znak nowej linii \n
# # print(f.readlines()) # zwraca liste jeszcze nie przeczytanych linijek
# for line in f:
#     # print(line) # drukuje linijke i znak nowej linii \n
#     print(line[:-1]) # tak mozemy usunac znak nowej linii
# # lines_without_newline = f.read().splitlines()
# # print(lines_without_newline)
# f.close()

# ex70_reading_file.py

# konstrukcja with
# dzieki niej nie musimy pamietac o zamykaniu pliku

# with open("some_text.txt","r") as f:
#     for line in f.readlines():
#         print(line[:-1])
#     print(f.closed) # wewnatrz with plik jest wciaz otwarty
# print(f.closed) # poza with plik jest automatycznie zamkniety

# ex71_reading_file.py
