import random
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

import os
TOKEN = os.environ.get("TOKEN")

# 💖 FULL Sticker Collection (All 17)
STICKERS = [
    "CAACAgUAAxkBAAMvaYww2vkchpSR0qQJ9h-JJHpbvQYAAnsYAAKlOthUOeaE0u2vE_06BA",
    "CAACAgUAAxkBAAMxaYwxP2s07H89DHY_CKzdm5-NaggAArAaAAL1ICBV7zrDsaRevN86BA",
    "CAACAgUAAxkBAAMyaYwxRE7wEGu6IUHTFz5RkknFKSQAAp0cAALqkhlV2Jljg8r6sHU6BA",
    "CAACAgUAAxkBAAMzaYwxRaZI9Pj-uqnApFFSf_7USF0AArQbAAKhgSFV-iV1z-VY2HM6BA",
    "CAACAgUAAxkBAAM0aYwxR5BnmaTg-pSVjh7ZwaBihMIAAg0YAAKe7hhVSXqBHYsTZT06BA",
    "CAACAgUAAxkBAAM1aYwxSDwycvPpJYPOujX68ONEIoUAAvYaAAJ8iRlV5cvXYWoMSws6BA",
    "CAACAgUAAxkBAAM2aYwxSrWqOg7t1Z-rXERYMeg7AUgAAt0ZAAJBLBlVjmuTvQf4lIo6BA",
    "CAACAgUAAxkBAAM3aYwxS3ejXf0mKFtMavqiuhfbAAGPAAJ2GgAC_W4YVQORZqb8BuxsOgQ",
    "CAACAgUAAxkBAAM4aYwxTIZ_5PSfCnILeqGwKxrJeM0AAmQZAALYlSBVl99OzPAEGlA6BA",
    "CAACAgUAAxkBAAM5aYwxTbg8iITS7UWX0kHpUBjrmwMAAoYaAAJOQilVb6uHji-ouYk6BA",
    "CAACAgUAAxkBAAM6aYwxTnpcXCiNu-hZFPcNXFhXSsYAAm4ZAAJMOohVBrXjUI0UAsE6BA",
    "CAACAgUAAxkBAAM7aYwxUBxBub6QIWc4xcfe0UzzxEsAAmsZAAKVS_FVblWgeVNcgEc6BA",
    "CAACAgUAAxkBAAM8aYwxUSj44AmBuDhmoDr212NXK88AAh4aAALN62hXXw5ZMBCEBfc6BA",
    "CAACAgUAAxkBAAM9aYwxUi87hJfoFedMd4pdkmLJN1MAAvoaAALIe9BUI-fb8ZpaUr06BA",
    "CAACAgUAAxkBAAM-aYwxUzud-ej6OR4LoxXO04mrKj0AAlYWAAKb1dhUR3UAAfYNvyi-OgQ",
    "CAACAgUAAxkBAAM_aYwxVbyOWDgXQN7Jg5QD51vxeo0AAvUcAAJN9JFWcafmz8Bwn846BA",
    "CAACAgUAAxkBAANAaYwxVltg5yI6w3R48NDpJd3_sWkAAn4cAAJveMhXb-9L4HK0Wh86BA"
]

# 🎬 Video Notes
START_VIDEO = "DQACAgUAAxkBAANxaYw3KyaMKHgTFXVuAjdpe9VqER4AAgMbAALbN2FUBuwE-jyOb8s6BA"

IMIU_VIDEOS = [
    "DQACAgUAAxkBAANyaYw3ZmjO2s1W5rhLHpVQbNdWLa8AAgQbAALbN2FUJEhr-tgL5H86BA",
    "DQACAgUAAxkBAANzaYw3a_ZPA_MN8j5VAgVw--jh6_0AAgUbAALbN2FUwW0F8tl-Sig6BA",
    "DQACAgUAAxkBAAN0aYw3i4n4AR7yc2Nt9NDjb6g8R1AAAgYbAALbN2FUR0XuxZJjo3k6BA",
    "DQACAgUAAxkBAAN1aYw3ntyX4MKD90QHk1KeT43XJWcAAgcbAALbN2FUnfqzHrilxjs6BA"
]

# 💥 Bye media
BYE_STICKER = "CAACAgIAAxkBAANBaYwxY0vAzA22DjKqd6841BdITxwAAnYNAAJ_H4lK4zCiT0tLmaM6BA"
BYE_VOICE = "AwACAgUAAxkBAANlaYw1ZacVXybuNH4ET__RKgFew0cAAv0aAALbN2FURfjIFlU5__c6BA"

#Wingwing voice
WINGWING_VOICE = "AwACAgUAAxkBAAMCaY2ZISTRbg8jV9Zcpk8PE6eIGcAAAuYZAAKPl3BUUtMZoPw-d6Q6BA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Happy Valentine's Day mi love!!! Chat Yeoh is here 😌💖\n\n"
        "Try:\n"
        "/hi_bao\n"
        "/i_mi_u\n"
        "/i_love_u\n"
        "/bhm\n"
        "/wingwing\n"
        "/bye")

    await context.bot.send_video_note(
        chat_id=update.message.chat_id,
        video_note=START_VIDEO
    )


async def hi_bao(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_reply(update, context,
        "hi bao, i am chat yeoh. your ai bao here to keep u company :)"
    )


async def i_mi_u(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_reply(update, context,
        "i mi u mo!!! MO!!!"
    )

    await context.bot.send_video_note(
        chat_id=update.message.chat_id,
        video_note=random.choice(IMIU_VIDEOS)
    )


async def i_love_u(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_reply(update, context,
        "i love u mosht heheh mua"
    )


async def bhm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_reply(update, context,
        "no BHM!!! but i love you!!! CONFIRMED."
    )
    
async def wingwing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("wingwing triggered")


async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(
        chat_id=update.message.chat_id,
        action="typing"
    )
    await asyncio.sleep(1)

    await update.message.reply_text("BYE LOR.")

    await context.bot.send_sticker(
        chat_id=update.message.chat_id,
        sticker=BYE_STICKER
    )

    await context.bot.send_voice(
        chat_id=update.message.chat_id,
        voice=BYE_VOICE
    )


async def send_reply(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str):
    await context.bot.send_chat_action(
        chat_id=update.message.chat_id,
        action="typing"
    )
    await asyncio.sleep(1)

    await update.message.reply_text(text)

    await context.bot.send_sticker(
        chat_id=update.message.chat_id,
        sticker=random.choice(STICKERS)
    )
async def grab_voice_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.voice:
        await update.message.reply_text(update.message.voice.file_id)


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.VOICE, grab_voice_id))

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hi_bao", hi_bao))
app.add_handler(CommandHandler("i_mi_u", i_mi_u))
app.add_handler(CommandHandler("i_love_u", i_love_u))
app.add_handler(CommandHandler("bhm", bhm))
app.add_handler(CommandHandler("wingwing", wingwing))
app.add_handler(CommandHandler("bye", bye))

print("Chat Yeoh ultimate multimedia mode activated 💖🎥🎙️")

import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")


def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()


if __name__ == "__main__":
    threading.Thread(target=run_dummy_server, daemon=True).start()
    app.run_polling()






