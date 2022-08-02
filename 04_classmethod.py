class Employee:
    Company = "Honda"
    City = "Sheikhupura"
    salary = 200

    #  __class__ method is a way to change class attribute
    #  def changesalary(self, salary):
    #  self.__class__.salary = salary

    # classmethod is used as another way to change the class attribute
    @classmethod
    def changesalary(cls, salary):  # first parameter of this method is usually cls but self not give error
        cls.salary = salary


e = Employee()
print(e.salary)
e.changesalary(300)  # if we call Employee() instead of e obj we should give self parameter also
print(e.salary)
print(Employee.salary)
