# Lab Exercise 14: Bank Account System using OOP

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance          # private attribute (encapsulation)
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit: amount must be positive.")
            return
        self.__balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal: amount must be positive.")
        elif amount > self.__balance:
            print(f"Insufficient balance! Available: {self.__balance}")
        else:
            self.__balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

    def show_history(self):
        print("Transaction history:", self.transactions)


# ---- Simulation / Testing ----
acc = BankAccount("Asha", 1000)
print("Balance:", acc.get_balance())

acc.deposit(500)        # valid
acc.withdraw(300)       # valid
acc.withdraw(5000)      # insufficient balance
acc.deposit(-100)       # invalid amount
acc.withdraw(0)         # invalid amount

print("Final balance:", acc.get_balance())
acc.show_history()

# acc.__balance cannot be accessed directly -> data protection
try:
    print(acc.__balance)
except AttributeError:
    print("Direct access to balance is blocked (encapsulation).")