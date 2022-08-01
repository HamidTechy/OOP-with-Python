class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getdetail(self):
        print(f"Employee of {self.company} is {self.name},")
        print(f"Product of {self.company} is {self.product}")


Hamid = Programmer("Hamid", "Skype")
Majid = Programmer("Majid", "Visual Studio")
Programmer.getdetail(Hamid)
#  Programmer.getdetail(Majid)
Majid.getdetail() # this is also possible with this syntax
