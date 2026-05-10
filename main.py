from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os
TOKEN = os.getenv("8682561865:AAGhR0mcDvKVnY7xRL5fXKKbxKYXLUksvGo")

# 👇 حط رقم حسابك في تيليجرام (User ID)
ADMIN_ID = 123456789

# ===== أوامر القروب =====
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📰 أخبار السوق: متابعة حركة السوق العالمية اليوم")

async def alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔔 تنبيه: حركة قوية في السوق تم رصدها")

# ===== أوامر خاصة لك فقط =====
async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ غير مصرح لك")
        return

    msg = " ".join(context.args)
    await update.message.reply_text(f"📨 تم الإرسال للقروب: {msg}")

# ===== تشغيل البوت =====
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("alert", alert))
app.add_handler(CommandHandler("send", 
