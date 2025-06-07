
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = "7354495730:AAEdzs7ILmJWv0P3qnAizz6ErP55epoJlMk"
WEBAPP_URL = "https://shihabmollah07.github.io/telegram-mini-board/"

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 বোর্ড খুলুন", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("নিচের বোতামটি চাপুন আপনার বোর্ড খুলতে:", reply_markup=reply_markup)

# Receiver for data sent from the Mini App
async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.web_app_data:
        data = update.message.web_app_data.data
        await update.message.reply_text(f"📦 আপনি পাঠালেন:\n{data}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
