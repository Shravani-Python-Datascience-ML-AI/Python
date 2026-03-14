class Bank_Account:


    Bank_Account
    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0
    def CreateAccount(self):
        print("enter your name:")
        self.Name = input()

        print("enter your initial amount:")
        self.Amount = input()

        print("enter your address:")
        self.Address = input()

        print("enter your AccountNumber:")
        self.AccountNo = int(input())
    def DisplayAccountInfo(self):


        print("__________Your Account Information is as below________")
        print("Name of account holder:", self.Name)
        print("Name of account holder:", self.AccountNo)
        print("Name of account holder:", self.Address)
        print("Name of account holder:", self.Amount)

def main():
    print("name:",Bank_Account.Bank_Name)
    print("interest",Bank_Account.ROT_On__FD)
    User1 = Bank_Account()
    User2 = Bank_Account()


    User1.CreateAccount()
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()



if __name__ == "__main__":
    main()