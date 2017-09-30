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


emp_1 = Employee('Mike', 'Kramer', 50000)  # these are our instances within the class ... instantiating our employee1
emp_2 = Employee('Derek', 'Welmendorf', 500032)  # these are our instances within the class ... instantiating our employee2
emp_3 = Employee('Solomun', 'Techno', 5000332)

emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'Jane-Dope-90000'

# first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee.from_string(emp_str_1)  # this would run our init method aka call from it

print(new_emp_1.email)
print(new_emp_1.pay)







