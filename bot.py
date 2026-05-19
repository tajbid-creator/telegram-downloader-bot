from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📥 Download", callback_data="download")],
        [InlineKeyboardButton("ℹ️ Help", callback_data="help")],
        [InlineKeyboardButton("⚙️ About", callback_data="about")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to your Advanced Bot!\n\nChoose an option below:",
        reply_markup=reply_markup
    )

# button handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "download":
        await query.edit_message_text("📥 Send me a link to download (feature coming next 🚀)")
    
    elif query.data == "help":
        await query.edit_message_text(
            "ℹ️ Help Menu:\n\n/start - Open menu\n/help - Help info\n/about - About bot"
        )

    elif query.data == "about":
        await query.edit_message_text(
            "🤖 Advanced Telegram Bot\nCreated with Python + Railway 🚀"
        )

# /help command
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Use /start to open menu.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(CallbackQueryHandler(button_handler))

app.run_polling()