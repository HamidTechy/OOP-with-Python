class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryafterincrement(self):
        return self.salary*self.increment

    @salaryafterincrement.setter
    def salaryafterincrement(self, sal):
        self.increment = sal / self.salary

e = Employee()
print(e.salaryafterincrement)
e.salaryafterincrement = 2000
print(e.increment)