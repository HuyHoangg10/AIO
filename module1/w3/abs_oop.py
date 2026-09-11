from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass


class CreditCardPayment(PaymentProcessor):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def process_payment(self, amount: float) -> str:
        return f"Paid {amount} via credit card {self.card_number}"


class MomoPayment(PaymentProcessor):
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def process_payment(self, amount: float) -> str:
        return f"Paid {amount} via Momo wallet {self.phone_number}"


def check_out(processor: PaymentProcessor, amount) -> None:
    print(processor.process_payment(amount))


credit_1 = CreditCardPayment("1234-5678-9999")
print(credit_1.process_payment(100.0))

check_out(credit_1, 500)
