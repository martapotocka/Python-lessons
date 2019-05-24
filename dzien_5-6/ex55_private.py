# stworz klase HealthRateCalculator, ktora w konstruktorze pobiera:
# - nazwisko pacjenta
# - wiek pacjenta
# - aktywnosc fizyczna pacjenta wyrazana w godzinach tygodniowo
# - bmi pacjenta

# stworz prywatne pola klasy zawierajace:
# - ocene wieku pacjenta
# - ocene bmi pacjenta
# - ocene aktywnosci pacjenta
# kazde z tych pol ma byc prywatne i wyliczane przy uzyciu specjalnej, prywatnej metody
# metoda przyznaje w kazdej kategorii punkty od 1(najmniej) do 3(najwiecej)

# stworz metode publiczna ktora na podstawie prywatnych pol z ocenami wypisze ogolna
# ocene zdrowia pacjenta:
# - powyzej 6 - pacjent w dobrej formie
# - powyzej 3 - pacjent sredniej formie
# - mniej - pacjent w zlej formie


class HealthRateCalculator:

    def __init__(self, patient_name, patient_bmi, patient_actity_hours_per_week, patient_age):
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_bmi = patient_bmi
        self.patient_actity_hours_per_week = patient_actity_hours_per_week
        self._patient_bmi_rate = self._calculate_bmi_rate()
        self._patient_actvity_rate = self._calculate_activity_rate()
        self._patient_age_rate = self._calculate_age_rate()

    def _calculate_bmi_rate(self):
        if self.patient_bmi > 30 or self.patient_bmi < 18:
            return 1
        elif self.patient_bmi > 25:
            return 2
        else:
            return 3

    def _calculate_activity_rate(self):
        if self.patient_actity_hours_per_week > 4:
            return 3
        elif self.patient_actity_hours_per_week > 2:
            return 2
        else:
            return 1

    def _calculate_age_rate(self):
        if self.patient_age > 70:
            return 1
        elif self.patient_age > 50:
            return 2
        else:
            return 3

    def calculate_health_rate(self):
        sum_of_rates = self._patient_age_rate + self._patient_bmi_rate + \
                       self._patient_actvity_rate

        if sum_of_rates > 7:
            print(f"Pacjent {self.patient_name} jest w bardzo dobrej formie.")
        elif sum_of_rates >= 5:
            print(f"Pacjent {self.patient_name} jest w sredniej formie.")
        else:
            print(f"Pacjent {self.patient_name} jest w kiepskiej formie.")

p1 = HealthRateCalculator("John", 25, 3, 35) # name, bmi, activity, age
p2 = HealthRateCalculator("Lucy", 31, 0, 55)
p3 = HealthRateCalculator("Stan", 17, 5, 71)
p1.calculate_health_rate()
p2.calculate_health_rate()
p3.calculate_health_rate()
