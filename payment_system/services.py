from interfaces import OnlinePaymentGateway, OfflinePaymentGateway


class PaymentValidator:
    def validate_amount(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")


class NotificationService:
    def send_receipt(self, method: str, amount: float):
        print(f"[Notification] Receipt sent for {method} payment of ${amount}.")


class PaymentService:
    def __init__(self, validator: PaymentValidator, notifier: NotificationService):
        self.validator = validator
        self.notifier = notifier

    def process_online_payment(self, gateway: OnlinePaymentGateway, amount: float):
        self.validator.validate_amount(amount)
        gateway.charge(amount)
        self.notifier.send_receipt(gateway.__class__.__name__, amount)

    def process_offline_payment(self, gateway: OfflinePaymentGateway, amount: float):
        self.validator.validate_amount(amount)
        gateway.collect_cash(amount)
        self.notifier.send_receipt(gateway.__class__.__name__, amount)
