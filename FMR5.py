

def CheckEven(No):
    return(No % 2 ==0)

def FilterX(CheckEven,Data):
    Results = []
    for No in Data:
        if((CheckEven) == True):
            Results.append(No)
    return Results

def main():
    print("ente the size")
    size = int(input())
    DataInput = []
    for i in range(0,size):
        print("enter the values")


