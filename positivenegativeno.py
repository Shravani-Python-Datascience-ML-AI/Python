#positive and negative no

def Chkno(no):
    if no == 0:
        print("zero")
    elif no > 0:
        print("Positive number")
    else:
        print(" Negative number")


def main():
   print("enter the number")
   no = int(input())
   Chkno(no)

if __name__ == "__main__":
   main()