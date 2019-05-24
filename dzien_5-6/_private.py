class Customer:

    def __init__(self, name, yearly_spent):
        self.name = name
        self.yearly_spent = yearly_spent
        self._rate = self._rate_customer() # prywatne pole klasy

    def _rate_customer(self):
        if self.yearly_spent > 1000:
            return 'very good'
        elif self.yearly_spent > 500:
            return 'good'
        else:
            return 'standard'

    def give_discount(self):
        if self._rate == "very good":
            print(f"{self.name}, dostaniesz 20% rabatu.")
        elif self._rate == "good":
            print(f"{self.name}, dostaniesz 10% rabatu.")
        else:
            print(f"{self.name}, nie dostaniesz rabatu.")

c1 = Customer("Tadeusz", 5000)
c2 = Customer("Maria", 999)
c3 = Customer("Janek", 50)
c1.give_discount()
c2.give_discount()
c3.give_discount()
print(c1.name, c1.yearly_spent, c1._rate) # dziala, ale nie powinnismy

# ex55_private.py
# ex56_car.py
