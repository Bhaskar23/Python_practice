class Employee:
    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay


emp1 = Employee('Bhaskar', 'S K', 50000)
emp2 = Employee('Udhay', 'Pt', 60000)

print("{} has {} pay".format(emp1.first,emp1.pay))
print("{} has {} pay".format(emp2.first,emp2.pay))
