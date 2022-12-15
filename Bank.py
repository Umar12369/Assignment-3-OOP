from SavingsAccount import SavingsAccount
from ChequingAccount import ChecquingAccount

class Bank:
  def __init__(self):
    # Initialize an empty list of accounts
    self.accounts = []
    # Create 5 accounts with hardcoded values
    # These can be either SavingsAccount or ChecquingAccount
    self.accounts.append(SavingsAccount(123, "Salman", 0.04, 5000, 5000))
    self.accounts.append(ChecquingAccount(111, "John", 0.03, 6000, 1000))
    self.accounts.append(SavingsAccount(12345, "Sharukh", 0.05, 5000, 5000))
    self.accounts.append(ChecquingAccount(222, "James", 0.03, 6000, 1000))
    self.accounts.append(SavingsAccount(1234, "Umar", 0.06, 5000, 5000))
    
  
  def search_account(self, account_number):
    # Search for the account with the given account number in the list of accounts
    # Return the account object if found, else return None
    for account in self.accounts:
      if account.get_account_number() == account_number:
        return account
    
    return None