# regular methods .vs class methods .vs static methods
# regular methods in a class take automatically an instance of the class as the first argument
# calling this self

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '-' + self.last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount): # this is a class method.
        # we work with class, instead of instance
        # meaning that working with cls instead of self
        cls.raise_amount = amount
    # some people say class method is alternative constructor
    # you can use class methods in order to provide multiple ways creating our objects

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # create new employee and return it

    # static methods don't pass anything automatically as the first argument
    # they don't pass instances or class, it behaves just like regular functions
    # except that they are included in class
    # if you don't access the instance or the class anywhere within the method
    # then, it is probably appropriate to be a static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('taeho', 'kim', 60000)
emp_2 = Employee('test', 'user', 40000)

import datetime
my_date = datetime.date(2020, 6, 30)
print(Employee.is_workday((my_date)))

# # 1) set class variable accessing from class

# Employee.set_raise_amt(1.05)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# # 2) set class variable with a class method, accessing from instances of the class

# emp_1.set_raise_amt(1.07) # it still changes a class variable
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
# # Example why and how using class method
#
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# # before using a class method

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# # after using a class method

# new_emp_2 = Employee.from_string(emp_str_2)

# print(new_emp_2.email)
# print(new_emp_2.pay)