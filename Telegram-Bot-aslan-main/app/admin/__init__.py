 deps.py            # احراز هویت ادمین (JWT/Cookie)
    views.py           # روت‌های پنل (HTML)
    templates/
      base.html
      login.html
      dashboard.html
      users_list.html
      subscriptions.html
      payments.html
      signals.html
      vip_results.html
      giveaways.html
      giveaway_tasks_partial.html
      settings.html
      health.html
    static/
      admin.css
      admin.js
  db.py                # Session/engine
  models.py            # SQLAlchemy models (users/payments/... + جدیدها)
  schemas.py           # Pydantic (فرم‌ها)
  services/            # منطق دامنه (payments, giveaways, signals...)
  main.py
