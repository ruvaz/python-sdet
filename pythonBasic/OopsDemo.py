class Calculator:
    num = 100  # class vr

    def __init__(self, a, b):
        self.A = a
        self.B = b
        print("constructor")

    def getData(self):
        print("method in class to print")

    def Suma(self):
        print(self.A, self.B, Calculator.num, "=", self.A + self.B + Calculator.num)
        return self.A+self.B+Calculator.num

obj = Calculator(2, 4)  # create an obj in python
obj.getData()
obj.Suma()
