from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    """Marker base class for all payment gateways."""
    pass


class OnlinePaymentGateway(PaymentGateway):
    """Interface for online payment gateways."""
    @abstractmethod
    def charge(self, amount: float):
        pass


class OfflinePaymentGateway(PaymentGateway):
    """Interface for offline payment gateways."""
    @abstractmethod
    def collect_cash(self, amount: float):
        pass
