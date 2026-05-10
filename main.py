
import os
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("8682561865:AAGhR0mcDvKVnY7xRL5fXKKbxKYXLUksvGo")

# 👤 حط رقمك في تيليجرام
ADMIN_ID = 123456789

# 🛡️ منع سبام بسيط
user_last_time = {}

def anti_spam(user_id):
    now = time.time()
    if user_id in user_last_time:
        if now - user_last_time[user_id] < 5:
            return False
    user_last_time[user_id] = now
    return True

# 🚀 تشغيل البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 البوت شغال: أخبار + تنبيهات")

# 📰 أخبار السوق الأمريكي
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not anti_spam(update.effective_user.id):
        return
    await update.message.reply_text(
        "📰 أخبار السوق الأمريكي: متابعة بيانات الاقتصاد وتأثيرها على الأسواق اليوم"
    )

# 🔔 تنبيهات عامة
async def alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not anti_spam(update.effective_user.id):
        return
    await update.message.reply_text("🔔 تنبيه: تحركات قوية في الأسواق العالمية حالياً")

# 💬 رسالة خاصة من الأدمن
async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ غير مصرح لك")
        return

    msg = " ".join(context.args)
    if not msg:
        await update.message.reply_text("اكتب رسالة بعد الأمر")
        return

    await update.message.reply_text(f"📨 {msg}")

# ===== تشغيل البوت =====
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("alert", alert))
    app.add_handler(CommandHandler("send", send))

    app.run_polling()

if __name__ == "__main__":
    main()
