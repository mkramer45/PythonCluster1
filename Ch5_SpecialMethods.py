class Employee:  # for this example, we will be using Managers and Developers as our sub classes for our parent class of Employee

    raise_amt = 1.04

    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        def fullname(self):  # this is our method
            return '{} {}'.format(self.first, self.last)

        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amt)

        def __repr__(self):
            return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)


emp_1 = Employee('Corey', 'Johnson', 50000)
emp_2 = Employee('Mike', 'Kramer', 100000)


print(emp_1)