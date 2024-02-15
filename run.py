import os
from enum import Enum
import tempfile
from pathlib import Path


from telegram.constants import ChatAction, ParseMode
from telegram import Update, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, Application, \
    CallbackQueryHandler, CallbackContext
from llama_cpp import Llama

BOT_TOKEN = os.getenv("BOT_TOKEN")