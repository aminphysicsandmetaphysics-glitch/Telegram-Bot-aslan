import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    BASE_URL = os.getenv("BASE_URL", "")
    WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", "/webhook")
    WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "changeme")

    # Admin panel
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "AMIN.101")
    ADMIN_PASSWORD_HASH = os.getenv("ADMIN_PASSWORD_HASH", "")
    ADMIN_JWT_SECRET = os.getenv("ADMIN_JWT_SECRET", "super-admin-secret")
    ADMIN_JWT_EXPIRE_MIN = int(os.getenv("ADMIN_JWT_EXPIRE_MIN", "720"))

    # DB
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://user:pass@host:5432/db")

    # Redis (optional)
    REDIS_URL = os.getenv("REDIS_URL", "")

    # Payments
    PAYMENT_PROVIDER = os.getenv("PAYMENT_PROVIDER", "zarinpal")
    ZARINPAL_MERCHANT = os.getenv("ZARINPAL_MERCHANT", "")
    CRYPTO_API_KEY = os.getenv("CRYPTO_API_KEY", "")
    CURRENCY = os.getenv("CURRENCY", "IRR")

    # Links
    SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME", "YourSupportUser")
    VIP_RESULTS_CHANNEL = os.getenv("VIP_RESULTS_CHANNEL", "@your_vip_results")
    FREE_CHANNEL = os.getenv("FREE_CHANNEL", "@your_free_channel")
    INSTAGRAM_URL = os.getenv("INSTAGRAM_URL", "https://instagram.com/yourbrand")

    # Giveaway
    SPONSOR_CHANNELS = os.getenv("SPONSOR_CHANNELS", "@yourSponsor1,@yourSponsor2")

    # Calendar
    CALENDAR_API_KEY = os.getenv("CALENDAR_API_KEY", "")

settings = Settings()
