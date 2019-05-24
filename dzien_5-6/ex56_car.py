# stworz klase Car, ktora w konstruktorze bedize pobierac nastepujace parametry:
# - nazwe
# - pojemnosc baku
# - spalanie na 100km wyrazone jako int np "5" oznacza 5/100km
# - wstepna ilosc benzyny w baku (max tyle ile wynosi pojemnosc)

# stworz metody:
# - zatankuj - ktora dodaje do baku podana ilosc benzyny (nie wiecej niz max)
# - jedz - ktora pobiera dystans do przejechania i informuje o tym czy przejechalismy go,
#   czy skonczyla sie benzyna. Modyfikuje zawartosc baku o ilosc spalonej benzyny.
# - __str__ - wypisz dane samochodu (nazwe, pojemnosc, aktualna ilosc benzyny w baku)

class Car:

    def __init__(self, name, tank_cap, gas_per_100km, current_gas):
        self.name = name
        self.tank_cap = tank_cap
        self.gas_per_100km = gas_per_100km
        self.current_gas = current_gas
        self.check_gas_level()

    def check_gas_level(self):
        if self.current_gas > self.tank_cap: # jesli dolano za duzo paliwa
            self.current_gas = self.tank_cap # ustaw current_gas na maksymalna pojemnosc baku

    def __str__(self):
        return f"Car: {self.name}, tank_cap: {self.tank_cap}, gas_per_100: \
{self.gas_per_100km}, current_gas: {self.current_gas}"

    def add_fuel(self, gasoline):
        if self.current_gas + gasoline > self.tank_cap:
            self.current_gas = self.tank_cap
        else:
            self.current_gas += gasoline
        print(f"Dolano {gasoline}l benzyny. W baku jest {self.current_gas}l benzyny.")

    def drive(self, distance):
        print(f"Chcemy przejechac {distance} km.")
        required_fuel = distance/100 * self.gas_per_100km
        if required_fuel <= self.current_gas:
            self.current_gas -= required_fuel
            print(f"Przejechano {distance}. W baku zostalo {self.current_gas} litrow.")
        else:
            distance_covered = self.current_gas/self.gas_per_100km * 100
            self.current_gas = 0
            print(f"Przejechano {distance_covered} i paliwo sie skonczylo.")




c1 = Car("Ford", 60, 5, 30)
print(c1)
c1.add_fuel(10)
c1.add_fuel(100)
c1.drive(1000)
c1.drive(300)
c1.add_fuel(40)
c1.drive(100)





# class Car:
#
#     def __init__(self, name, tank, gas_per_100km, current_gas):
#         self.name = name
#         self.tank = tank
#         self.gas_per_100km = gas_per_100km
#         self.current_gas = current_gas
#         print(f"Stworzono samochod {self.name}, pali {self.gas_per_100km} na setke.")
#
#     def add_gasoline(self, liters):
#         if self.current_gas + liters <= self.tank:
#             self.current_gas += liters
#         else:
#             self.current_gas = self.tank
#         print(f"Dolano {liters} benzyny. Obecnie mam w baku {self.current_gas}l benzyny.")
#
#     def drive(self, kilometers):
#         print(f"Chcialbym przejechac {kilometers} kilometrow.")
#         range = self.current_gas/self.gas_per_100km * 100
#         gas_usage = kilometers/100 * self.gas_per_100km
#         if gas_usage <= self.current_gas:
#             self.current_gas -= gas_usage
#             print(f"Przejechano {kilometers} kilometrow. W baku zostalo {self.current_gas}l benzyny.")
#         else:
#             self.current_gas = 0
#             print(f"Przejechano {range} kilometrow i skonczyla sie benzyna.")
#
# s = Car("Syrenka", 50, 20, 25)
# s.add_gasoline(10)
# s.add_gasoline(20)
# s.drive(200)
# s.drive(200)
# s.add_gasoline(60)
# s.drive(300)
