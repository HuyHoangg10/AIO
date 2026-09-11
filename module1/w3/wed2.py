from abc import ABC, abstractmethod


class InsufficientFundsError(Exception):
    pass


class Account(ABC):
    def __init__(self, account_number: str, balance: float):
        super().__init__()
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

class SavingsAccount(Account):
    def __init__(self, account_number:str, balance:float):
        super().__init__(account_number, balance)

    def withdraw(self, amount:float) -> None:
        if amount > self.balance:
            raise InsufficientFundsError("Not enough money to draw") 
        else:
            self.balance -= amount

acc = SavingsAccount("ACC01", 100.0)
try:
    acc.withdraw(150.0)
except InsufficientFundsError as err:
    print(f"Transaction failed: {err}")
    
        