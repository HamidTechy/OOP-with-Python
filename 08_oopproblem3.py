class Sample:
    a = "Hamid"


obj = Sample()
obj.a = "Majid"
#  Sample.a = "Majid"  # this will change class attribute

print(Sample.a)
print(obj.a)
