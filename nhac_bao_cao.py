import os
import time
import requests
from datetime import datetime, timezone, timedelta

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
GOOGLE_SHEET_URL = os.environ["GOOGLE_SHEET_URL"]

DEADLINE = "17:30"

vn_time = datetime.now(timezone(timedelta(hours=7)))
today = vn_time.strftime("%d/%m/%Y")

message = f"""
📋 *VIẾT BÁO CÁO NGÀY HÔM NAY ĐI ĐỒ KHỐN*

🗓 Date: {today}
⏰ Dead Time: {DEADLINE}

🔗 Mở Google Sheet.
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "Markdown",
    "reply_markup": {
        "inline_keyboard": [
            [
                {
                    "text": "📄 Open this Sheet",
                    "url": GOOGLE_SHEET_URL
                }
            ]
        ]
    }
}

success = False

for attempt in range(1, 4):
    print(f"Attempt {attempt}/3")

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=30
        )

        print(response.status_code)
        print(response.text)

        if response.status_code == 200:
            success = True
            print("Telegram message sent successfully")
            break

    except Exception as e:
        print(f"Error: {e}")

    if attempt < 3:
        print("Retry after 10 seconds...")
        time.sleep(10)

if not success:
    raise Exception("Failed to send Telegram message after 3 attempts")
