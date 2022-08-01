class Calculator:

    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"square of {self.num} is {self.num **2}")

    def squareroot(self):
        print(f"squareroot of {self.num} is {self.num **0.5} ")

    def cube(self):
        print(f"cube of {self.num} is {self.num **3}")


calc = Calculator(9)
calc.square()
calc.squareroot()
calc.cube()
#  Calculator.cube(calc)  # this syntax is also possible
