import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler

TOKEN = "8947513136:AAHsQ0czojsOJ8tNHEQ6nTuRQr4imlllgvc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send me a video link from YouTube, Facebook, Instagram or TikTok 🎥"
    )

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = update.message.text

    msg = await update.message.reply_text("Downloading... ⏳")

    try:

        ydl_opts = {
            "outtmpl": "video.%(ext)s",
            "format": "mp4",
            "noplaylist": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        await update.message.reply_video(
            video=open(filename, "rb"),
            caption="Downloaded Successfully ✅"
        )

        os.remove(filename)

        await msg.delete()

    except Exception as e:
        await update.message.reply_text(f"Error ❌\n{e}")

def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, download)
    )

    print("Bot Running...")

    app.run_polling()

if __name__ == "__main__":
    main()