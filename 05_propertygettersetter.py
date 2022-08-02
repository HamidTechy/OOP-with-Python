class Employee:
    Company = "Zaman Board"
    salary = 6000
    salarybonus = 500

    @property  # this is also called getter
    def totalsalary(self):
        return self.salary + self.salarybonus

    @totalsalary.setter  # this is called setter
    def totalsalary(self, val):
        self.salarybonus = val - self.salary


e = Employee()
print(e.salary)
print(e.salarybonus)
print(e.totalsalary)  # print(e.totalsalary()) we can call function like with without property method
e.totalsalary = 6300
print(e.totalsalary)
print(e.salarybonus)
