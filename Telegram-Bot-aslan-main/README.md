# VIP Telegram Bot (Aslan)

A production-ready Persian/RTL Telegram bot for VIP trading memberships, giveaways, and admin web panel. Deploys on Render via Docker.

## Quick Start
1) Put these files in your GitHub repo `Telegram-Bot-aslan`.
2) On Render: New Web Service → connect the repo. Render auto-detects `render.yaml`.
3) In Render → Environment, set:
   - BOT_TOKEN (from BotFather; rotate if exposed)
   - BASE_URL (Render URL, e.g., https://telegram-vip-bot.onrender.com)
   - ADMIN_PASSWORD_HASH (Argon2id hash of your admin password)
   - PAYMENT vars (Zarinpal or Crypto)
4) Redeploy. Then `/start` in Telegram.

### Generate Argon2 hash (locally)
```bash
python - << 'PY'
from argon2 import PasswordHasher
ph = PasswordHasher()
print(ph.hash("cvhwkesx10A"))
PY
```
Copy the output into `ADMIN_PASSWORD_HASH` env var.
