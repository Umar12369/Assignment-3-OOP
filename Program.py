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

    
    
    
    
    
    
    
    def run(self):
        self.show_main_menu()

program = Program()
program.run()