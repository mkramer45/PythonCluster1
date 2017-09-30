class Employee:

    raise_amount = 1.04  ## default raise amount for all employees is 4%, unless specified otherwise (in an instance)

    def __init__(self, first, last, pay):  # init is the constructor for this class ... allows us to call it ... self is the instance of this object
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):  # this is our method
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)  # apply_raise is a method of taking adding the raise ... which is calculated by employee's pay * raise amount


emp_1 = Employee('Mike', 'Kramer', 50000)  # these are our instances within the class ... instantiating our employee1
emp_2 = Employee('Derek', 'Welmendorf', 500032)  # these are our instances within the class ... instantiating our employee2

# emp_1.raise_amount = 1.05  # for emp 1 ... we are saying screw the default raise amount defined in our class, let's defined a new raise amount in our instance for emp_1


print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)





