
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

‏TOKEN = HTTP API:
8682561865:AAGhR0mcDvKVnY7xRL5fXKKbxKYXLUksvGo


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 البوت شغال داخل القروب")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 إشارة تجريبية: شراء SPX عند 5120\nTP: 5150\nSL: 5100")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📰 أخبار السوق: السوق متذبذب اليوم مع ترقب بيانات اقتصادية")

async def alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔔 تنبيه: حركة قوية في السوق تم رصدها")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))
app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("alert", alert))

print("Bot is running...")
app.run_polling()
