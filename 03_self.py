class Employee:
    company = "Google"
    salary = 100000

    def getSalary(self):
        print(f"salary of {self.name} working in {self.company} is {self.salary}")


Hamid = Employee()
Hamid.name = "Hamid"
Hamid.salary = 200000  # first prefrence is instance attribute
print(Hamid.getSalary())
Hamid.getSalary()  # Employee.getSalary(Hamid)
