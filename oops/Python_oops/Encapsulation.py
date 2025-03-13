class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute 

    def get_balance(self):
        return self.__balance  # Getter method only it can acess __balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

my_account = BankAccount(500)
my_account.deposit(200)
print(f"Current balance: ${my_account.get_balance()}")
