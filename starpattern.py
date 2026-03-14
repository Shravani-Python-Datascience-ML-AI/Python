
# display input = 3   ***
#                     ***
#                     ***


def main():
    print("enter the no of rows")
    Row = int(input())
    for i in range(1,Row):
      for j in range(1,Row):
           print("*", end=' ')
      print()



if __name__ == "__main__":
    main()