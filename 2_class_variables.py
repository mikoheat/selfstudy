# class variables should be identical
# class variables are shared among all instances of a class

class Employee:

    raise_amount = 1.04 # class variables
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '-' + self.last + '@company.com'

        Employee.num_of_emps += 1 # it shouldn't be self.num_of_emps

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # To access class variables, it can be done
        # through class itself or instance of the class
        # raise_amount (wrong)
        # Employee.raise_amount .vs self.raise_amount (correct)
        # Employee.raise_amount affects instances of the class
        # self.raise_amount affects only the instance, other instances of the class are not changed
