class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Invalid amount or insufficient funds!")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number in self.accounts:
            print("Account number already exists!")
        else:
            new_account = BankAccount(account_number, account_holder)
            self.accounts[account_number] = new_account
            print(f"Account created for {account_holder} with account number {account_number}")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found!")
            return None

def main():
    bank = Bank()

    while True:
        print("\n--- Banking Management System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            bank.create_account(account_number, account_holder)

        elif choice == '2':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

        elif choice == '3':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

        elif choice == '4':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                account.check_balance()

        elif choice == '5':
            print("Thank you for using the Banking Management System.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
