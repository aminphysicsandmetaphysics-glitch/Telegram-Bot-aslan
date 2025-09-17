import datetime as dt
import httpx
from .utils import fa_date

async def fetch_today_events(api_key: str) -> list[dict]:
    if not api_key:
        return []
    # Placeholder. Replace with real provider.
    base_url = "https://api.example.com/economic-calendar"
    today = dt.date.today().isoformat()
    params = {"date": today, "importance": "medium,high"}
    headers = {"Authorization": f"Bearer {api_key}"}
    async with httpx.AsyncClient(timeout=15) as client:
        r = await client.get(base_url, params=params, headers=headers)
        data = r.json() if r.status_code == 200 else {}
    events = []
    for e in data.get("events", []):
        events.append({
            "time": e.get("time", ""),
            "country": e.get("country", ""),
            "event": e.get("title", ""),
            "actual": e.get("actual", ""),
            "forecast": e.get("forecast", ""),
            "previous": e.get("previous", ""),
        })
    return events

def render_events_fa(events: list[dict]) -> str:
    if not events:
        return ""
    lines = [f"🗓 رویدادهای اقتصادی امروز ({fa_date()}):\n"]
    for e in events[:12]:
        lines.append(
            f"• {e['time']} — {e['country']} — {e['event']}"
            + (f" | Actual: {e['actual']}" if e['actual'] else "")
            + (f" | Forecast: {e['forecast']}" if e['forecast'] else "")
            + (f" | Prev: {e['previous']}" if e['previous'] else "")
        )
    return "\n".join(lines)
