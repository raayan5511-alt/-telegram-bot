import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ===== إعدادات =====
TOKEN = os.getenv("TOKEN")
NEWS_API = os.getenv("NEWS_API_KEY")

CHAT_ID = -1002593594346

# ===== أخبار السوق =====
def get_news():
    url = (
        "https://newsapi.org/v2/top-headlines?"
        "category=business&language=en&apiKey=" + NEWS_API
    )
    res = requests.get(url).json()
    return res.get("articles", [])

# ===== فلترة الأخبار المهمة =====
def filter_news(articles):
    keywords = [
        "fed", "inflation", "cpi", "interest rate",
        "nasdaq", "sp500", "stock market",
        "recession", "gdp", "unemployment"
    ]

    result = []

    for a in articles:
        title = a.get("title", "").lower()

        if any(k in title for k in keywords):
            result.append("🔥 " + a.get("title", ""))

    return result

# ===== إرسال الأخبار =====
async def send_news(context: ContextTypes.DEFAULT_TYPE):
    articles = get_news()
    news_list = filter_news(articles)

    if news_list:
        message = "🚨 أخبار السوق الأمريكي:\n\n" + "\n".join(news_list[:5])

        await context.bot.send_message(
            chat_id=CHAT_ID,
            text=message
        )

# ===== start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 البوت شغال بنجاح")

# ===== تشغيل البوت =====
def main():
    if not TOKEN or not NEWS_API:
        raise ValueError("Missing TOKEN or NEWS_API_KEY")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    # 🔥 تشغيل تلقائي كل دقيقة
    app.job_queue.run_repeating(send_news, interval=60, first=10)

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
