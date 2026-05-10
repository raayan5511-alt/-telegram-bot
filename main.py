import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8682561865:AAGhR0mcDvKVnY7xRL5fXKKbxKYXLUksvGo")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 البوت شغال")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📰 أخبار السوق الأمريكي")

async def alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔔 تنبيه: حركة في السوق")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("alert", alert))

app.run_polling()
