import logging
from typing import Dict

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

import ping

# 텔레그램 토큰 파일 위치
token_file = '.telegram_token'
try:
    with open(token_file, 'r') as file:
        TELEGRAM_BOT_TOKEN = file.read().strip()

except FileNotFoundError:
    print(f"Error: The file '{token_file}' does not exist.")
    exit(1)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [
    ["Ping"],
    ["Done"]
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Start the conversation and ask user for input."""
    await update.message.reply_text(
        "What do you want?",
        reply_markup=markup,
    )
    return CHOOSING


async def handle_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Ask the user for info about the selected predefined choice."""
    command = update.message.text

    if command == "Ping":
        context.user_data['cmd'] = command
        await update.message.reply_text(f"Please input the host to ping.")
        return TYPING_REPLY
    else:
        await update.message.reply_text(f"I don't know what you want.")
        return CHOOSING


async def handle_ping_request(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handle ping request and respond with the result."""
    if context.user_data.get('cmd') == "Ping":
        host = update.message.text
        await update.message.reply_text(
            f"Start checking ping for {host}..."
        )

        ping_result = ping.check(host)  # Assumes ping.check returns a string result

        await update.message.reply_text(
            f"{ping_result}\nPlease input another host to ping or type 'Done' to finish.",
            reply_markup=markup,
        )
    else:
        await update.message.reply_text(
            f"Unexpected error occurred.",
            reply_markup=markup,
        )

    return TYPING_REPLY


async def done_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Display the gathered info and end the conversation."""
    await update.message.reply_text(
        "Command finished.",
        reply_markup=ReplyKeyboardRemove(),
    )

    context.user_data.clear()
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("cmd", start_command)],
        states={
            CHOOSING: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")), handle_choice
                )
            ],
            TYPING_REPLY: [
                MessageHandler(
                    filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")),
                    handle_ping_request,
                )
            ],
        },
        fallbacks=[MessageHandler(filters.Regex("^Done$"), done_command)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

