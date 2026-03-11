class BankAccount:

    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)

    def display_details(self):
        print("Account Number:", self.acc_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


accounts = {}

while True:

    print("\n---- Bank Management System ----")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Account")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        acc_no = int(input("Enter Account Number: "))
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))

        accounts[acc_no] = BankAccount(acc_no, name, balance)
        print("Account Created Successfully")

    elif choice == 2:
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Deposit Amount: "))

        if acc_no in accounts:
            accounts[acc_no].deposit(amount)
        else:
            print("Account Not Found")

    elif choice == 3:
        acc_no = int(input("Enter Account Number: "))
        amount = float(input("Enter Withdraw Amount: "))

        if acc_no in accounts:
            accounts[acc_no].withdraw(amount)
        else:
            print("Account Not Found")

    elif choice == 4:
        acc_no = int(input("Enter Account Number: "))

        if acc_no in accounts:
            accounts[acc_no].check_balance()
        else:
            print("Account Not Found")

    elif choice == 5:
        acc_no = int(input("Enter Account Number: "))

        if acc_no in accounts:
            accounts[acc_no].display_details()
        else:
            print("Account Not Found")

    elif choice == 6:
        print("Thank You for Using Bank System")
        break

    else:
        print("Invalid Choice")
