



def large(Arr):
    large = Arr[0]
    for i in Arr:
        if i > large:
         large = i
    return large

def main():

    list = []
    print("enter the size")
    size = int(input())
    print("enter the values")
    for i in range(0,size):
      values = int(input())
      list.append(values)
    print(large(list))

if __name__ == "__main__":
    main()

