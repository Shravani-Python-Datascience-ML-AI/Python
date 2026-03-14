#display Factors
#the factorial of 6 is 1*2*3*4*%*6 = 720


def main():
    print("enter the number")
    no = int(input())
    fact = 1

    for i in range(1,no+1):                 #no+1 - 1 to 6 lihale tr 1 hto 5 parayant janar
        fact = fact*i

    print("the factorial of a given no is",fact)





if __name__ == "__main__":
     main()