def CheckPrime(No):

    return all(No % i for i in range(2, No))

def Increment(No):
    return No*2

def filterX(Arr,CheckPrime):
    Result = []
    for no in Arr:
        if(CheckPrime(no)):
            Result.append(no)
    return Result

def mapX(Arr,Increment):
    Result = []
    for no in Arr:
        value = Increment(no)
        Result.append(value)
    return Result

def reduceX(Arr):
    max = Arr[0]
    for x in Arr:
        if x > max:
            max = x
    return max

def main():


    Arr = list()
    print("Enter how many elements you want to store?")
    size = int(input())

    print("Please enter the values")

    for i in range(0,size):
       no = int(input())
       Arr.append(no)




    print("Original data : ",Arr)


    Data_Filter = list(filterX(Arr,CheckPrime))

    print("Data after filter : ",Data_Filter)

    Data_map = list(mapX(Data_Filter,Increment))

    print("Data after map : ",Data_map)

    Ret = reduceX(Data_map)

    print("Data after reduce : ",Ret)

if __name__ == "__main__":
    main()
