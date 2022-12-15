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