class Employee:
    company = "Google"

    def __init__(self, name, salary, unit):
        print("Employee is created")
        self.name = name
        self.salary = salary
        self.unit = unit

    def getdetail(self):
        print(f"Name of employee is {self.name}")
        print(f"salary of employee is {self.salary}")
        print(f"unit of employee is {self.unit}")


Hamid = Employee("Hamid", 100, "Youtube")
Employee.getdetail(Hamid)
