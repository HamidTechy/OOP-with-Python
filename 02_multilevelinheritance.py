# multilevel inheritance
class Person:
    country = "Pakistan"

    def takebreakth(self):
        print("i am breathing")


class Employee(Person):
    company = "Google"

    def getsalary(self):
        print(f"Salary is very high in {self.company}")

    def takebreakth(self):
        print("i am also breathing")


class Programmer(Employee):  # it will go for child 1 class and child 1 go for parent class this is the sequence
    company = "Fiverr"

    @staticmethod
    def toplevel():
        print("this programmer is doing highly paid project")

    def eating(self):
        print("programmer eating healthy food")


p = Person()
e = Employee()
pr = Programmer()
pr.toplevel()
pr.eating()
print(pr.company)
pr.takebreakth()
pr.getsalary()  # it will use function of parent and prefer his own class attribute instead of parent class attribute
