class Employee:
    company = "Google"

    def getsalary(self, signature, testing):
        print(f"salary of employee working in {self.company} is {self.salary} {signature} {testing}")

    @staticmethod  # sometimes we need function that does not use self parameter than we call @static method
    def greet():
        print("Good morning, Sir")


Hamid = Employee()
Hamid.salary = 200000
Hamid.getsalary("thanks", "testing")  # we can add many parameters in that function
# Employee.getSalary(Hamid) # this is for sense
Hamid.greet()
