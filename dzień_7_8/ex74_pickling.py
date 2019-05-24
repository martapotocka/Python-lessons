stworz klase SloikOgorkow pobierajaca w konstruktorze dane:
firma, pojemnosc, typ, data waznosci
stworz obiekt klasy SloikOgorkow a nastepnie przy uzyciu pickling zapisz go do pliku
ogorek.dat
nastepnie odczytaj obiekt ogorka z pliku i wypisz jego dane
(te same, ktore podales w konstruktorze)










# import pickle
#
# class SloikOgorkow:
#
#     def __init__(self, firma, pojemnosc, typ, cena):
#         self.firma = firma
#         self.pojemnosc = pojemnosc
#         self.typ = typ
#         self.cena = cena
#
# sloik1 = SloikOgorkow("Rolnik", "800ml", "kiszone", 10)
#
# with open("ogorek.dat", "wb") as f1:
#     pickle.dump(sloik1, f1)
#
# with open("ogorek.dat", "rb") as f2:
#     ogorek = pickle.load(f2)
#
# print(ogorek.firma, ogorek.pojemnosc, ogorek.typ, ogorek.cena)
