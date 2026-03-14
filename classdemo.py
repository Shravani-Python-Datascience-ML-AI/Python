class Demo:
    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B

    def Fun(self):
        return self.No1
        return self.No2

    def Gun(self):
        return self.No1
        return self.No2


def main():


    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)




    Ans = obj1.Fun()
    print(" instance variable of obj1 ", Ans)

    Ans = obj2.Gun()
    print("instance variable of obj1 : ", Ans)

    Ans = obj1.Fun()
    print("instance variable of obj2 ", Ans)

    Ans = obj2.Gun()
    print("instance variable of obj2 : ", Ans)


if __name__ == "__main__":
    main()