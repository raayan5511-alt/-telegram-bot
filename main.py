import os
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8682561865:AAGhR0mcDvKVnY7xRL5fXKKbxKYXLUksvGo")

# 👤 حط رقمك (لازم)
ADMIN_ID = 123456789

# 🛡️ منع السبام (بسيط)
user_last_time = {}

def anti_spam(user_id):
    now = time.time()
    if user_id in user_last_time:
        if now - user_last_time[user_id] < 5:  # 5 ثواني بين كل أمر
            return False
    user_last_time[user_id] = now
    return True

# 📰 أخبار السوق الأمريكي (ثابتة حالياً - نطورها لاحقاً)
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not anti_spam(update.effective_user.id):
        return
    await update.message.reply_text("📰 أخبار السوق الأمريكي: ترقب بيانات اقتصادية وتأثيرها على الأسواق اليوم")

# 🔔 تنبيهات عامة
async def alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not anti_spam(update.effective_user.id):
        return
    await update.message.reply_text("🔔 تنبيه: حركة قوية في السوق تم رصدها حالياً")

# 💬 أوامر خاصة للأدمن فقط
async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ غير مصرح لك")
        return

    msg = " ".join(context.args)
    if not msg:
        await update.message.reply_text("اكتب الرسالة بعد الأمر")
        return

    await update.message.reply_text(f"📨 تم إرسال: {msg}")

# ❌ إيقاف إشارات أو أوامر (كتم تنبيهات)
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    await update.message.reply_text("⛔ تم إيقاف الأوامر/التنبيهات")

# 🚀 تشغيل تلقائي (رسالة عند بدء البوت)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 البوت شغال: أخبار + تنبيهات + أوامر خاصة")

# ===== تشغيل البوت =====
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("alert", alert))
app.add_handler(CommandHandler("send", send))
app.add_handler(CommandHandler("stop", stop))
