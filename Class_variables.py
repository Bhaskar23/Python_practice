class Employee:
    raise_amount = 1.04  # class variables  It can be used across the Class Methods
    num_of_emps = 0

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {} ".format(self.first, self.last)

    def pay_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def reduce_pay(self):
        self.pay = int(self.pay * Employee.reduce_amout)

print(Employee.num_of_emps)
emp1 = Employee('Bhaskar', 'S K', 50000)
emp2 = Employee('Udhay', 'Pt', 60000)

print(Employee.num_of_emps)
