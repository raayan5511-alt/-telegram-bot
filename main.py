import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

# 👇 هذا الأمر يطلع لك القروب ID
async def getid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"📌 Chat ID هو:\n{chat_id}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("getid", getid))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
