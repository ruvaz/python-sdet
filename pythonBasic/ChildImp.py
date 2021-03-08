from pythonBasic.OopsDemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def getCompleteData(self):
        print(self.num2 + self.num)
        return self.num2 + self.num


obj = ChildImpl(4, 5)
obj.Suma()
