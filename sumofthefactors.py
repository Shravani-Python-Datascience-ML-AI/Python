# Python Program to find the sum of factors of a number


def checkFactor(iValue, iNo):
    if iValue == 0 or iNo == 0:
        return False

    if iNo % iValue == 0:
        return True
    else:
        return False


def AddFactors(iNo):
    if iNo == 0:
        return 0

    iSum = 0
    for iCnt in range(iNo):
        if checkFactor(iCnt, iNo) == True:
            iSum = iSum + iCnt

    return iSum


def main():
    iNo = int(input("Enter number : "))
    print("Addition of factor of a number is ",AddFactors(iNo))


if __name__ == "__main__":
    main()
