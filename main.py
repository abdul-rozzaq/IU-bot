############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################


from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler



keyboard = ReplyKeyboardMarkup([
    ['Hozirda qaysi universitetlarga qabul ochiq'],
    ['Tarjima va topshirish narxi'],
], resize_keyboard=True)


 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name} \nMen <a href="https://t.me/islomiyuniversitetlar">Islomiy Universitetlar kanali</a> ning telegram botiman\n\nPastdagi tugmalar orqali savollaringizga javob olishingiz mumkin', parse_mode='HTML', reply_markup=keyboard)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    
async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('xx')
    await update.message.reply_text(f'Yangi habar')

print("Bot started ...")

app = ApplicationBuilder().token("6474695276:AAEl9r8WsiMNgu--ac_tKvn0sZj9W3Nz8KE").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message))


app.run_polling()