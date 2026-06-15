import os
import requests
from datetime import datetime, timezone, timedelta

BOT_TOKEN = os.environ["8562579660:AAFBMGhaCsThpAvY5Jp0Gt0E0yXoe6xk6q0"]
CHAT_ID = os.environ["-5180038890"]
GOOGLE_SHEET_URL = os.environ["https://docs.google.com/spreadsheets/d/1r-INxnpXdFqqTSkzcUFumThF2mLi6HkY-iOiiKalF2Y/edit?gid=677493022#gid=677493022"]

DEADLINE = "17:30"

vn_time = datetime.now(timezone(timedelta(hours=7)))
today = vn_time.strftime("%d/%m/%Y")

message = f"""
📋 *VIẾT BÁO CÁO NGÀY HÔM NAY ĐI ĐỒ KHỐN*

🗓 Datey: {today}
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

response = requests.post(url, json=payload)
print(response.status_code)
print(response.text)
