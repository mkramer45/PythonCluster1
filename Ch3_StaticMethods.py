class Employee:  # this tutorial is aboout regular methods vs static vs class methods

    """
  regular methods in a class automatically take the instance as the first argument (self) ... aka the instance
  creating class methods will allow us to instead take the class as the first argument
  all we need to do is add a decorator (def @classmethod)
    """

    num_of_emps = 0
    raise_amount = 1.04  # default raise amount for all employees is 4%, unless specified otherwise (in an instance)

    def __init__(self, first, last, pay):  # init is the constructor for this class ... allows us to call it ... self is the instance of this object
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):  # this is our method
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):  # common convention for regular methods is to define the argument as self
        self.pay = int(self.pay * self.raise_amount)  # apply_raise is a method of taking adding the raise ... which is calculated by employee's pay * raise amount

    @classmethod  # this is out decorator ... we are now using the class as our first argument, instead of the instance
    def set_raise_amt(cls, amount):  # common convention for class methods is using 'cls' as an argument instead of 'sel'f in our regular methods
        cls.raise_amount = amount
    """
    Above is where we are defining our class method
    """

    @classmethod  # this is an example of an altenative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day1):  # we are not taking instance OR class as an argument,  so lets just use day as our argument ... defining our method step1
        if day1.weekday() == 5 or day1.weekday() == 6:  # weekday is a keyword of the datetime method ... 0 is monday, 6 is sunday ... so we are checking for only weekends here
            return False
        return True

emp_1 = Employee('Mike', 'Kramer', 50000)  # these are our instances within the class ... instantiating our employee1
emp_2 = Employee('Derek', 'Welmendorf', 500032)  # these are our instances within the class ... instantiating our employee2

"""
lets create a function where it will take in a date, and determine if it is a workday or not
this method we want to create has no dependence on our instances or classes, so let's create a static method
"""

import datetime
my_date = datetime.date(2016, 7, 27)

print(Employee.is_workday(my_date))
