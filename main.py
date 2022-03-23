from telegram import Update, ForceReply, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, Defaults

import logging

TOKEN = "5170179293:AAE-eWbnGnkCQHkwLct0ChcLUGXgKiMlddE"

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    a = update
    b = context
    text = f"<code>{update.message.text}</code>"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def photo_or_video(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text('You sent a photo or you sent a video')

def forwarded_photo_or_video(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text('*You sent a photo or you sent a video*', parse_mode='Markdown')

def audio(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text('You sent an audio')

def url(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text('A message consists of an url')

def main() -> None:
    defaults = Defaults(parse_mode=ParseMode.HTML)
    updater = Updater(TOKEN, defaults=defaults)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.add_handler(MessageHandler(Filters.photo | Filters.video, photo_or_video))
    dispatcher.add_handler(MessageHandler(Filters.audio, audio))
    dispatcher.add_handler(MessageHandler(Filters.forwarded, forwarded_photo_or_video))
    dispatcher.add_handler(MessageHandler(Filters.entity("url"), url))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()