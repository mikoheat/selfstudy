# Learning special methods. These are also called magic or dunder methods.
# These methods allow us to emulate built-in types or implement operator overloading.

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '-' + last + '@eamil.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee('Test', 'User', 50000)
emp_2 = Employee('jankos', 'Usher', 70000)

print(emp_1)
print(emp_1 + emp_2)