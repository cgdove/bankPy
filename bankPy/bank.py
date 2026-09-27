import pickle
import os

accounts = []

def addAccount(accounts):
    accNo = input("Enter account number: ")
    name = input("Enter holder's name: ")
    balance = input("Enter initial balance: ")
    accounts += [{"accNo": accNo, "name": name, "balance": int(balance)}]

def incBalance(accounts):
    accNo = input("Enter accNo: ")
    amount = input("Enter the amount: ")
    for el in accounts:
        if el["accNo"] == accNo:
            el["balance"] += int(amount)

def storeAccounts(accounts):
    os.remove("./bankStore")  # remove existing bank account records from backing storage
    storeFile = open('bankStore', 'ab')
    pickle.dump(accounts, storeFile)
    storeFile.close()

def loadAccounts():
    global accounts
    storeFile = open('bankStore', 'rb')
    accounts = pickle.load(storeFile)

def main():
    print("Commands:")
    print("Display accounts [display], Add account [add], Increment balance [inc]")
    print("Store accounts [store], Load accounts [load], Exit [exit]")
    while(True):
        command = input("Enter a command: ")
        if command == "add":
            addAccount(accounts)
        elif command  == "display":
            print(accounts)
        elif command == "inc":
            incBalance(accounts)
        elif command == "exit":
            exit()
        elif command == "store":
            storeAccounts(accounts)
        elif command == "load":
            loadAccounts()
        else:
            print("Command not recognised.")

if __name__ == "__main__":
    main()


            
            
    
