class Circle:
    def __init__(self):
        print("Inside init method")
        self.Radius = 0.0
        self.Circumference = 0.0
        self.Area = 0.0
        self.pi = 3.14

    def Accept(self):
        print("enter the radius")
        r = int(input())
        return r

    def CalculateArea(self):
        Area = self.pi * self.r * self.r
        return Area

    def CalculateCircumference(self):
        Circumference = 2 * self.pi * self.r

    def Display(self):



def main():
    print("Inside main method")

    obj = Arithematic(11,10)
    Output = obj.Addition()
    print("Addition is : ",Output)
    Output = obj.Substraction()
    print("Substraction is : ",Output)

    objX = Arithematic(21,20)

if __name__ == "__main__":
    print("Inside starter")
    main()