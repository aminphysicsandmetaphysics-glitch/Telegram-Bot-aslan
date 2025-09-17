import httpx
from .base import PaymentProvider

class CryptoProvider(PaymentProvider):
    def __init__(self, api_key: str, callback_url: str):
        self.api_key = api_key
        self.callback_url = callback_url

    async def create_invoice(self, user_id: int, amount: int, desc: str):
        headers = {"x-api-key": self.api_key}
        payload = {"price_amount": amount, "price_currency":"USD", "order_description":desc, "ipn_callback_url": self.callback_url}
        async with httpx.AsyncClient(timeout=15) as c:
            r = await c.post("https://api.nowpayments.io/v1/invoice", headers=headers, json=payload)
            data = r.json()
        return {"pay_url": data.get("invoice_url"), "invoice_id": data.get("id")}

    async def verify(self, **kwargs):
        # TODO: verify via IPN/callback
        return {"status":"paid", "tx":"DEMO-TX"}
