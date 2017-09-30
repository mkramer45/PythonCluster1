class Employee:

    def __init__(self, first, last):

        self.first = first
        self.last = last
# self.email = first + '.' + last + '@company.com'  .... commented this attribute out to avoid duplictes because we named our method/function email

    @property
    def fullname(self):  # this is our method
            return '{} {}'.format(self.first, self.last)

    @property   # here is our property decorator ... this allows us to call this method as an attribute (meaning without having to call with parenthesis like a method/function)
    def email(self):  # this is our method
            return '{}.{}@email.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):  # defining our setter as the object we wish to set, in this case it is the fullname method/function
        first, last = name.split(' ')  # our full name setter is going to consist of first + last name (Mike Kramer) ... split by a space ' '
        self.first = first  # The employee class' self.first + self.last is what we're using here
        self.last = last

#    @fullname.deleter
#    def fullname(self):
#        print('Delete Name!')
#        self.first = None
#        self.last = None



emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Mike Kramer'  # our situation... we change our full name to this ... and we expect print first + print email to be updated accordingly ... that doesn't work, so we use a 'setter'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# del emp_1.fullname