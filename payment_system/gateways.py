from interfaces import OnlinePaymentGateway, OfflinePaymentGateway


class StripePaymentGateway(OnlinePaymentGateway):
    def charge(self, amount: float):
        print(f"[Stripe] Charging ${amount} online.")


class PayPalPaymentGateway(OnlinePaymentGateway):
    def charge(self, amount: float):
        print(f"[PayPal] Charging ${amount} online.")


class CashOnDeliveryPaymentGateway(OfflinePaymentGateway):
    def collect_cash(self, amount: float):
        print(f"[COD] Collecting ${amount} in cash at delivery.")
