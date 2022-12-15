from Account import Account

class ChecquingAccount(Account):
  def __init__(self, account_number, account_holder_name, rate_of_interest, balance, overdraft_limit):
    # Call the constructor of the base class to initialize the common properties
    super().__init__(account_number, account_holder_name, rate_of_interest, balance)
    self.overdraft_limit = overdraft_limit
  
  def withdraw(self, amount):
    # Override the base class method to implement the additional logic for ChecquingAccount
    # Reject transactions that cannot be completed even after using the overdraft limit
    pass