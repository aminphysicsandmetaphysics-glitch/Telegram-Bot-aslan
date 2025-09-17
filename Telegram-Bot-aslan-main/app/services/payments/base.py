from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    @abstractmethod
    async def create_invoice(self, user_id: int, amount: int, desc: str) -> dict: ...
    @abstractmethod
    async def verify(self, **kwargs) -> dict: ...
