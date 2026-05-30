import requests
import time

API_URL = "https://shopgmail9999.com/api/BuyGmail/GetstockGmail?apikey=183ac98abf6442e18d405d5dc233b793&id=1"
NTFY_TOPIC = "gmail-stock-9999"   # ← THAY BẰNG TÊN TOPIC CỦA BẠN
INTERVAL = 30

print("🚀 Bắt đầu monitor stock Gmail 10 Phút trên Render")

last_stock = 0

while True:
    try:
        r = requests.get(API_URL, timeout=10)
        stock = r.json().get("data", {}).get("stock", 0)

        if stock > 0 and last_stock <= 0:
            message = f"""✅ STOCK ĐÃ CÓ HÀNG!
Gmail 10 Phút - VERIFY ACC GAME
Stock hiện tại: {stock}
⏰ {time.strftime("%H:%M:%S %d/%m/%Y")}"""

            requests.post(
                f"https://ntfy.sh/{NTFY_TOPIC}",
                headers={
                    "Title": "🔥 Gmail Stock Alert!",
                    "Priority": "high",
                    "Tags": "rocket,mail"
                },
                data=message
            )
            print(f"✅ ĐÃ GỬI NTFY - Stock = {stock}")

        else:
            print(f"📦 Stock hiện tại: {stock}")

        if stock == 0:
            last_stock = 0  # reset để lần sau stock tăng lại thì báo
        else:
            last_stock = stock

    except Exception as e:
        print("❌ Lỗi:", e)

    time.sleep(INTERVAL)