#  this is also callled sigle inheritance
class Employee:
    company = "Google"

    @staticmethod
    def salaryinfo():
        print("All employee are highly paid here")

    @staticmethod
    def experience():
        print("mostly engineer have more then 3 years of experience")


class Programmer(Employee):  # this is inheritance which mean child class object can use parent class function
    language = "Python"

    def firstlang(self):
        print(f"My first programing language is {self.language}")

    @staticmethod
    def secondlang():
        print(f"after this i will learn c++")


e = Employee()
p = Programmer()
e.salaryinfo()
e.experience()
p.salaryinfo()
p.experience()
p.firstlang()
p.secondlang()
Employee.company = "youtube"
print(e.company)
