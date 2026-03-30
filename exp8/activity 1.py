# ATM withdraw system handles insufficient balance.
"""
Created on Mon Mar 30 15:35:42 2026

@author: Sohel Mulla
"""

class InsufficientBalanceError(Exception):
  """Custom Exception for insufficient balance"""
pass

def withdraw(balance, amount):
 try:
  if amount > balance:
   raise InsufficientBalanceError("Insufficient balance in your account.")
  elif amount <= 0:
    raise ValueError("Enter a valid withdrawal amount.")
  else:
   balance -= amount
  print(f"Withdrawal successful! Remaining balance: ₹{balance}")
  return balance
 except InsufficientBalanceError as e:
  print("Error:", e)

 except ValueError as v:
  print("Error:", v)

 except Exception as ex:
  print("Unexpected error:", ex)

# Main program
balance = 5000 # Initial balance

try:
 amount = float(input("Enter amount to withdraw: ₹"))
 balance = withdraw(balance, amount)
except Exception as e:
 print("Invalid input:", e)






