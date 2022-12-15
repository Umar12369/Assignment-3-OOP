
class Account:
  def __init__(self, account_number, account_holder_name, rate_of_interest, balance):
    self.account_number = account_number
    self.account_holder_name = account_holder_name
    self.rate_of_interest = rate_of_interest
    self.balance = balance

# getters method
  def get_account_number(self):
    return self.account_number
  
  def get_account_holder_name(self):
    return self.account_holder_name
  
  def get_rate_of_interest(self):
    return self.rate_of_interest
  
  def get_balance(self):
    return self.balance
  
  #setters method
  def set_account_holder_name(self, account_holder_name):
    self.account_holder_name = account_holder_name
  
  def set_rate_of_interest(self, rate_of_interest):
    self.rate_of_interest = rate_of_interest
  
  def deposit(self, amount):
    # Implement the logic for deposit
    # Update the balance of the account
    pass
  
  def withdraw(self, amount):
    # Implement the common logic for withdrawal
    # This method should be overridden by the derived classes
    pass