
# pobierz w konstruktorze imie, oraz odsetek trafnych wrozb (wyrazony w procentach np '60%')
# i stworz takie pola klasy
# stworz metode, ktora na podstawie odsetka trafnosci okresli czy wrozka jest:
# dobra (powyzej 80 trafnych)
# srednia (powyzej 50 trafnych)
# kiepska (ponizej 50 trafnych)
# stworz odpowiednie pole klasy do przechowywania tej informacji
# stworz metode do wydrukowania informacji o wrozce (imie i kategoria)

class Wrozka:

    def __init__(self, name, acc):
        self.name = name
        self.acc = int(acc[:-1])
        self.rate = self.give_rate()

    def give_rate(self):
        if self.acc > 80:
            return 'dobra'
        elif self.acc > 50:
            return 'srednia'
        else:
            return 'kiepska'

    def print_info(self):
        print(f"Wrozka {self.name} jest {self.rate}")

e = Wrozka("Esmeralda", "85%")
r = Wrozka("Rozalia", "55%")

e.print_info()
r.print_info()





# class Fairy:
#
#     def __init__(self, name, correct_rate):
#         self.name = name
#         self.correct_rate = correct_rate
#         self.cathegory = self.give_the_cathegory()
#
#     def give_the_cathegory(self):
#         correct_rate_int = int(self.correct_rate[:-1])
#         if correct_rate_int > 80:
#             return 'good'
#         elif correct_rate_int > 50:
#             return 'average'
#         else:
#             return 'poor'
#
#     def print_info(self):
#         print(f"The fairy name is {self.name} and she has the {self.cathegory} cathegory.")
#
#
# esmeralda = Fairy("Esmeralda", "85%")
# rozalia = Fairy("Rozalia", "60%")
# miranda = Fairy("Miranda", "30%")
# esmeralda.print_info()
# rozalia.print_info()
# miranda.print_info()
