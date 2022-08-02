# this is multiple inheritance
class Employee:
    company = "Nestle"

    def grades(self):
        print(f"Managers in {self.company} are Grade 1 level employee")


class Freelancer:
    company = "upwork"

    @staticmethod
    def upgradelevel():
        print("this is just a function")


class Programmer(Employee, Freelancer):
    name = "Hamid"


p = Programmer()
print(p.company)  # it will give priority to methods and property to that class which is writen in () firstly
p.grades()
p.upgradelevel()
