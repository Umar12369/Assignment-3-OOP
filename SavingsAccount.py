from Account import Account

class SavingsAccount(Account):
  def __init__(self, account_number, account_holder_name, rate_of_interest, balance, min_balance):
    # Call the constructor of the base class to initialize the common properties
    super().__init__(account_number, account_holder_name, rate_of_interest, balance)
    self.min_balance = min_balance
  
  def withdraw(self, amount):
    # Override the base class method to implement the additional logic for SavingsAccount
    # Reject transactions that would bring the current balance of the account below the minimum balance
    pass
