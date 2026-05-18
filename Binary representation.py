#Accept an integer from the user and display its value in binary format

def Binary(no):
    no = f"{no:b}"  
    return no       

def main():
    print("enter the number")
    Num = int(input())
    binary_value = Binary(Num) 
    print("binary value:", binary_value)

if __name__ == "__main__":
    main()