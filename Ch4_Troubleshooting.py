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

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def fullname(self):  # this is our method
        return '{} {}'.format(self.first, self.last)

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):  # print the employees first name + --> if it these values are present in the employee class
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Johnson', 50000, 'Python')
dev_2 = Developer('Mike', 'Kramer', 100000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1, dev_2])  # if there is nothing in the employees place-holder, do nothing ... if there is something,

mgr_1.print_emps()