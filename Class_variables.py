class Employee:
    raise_amount = 1.04  # class variables  It can be used across the Class Methods
    reduce_amout = 0.88  # class variables

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return "{} {} ".format(self.first, self.last)

    def pay_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def reduce_pay(self):
        self.pay = int(self.pay * Employee.reduce_amout)


emp1 = Employee('Bhaskar', 'S K', 50000)
emp2 = Employee('Udhay', 'Pt', 60000)

print(emp1.pay)
emp1.pay_raise()
print(emp1.pay)
emp1.reduce_pay()
print(emp1.pay)
