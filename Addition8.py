print("Apllication to demonstrate industrial programming")
import module
def main():
    print("value of __name__from main is :",__name__)
    print("enter first number:")
    no1 = int(input())
    print(type(no1))
    print("enter second number:")
    no2 = int(input())
    print(type(no1))
    Sum = module.Addition(no1,no2)
    print("additon is:",Sum)
if __name__ == "__main__":
    main()