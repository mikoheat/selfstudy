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



class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # the line above passes first, last, pay to my employee's __init__() method
        # and let that class handles those arguments
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.semployees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--> ', emp.fullname())


dev_1 = Developer('Test', 'Employee', 50050, 'Python')
dev_2 = Developer('dda', 'hyoni', 100000, 'Java')
mgr_1 = Manager('Sue', 'Lin', 90000, [dev_1])

print(mgr_1.email)
mgr_1.print_emps()
print("After")
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

# isinstance(instance, class)
# issubclass(class, class)