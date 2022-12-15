from Account import Account
from Bank import Bank
from SavingsAccount import SavingsAccount
from ChequingAccount import ChecquingAccount

class Program:
    
    def __init__(self):
        self.accounts = {} #dictionary to store values
    
    def show_main_menu(self):
        while True:
            print("Banking Main Menu:")
            print("1. Open Account")
            print("2. Select Account")
            print("3. Exit")
            choice = input("Enter your choice: ")
        
            if choice == "1":
                self.open_account()
            elif choice == "2":
                self.select_account()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def show_account_menu(self, account):
        while True:
            print("Account Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit Account")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                account.get_balance()
            elif choice == "2":
                account.deposit()
            elif choice == "3":
                amount = input("Enter the amount to withdraw: ")
                account.withdraw(amount)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    def open_account(self):
        # Prompt the user for account details and create an account object
        account_number = input("Enter the account number: ")
        account_holder_name = input("Enter the account holder's name: ")
        rate_of_interest = input("Enter the rate of interest: ")
        balance = input("Enter the balance: ")
        account_type = input("Enter the account type (1 for Savings, 2 for Checking): ")
        
        if account_type == "1":
        # Create a SavingsAccount object
            min_balance = input("Enter the minimum balance: ")
            account = SavingsAccount(account_number, account_holder_name, rate_of_interest, balance, min_balance)
        elif account_type == "2":
        # Create a ChecquingAccount object
            overdraft_limit = input("Enter the overdraft limit: ")
            account = ChecquingAccount(account_number, account_holder_name, rate_of_interest, balance, overdraft_limit)
        else:
            print("Invalid account type. Please try again.")
            return
        
        # Add the account to the accounts dictionary
        self.accounts[account_number] = account
        print("Account created successfully.")


    def select_account(self):
        # Prompt the user for the account number
        account_number = input("Enter the account number: ")
        
        # Search for the account in the accounts dictionary
        if account_number in self.accounts:
            account = self.accounts[account_number]
        # If found, call show_account_menu() with the account object as argument
            self.show_account_menu(account)
        else:
            print("Account not found. Please try again.")
    
    def run(self):
        self.show_main_menu()

program = Program()
program.run()