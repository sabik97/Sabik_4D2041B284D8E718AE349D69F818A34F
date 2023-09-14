#Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality. 
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}"
        elif amount > self.__account_balance:
            return "Insufficient funds."
        else:
            return "Invalid withdrawal amount. Please enter a positive amount."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ₹{self.__account_balance}"
if __name__ == "__main__":
    account1 = BankAccount("(9876543210)", "SABIK", 10000)

    print(account1.display_balance())
    print(account1.deposit(5000))
    print(account1.withdraw(2000))
    print(account1.withdraw(15000))
    print(account1.display_balance())