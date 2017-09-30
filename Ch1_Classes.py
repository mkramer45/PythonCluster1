

class Employee:  # here is our class

    def __init__(self, first, last, pay):  # here are our variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  # this is our method
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Mike', 'Kramer', '50000')  # these are our instances within the class
emp_2 = Employee('Derek', 'Welmendorf', 500032)  # these are our instances within the class


print(emp_1.fullname())
# or we could do  print(Employee.fullname(emp_1) ... same result


