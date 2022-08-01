class Employee:
    company = "Google"
    salary = 100


Hamid = Employee()
Majid = Employee()
print(Hamid.company)
print(Majid.company)
#  creating instance  attribute for first object
Hamid.salary = 200  # first priority is to check instance attribute otherwise go for class attribute
print(Hamid.salary)
print(Majid.salary)
Hamid.company = "Youtube"
Majid.company = "Youtube"
print(Hamid.company)
print(Majid.company)