from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8682561865:AAGhR0mcDvKVnY7xRL5fXKKbxKYXLUksvGo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 البوت شغال داخل القروب")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE)
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📰 أخبار السوق: ترقب بيانات اقتصادية")

async def alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔔 تنبيه: حركة قوية في السوق")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))
app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("alert", alert))

print("Bot running...")
app.run_polling()
