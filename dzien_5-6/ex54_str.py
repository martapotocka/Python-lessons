# stworz klase Car
# konstruktor klasy powinien pobierac trzy wybrane przez ciebie dane od uzytkownika
# i tworzyc trzy pola klasy
# a) stworz dwa rozne obiekty klasy Car i wydrukuj je uzywajac funkcji print
# b) w klasie Car dopisz metode __str__ i ponownie wydrukuj stworzone obiekty

class Car:

    def __init__(self, manufacturer, year, color):
        self.manufacturer = manufacturer
        self.year = year
        self.color = color

    def __str__(self):
        return f"Samochod marki {self.manufacturer}, rocznik {self.year} ma kolor {self.color}"

s = Car("Suzuki", 1990, 'zielony')
print(s)





# class Car:
#
#     def __init__(self, manufacturer, year, color):
#         self.manufacturer = manufacturer
#         self.year = year
#         self.color = color
#         print("Samochod zostal stworzony.")
#
#     def __str__(self):
#         return f"Samochod marki {self.manufacturer} z roku {self.year}, ma {self.color} kolor."
#
# car1 = Car("Suzuki", 1990, 'zielony')
# car2 = Car("Suzuki", 2015, 'srebrny')
#
# print(car1)
# print(car2)
