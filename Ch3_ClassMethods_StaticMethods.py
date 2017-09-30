class Employee:  # class
    def __init__(self, first, last):
        self.first = first
        self.last = last  # variables

    def fullname(self):
        return '{} {}'.format(self.first, self.last)  # function

emp_1 = Employee('Mike', 'Kramer')  # instance

print(emp_1)


