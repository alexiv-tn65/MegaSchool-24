import os
from enum import Enum

from llama_cpp import Llama
from telegram import Update, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ChatAction
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, Application, \
    CallbackQueryHandler, CallbackContext

BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    print("Error: set the BOT_TOKEN environment variable!")
    exit(1)

MODEL_PATH = os.getenv("MODEL_PATH")
if not MODEL_PATH or not os.path.isfile(MODEL_PATH):
    print("Error: set the MODEL_PATH environment variable!")
    exit(1)

ll_model = Llama(model_path=MODEL_PATH)

def save_chat(user_id, chat_in, chat_out) -> None:
    chat_history = ""
    if user_id not in user_db:
        user_db[user_id] = {}

    try:
        chat_history = user_db[user_id]["history"]
    except KeyError:
        pass

    chat_history = f"{chat_history} {chat_in} {chat_out}"
    if len(chat_history) > context_len:
        chat_history = chat_history[-context_len:]

    user_db[user_id]["history"] = chat_history

def get_history(user_id):
    try:
        return user_db[user_id]["history"]
    except KeyError as e:
        print(e)
        pass

    return ""


def clear_history(user_id):
    try:
        user_db[user_id]["history"] = ""
    except KeyError as e:
        print(e)
        pass


def set_mode(user_id, mode):
    if user_id not in user_db:
        user_db[user_id] = {}

    try:
        user_db[user_id]["chat_mode"] = mode
    except KeyError as e:
        print(e)
        pass


def get_mode(user_id):
    try:
        return user_db[user_id]["chat_mode"]
    except KeyError as e:
        print(e)
        pass

    return Mode.TEXT


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"/start called by user={update.message.chat_id}")
    clear_history(update.message.chat_id)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}.\
     I\'m Alpha\'s language assistant.. Choose: ')


async def new_chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"/new_chat called by user={update.message.chat_id}")
    clear_history(update.message.chat_id)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}. \
    I\'m Alpha\'s language assistant.\Please ask me questions. ')


async def start_text_chat(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    set_mode(query.message.chat_id, Mode.TEXT)
    await query.answer()
    await query.message.reply_text('Text chat enabled')


async def create_response(prompt, temp_msg, context):
    chat_out = ""
    try:
        tokens = ll_model.create_completion(prompt, max_tokens=240, top_p=1, stop=["</s>"], stream=True)
        resp = []
        for token in tokens:
            tok = token["choices"][0]["text"]
            if not token["choices"][0]["finish_reason"]:
                resp.append(tok)
                chat_out = ''.join(resp)
                try:
                    await context.bot.editMessageText(text=chat_out, chat_id=temp_msg.chat_id,
                                                      message_id=temp_msg.message_id)
                except Exception as e:
                    print(e)
                    pass

        if not resp:
            print("Empty generation")
            await context.bot.editMessageText(text='Error, try again',
                                              chat_id=temp_msg.chat_id, message_id=temp_msg.message_id)
    except Exception as e:
        print(f"Unexpected error: {e}")
        await context.bot.editMessageText(text='Sorry, unexpected error, try again',
                                          chat_id=temp_msg.chat_id, message_id=temp_msg.message_id)
        pass
    return chat_out

# process the user's message
async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_history = get_history(update.message.chat_id)

    chat_in = update.message.text
    chat_id = update.message.chat_id
    print(f"user={chat_id}, chat: {chat_in}")

    await update.message.chat.send_action(action=ChatAction.TYPING)

    prompt = TEMPLATE.format(chat_in=chat_in, chat_history=chat_history)
    print(f"user={chat_id}, prompt: {prompt}")

    # create_response
    temp = await update.message.reply_text("...")
    chat_out = await create_response(prompt, temp_msg=temp, context=context)

    save_chat(chat_id, chat_in, chat_out)
    print(f"user={chat_id}, response: {chat_out}")


async def chat_initialization(application: Application):
    await application.bot.set_my_commands([
        BotCommand("/new_chat", "Start new chat"),
    ])
    print("Bot commands added")


def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Text Chat', callback_data='text')]]
    return InlineKeyboardMarkup(keyboard)


if __name__ == '__main__':

    # Сreating an application
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .concurrent_updates(4)
        .post_init(chat_initialization)
        .read_timeout(60)
        .write_timeout(60)
        .build()
    )

    # handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("new_chat", new_chat))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), process_message))
    app.add_handler(CallbackQueryHandler(start_text_chat, pattern='text'))

    print("Bot is starting")

    app.run_polling()
