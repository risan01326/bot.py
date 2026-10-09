import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# আপনার টোকেনটি সরাসরি এখানে বসানো হলো
TOKEN = '8705234961:AAGNXOW6I-jPS-ukGNPRgENtTZ9ncN2Jfv4'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ARIYAN BD Bot Active! ইউজার মেসেজ ফরওয়ার্ড করুন।")

async def get_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.forward_from:
        user = update.message.forward_from
        info = f"👤 **User Found!**\n\n🆔 ID: `{user.id}`\n📛 Name: {user.first_name} {user.last_name or ''}\n🔗 Username: @{user.username or 'N/A'}\n🤖 Is Bot: {user.is_bot}"
        await update.message.reply_text(info, parse_mode='Markdown')
    else:
        await update.message.reply_text("অনুগ্রহ করে ওই ইউজারের একটি মেসেজ আমাকে ফরওয়ার্ড করুন।")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.FORWARDED, get_info))
    print("Bot is running...")
    application.run_polling()