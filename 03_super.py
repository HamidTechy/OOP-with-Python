class Person:
    country = "Pakistan"

    def __init__(self):
        super().__init__()
        print("Initialising Person")

    def takebreakth(self):
        print("i am breathing")


class Employee(Person):
    company = "Google"

    def __init__(self):
        super().__init__()
        print("initialising Employee")

    def getsalary(self):
        print(f"Salary is very high in {self.company}")

    def takebreakth(self):
        super().takebreakth()
        print("i am also breathing")


class Programmer(Employee):  # it will go for child 1 class and child 1 go for parent class this is the sequence
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("initialising Program")

    @staticmethod
    def toplevel():
        print("this programmer is doing highly paid project")

    def takebreakth(self):
        super().takebreakth()
        print("i am Programmer and i also breathing")


# p = Person()
# p.takebreakth()

e = Employee()
# e.takebreakth()

pr = Programmer()
# pr.takebreakth()
