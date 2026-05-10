import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 البوت شغال")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📰 أخبار عامة")

async def alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔔 تنبيه: يوجد تحديثات جديدة")

def main():
    if not TOKEN:
        raise ValueError("TOKEN is missing in environment variables")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("alert", alert))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
