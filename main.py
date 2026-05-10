import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

# ===== start command =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 البوت شغال ويستقبل الأوامر")

# ===== اختبار بسيط =====
async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ البوت يرد طبيعي")

def main():
    if not TOKEN:
        raise ValueError("TOKEN missing")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
