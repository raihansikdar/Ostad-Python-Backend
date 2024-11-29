class Banking:
     def __init__(self, user_name, initial_balance) -> None:
          self.user_name  = user_name
          self.initial_balance = initial_balance
          
     def deposit(self, deposit_amount) -> int:
         if deposit_amount>0:
             self.initial_balance += deposit_amount
         return deposit_amount
     
     def get_balance(self) -> int:
         return self.initial_balance
     
     def withdraw(self, withdraw_amount):
          if withdraw_amount < self.initial_balance:
              self.initial_balance -= withdraw_amount
              return withdraw_amount
          else:
              return f"Insufficient Balance"
         
          
clint = Banking("Raihan", 5000)
print(f"Account Name: {clint.user_name}")
print(f"Initial Balance is: {clint.initial_balance}")
print(f"Deposit Balance: {clint.deposit(2000)}")
print(f"After deposit, Your Balance is: {clint.get_balance()}")
print(f"Withdraw Balance: {clint.withdraw(4000)}")
print(f"After withdraw, Your Balance is: {clint.get_balance()}")