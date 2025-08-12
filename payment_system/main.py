from services import PaymentValidator, NotificationService, PaymentService
from gateways import StripePaymentGateway, PayPalPaymentGateway, CashOnDeliveryPaymentGateway


if __name__ == "__main__":
    # Create service dependencies
    validator = PaymentValidator()
    notifier = NotificationService()
    payment_service = PaymentService(validator, notifier)

    # Online payments
    stripe = StripePaymentGateway()
    paypal = PayPalPaymentGateway()
    payment_service.process_online_payment(stripe, 200)
    payment_service.process_online_payment(paypal, 150)

    # Offline payment
    cod = CashOnDeliveryPaymentGateway()
    payment_service.process_offline_payment(cod, 300)
