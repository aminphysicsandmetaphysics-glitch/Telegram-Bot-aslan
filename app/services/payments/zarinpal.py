import httpx
from .base import PaymentProvider

class ZarinpalProvider(PaymentProvider):
    def __init__(self, merchant_id: str, callback_url: str):
        self.merchant_id = merchant_id
        self.callback_url = callback_url

    async def create_invoice(self, user_id: int, amount: int, desc: str):
        payload = {
            "merchant_id": self.merchant_id,
            "amount": amount,
            "callback_url": self.callback_url,
            "description": desc
        }
        async with httpx.AsyncClient(timeout=15) as c:
            r = await c.post("https://api.zarinpal.com/pg/v4/payment/request.json", json=payload)
            data = r.json()
        # TODO: extract and return real pay_url/authority
        return {"pay_url": data.get("data",{}).get("link",""), "authority": data.get("data",{}).get("authority","")}

    async def verify(self, authority: str):
        # TODO: implement verify based on Zarinpal docs
        return {"status":"paid", "ref_id":"DEMO-REF"}
