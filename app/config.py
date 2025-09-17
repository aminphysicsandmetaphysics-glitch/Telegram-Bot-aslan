import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BASE_URL = os.getenv("BASE_URL", "")
    WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", "/webhook")
    WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "changeme")

    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "aslan")
    ADMIN_PASSWORD_HASH = os.getenv("ADMIN_PASSWORD_HASH", "")
    ADMIN_JWT_SECRET = os.getenv("ADMIN_JWT_SECRET", "super-admin-secret")
    ADMIN_JWT_EXPIRE_MIN = int(os.getenv("ADMIN_JWT_EXPIRE_MIN", "720"))

    DATABASE_URL = os.getenv("DATABASE_URL", "")
    REDIS_URL = os.getenv("REDIS_URL", "")

    PAYMENT_PROVIDER = os.getenv("PAYMENT_PROVIDER", "zarinpal")
    ZARINPAL_MERCHANT = os.getenv("ZARINPAL_MERCHANT", "")
    CRYPTO_API_KEY = os.getenv("CRYPTO_API_KEY", "")
    CURRENCY = os.getenv("CURRENCY", "IRR")

    SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME", "YourSupportUser")
    VIP_RESULTS_CHANNEL = os.getenv("VIP_RESULTS_CHANNEL", "@your_vip_results")
    FREE_CHANNEL = os.getenv("FREE_CHANNEL", "@your_free_channel")
    INSTAGRAM_URL = os.getenv("INSTAGRAM_URL", "")
    SPONSOR_CHANNELS = os.getenv("SPONSOR_CHANNELS", "")

settings = Settings()
