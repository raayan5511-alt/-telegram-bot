import os
import requests
from telegram.ext import ApplicationBuilder, ContextTypes

# ===== إعدادات =====
TOKEN = os.getenv("TOKEN")
NEWS_API = os.getenv("NEWS_API_KEY")

CHAT_ID = -1002593594346

# ===== كلمات الأخبار المهمة =====
KEYWORDS = [
    "fed", "inflation", "cpi", "interest rate",
    "nasdaq", "sp500", "stock market",
    "recession", "gdp", "unemployment"
]

# ===== جلب الأخبار =====
def fetch_news():
    url = (
        "https://newsapi.org/v2/top-headlines?"
        "category=business&language=en&apiKey=" + NEWS_API
    )
    res = requests.get(url).json()
    return res.get("articles", [])

# ===== فلترة الأخبار =====
def is_important(title):
    title = title.lower()
    return any(word in title for word in KEYWORDS)

# ===== تجهيز الرسالة =====
def build_message(articles):
    messages = []

    for a in articles:
        title = a.get("title", "")
        if is_important(title):
            messages.append(f"🔥 {title}")

    if not messages:
        return None

    return "🚨 أخبار مهمة للسوق الأمريكي:\n\n" + "\n".join(messages[:5])

# ===== الإرسال التلقائي =====
async def send_news(context: ContextTypes.DEFAULT_TYPE):
    articles = fetch_news()
    message = build_message(articles)

    if message:
        await context.bot.send_message(
            chat_id=CHAT_ID,
            text=message
        )

# ===== التشغيل =====
def main():
    if not TOKEN:
        raise ValueError("TOKEN missing")
    if not NEWS_API:
        raise ValueError("NEWS_API_KEY missing")

    app = ApplicationBuilder().token(TOKEN).build()

    # 🔥 كل 60 ثانية
    app.job_queue.run_repeating(send_news, interval=60, first=5)

    print("🔥 Real-time news bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
