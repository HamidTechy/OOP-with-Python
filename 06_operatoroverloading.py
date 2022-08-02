#  this methods are called dundar methods and we use them with __name__ just like that
class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("lets Add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("lets Multiply")
        return self.num * num2.num


n1 = Number(12)
n2 = Number(7)
add = n1 + n2
print(add)
mul = n1 * n2
print(mul)
