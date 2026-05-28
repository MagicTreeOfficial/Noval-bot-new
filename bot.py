from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from dotenv import load_dotenv
import os
import random

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

crypto_replies = [
    "Bitcoin looking strong today 🚀",
    "Altcoin season could be near 👀",
    "Always DYOR before aping in.",
    "Bullish momentum detected 📈",
    "Crypto never sleeps 🌙",
    "Memecoins are printing again 😂",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Crypto AI bot is live 🚀")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = random.choice(crypto_replies)
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Crypto bot started 🚀")

app.run_polling()