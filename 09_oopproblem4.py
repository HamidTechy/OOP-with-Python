class Calculator:

    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"square of {self.num} is {self.num **2}")

    def squareroot(self):
        print(f"squareroot of {self.num} is {self.num **0.5} ")

    def cube(self):
        print(f"cube of {self.num} is {self.num **3}")

    @staticmethod
    def greet():
        print("****** Hello Welcome to the best calculator of this world ******")


calc = Calculator(9)
calc.greet()
calc.square()
calc.squareroot()
calc.cube()
