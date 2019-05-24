# stworz klase Wrozka
# dodaj metode bezparametrowa w ktorej wrozka podaje swoja stawke za godzine
# dodaj metode pobierajaca parametr(imie), w ktorej wrozka wita klienta
# dodaj metode pobierajaca dwa parametry (imie,wrozba), w ktorej wrozka wyglasza wrozbe
#
# stworz obiekt klasy Wrozka
# podaj stawke, przywitaj i powróż dwom roznym osobom


class Wrozka:

    def say_price(self):
        print("Stawka za godzine wynosi 50zl.")

    def greet_customer(self, name):
        print(f"Witaj {name}. Wiem co cie tu sprowadza.")

    def say_omen(self, name, omen):
        print(f"{name}, czeka cie {omen}")

esmeralda = Wrozka()
esmeralda.say_price()
esmeralda.greet_customer("Tadeusz")
esmeralda.say_omen("Tadeusz", "bogactwo")
esmeralda.greet_customer("Stefania")
esmeralda.say_omen("Stefania", "interesujace spotkanie.")









# class Fairy:
#
#     def say_price(self):
#         print("Cena za godzine wrozenia to 100zł.")
#
#     def welcome_customer(self, name):
#         print(f"Witaj {name}. Co cie do mnie sprowadza?")
#
#     def say_omen(self, name, omen):
#         print(f"{name}, wkrotce {omen}")
#
#
# esmeralda = Fairy()
# esmeralda.say_price()
# esmeralda.welcome_customer("Tadeusz")
# esmeralda.say_omen("Tadeusz", "wygrasz w totka.")
# esmeralda.welcome_customer("Katarzyna")
# esmeralda.say_omen("Katarzyna", "poznasz przystojnego bruneta.")
