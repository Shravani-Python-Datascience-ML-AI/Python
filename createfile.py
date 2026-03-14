import os


def write_file(fileName):
    if(os.path.exists(fileName)):
        print("enter the data  that you want to write in the file")
        data = input()



    else:
        print("file is not existing")
        return


def main():
    print("enter the file name to create")
    Name = input()


    write_file(Name)


if __name__ == "__main__":
    main()
