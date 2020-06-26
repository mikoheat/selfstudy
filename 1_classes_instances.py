# basis of creating and instanciating class, instance variables

# why using class
# they allow us to logically group our data and functions in a way that's easy to reuse
# and also easy to build upon if need to be

# data and functions that are associated with a specific class
# we call those attributes and methods

class Employee: # class is a blueprint of instances
    def __init__(self, first, last, pay): # method of initialize and it is called constructor in other language
        # self means here is indicating an 'instance' itself.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '-' + self.last + '@company.com'

    # let's say that we wanted the ability to perform some kind of action
    # we can add some methods to our class
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('kim', 'taeho', 60000)
emp_2 = Employee('unit', 'test', 40000)

print(emp_1.fullname()) # we need parenthesis because it is a method not a attribute
print(emp_2.fullname()) # if we take off the parenthesis, it returns address of itself on memory
                        # in parenthesis, argument 'self' passes automatically
Employee.fullname(emp_1)# this line works exactly same as  emp_1.fullname()

# instance variable .vs class variables
# need to distinguish those precisely
# it's important to know the difference between those


# instance variables contain data that is unique to each instance

# emp_1.first = "kim"
# emp_1.last = "taeho"
# emp_1.email = "taeho3126@naver.com"
# emp_1.pay = 60000


# we wouldn't want to have manually set these variables every time. So we need "__init__() method".