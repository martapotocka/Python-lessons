# stworz klase Wrozka i w metodzie init pobierz imie wrozki oraz jej stawke
# stworz trzy dodatkowe pola klasy (nie pobierane od usera):
# - dobra wrozba na temat milosci
# - dobra wrozba na temat pieniedzy
# - dobra wrozba bez konkretnego tematu

# stworz metode do witania klienta i podawania stawki (pobiera imie klienta)
# stworz metode do wrozenia klientowi w zaleznosci od potrzeb
# (pobiera imie klienta i typ wrozby)

# stworz dwie wrozki
# wrozka1 ma powrozyc Tadeuszowi ktory szuka milosci
# wrozka2 Alicji ktora chce pieniedzy
# wrozka2 Marianowi, ktory nie wie czego szuka


class Wrozka:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.good_omen_love = "poznasz przystojnego bruneta"
        self.good_omen_money = "wygrasz na loterii"
        self.good_omen_generic = "wszystko bedize super"

    def greet_customer(self, name):
        print(f"Witaj {name}. Mam na imie {self.name} i moja stawka za godzine to {self.price}")

    def say_omen(self, name, need):
        if need == 'love':
            print(f"Witaj {name}, wkrotce {self.good_omen_love}")
        elif need == 'money':
            print(f"Witaj {name}, wkrotce {self.good_omen_money}")
        else:
            print(f"Witaj {name}, wkrotce {self.good_omen_generic}")

e = Wrozka('Esmeralda', 50)
r = Wrozka('Rozalia', 100)

e.greet_customer("Tadeusz")
e.say_omen("Tadeusz", "love")

r.greet_customer("Alicja")
r.say_omen("Alicja", "money")

r.greet_customer("Marian")
r.say_omen("Marian", 'nie wiadomo')














# class Fairy:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.good_omen_love = "poznasz przystojnego bruneta"
#         self.good_omen_money = "wygrasz na loterii"
#
#     def welcome_customer(self):
#         print(f"Jestem wrozka {self.name} i biore {self.price} za godzine wrozenia.")
#
#     def say_omen(self, customer_name, omen_type):
#         if omen_type == 'love':
#             print(f"Witaj {customer_name}, wkrotce {self.good_omen_love}.")
#         elif omen_type == 'money':
#             print(f"Witaj {customer_name}, wkrotce {self.good_omen_money}.")
#         else:
#             print(f"Witaj {customer_name}, twoje zycie wkrotce sie zmieni.")
#
# rozalia = Fairy("Rozalia", 150)
# rozalia.welcome_customer()
# rozalia.say_omen("Tadeusz", "love")
# rozalia.say_omen("Katarzyna", "money")
# rozalia.say_omen("Zdzichu", "wstydzi sie pytac")
