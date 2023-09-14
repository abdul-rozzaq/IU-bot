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
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################


from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, User as tgUser
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler
from asgiref.sync import sync_to_async


app = ApplicationBuilder().token("1936491324:AAEsOVflNJ0PVvEqCZkTiKk8btKaDw_WLsU").build()

 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    buttons = await getButtons()
    
    await createUser(update.effective_user)
    
    await update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name} \nMen <a href="https://t.me/islomiyuniversitetlar">Islomiy Universitetlar kanali</a> ning telegram botiman \n\nPastdagi tugmalar orqali savollaringizga javob olishingiz mumkin', 
        parse_mode='HTML', 
        reply_markup=buttons
    )


    
async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answer = await getAnswer(update.message.text) 
    buttons = await getButtons()

    await update.message.reply_text(answer, reply_markup=buttons, parse_mode='HTML')


################################
## DB
################################


@sync_to_async
def getButtons():
    
    qs = Question.objects.all()
    
    buttons = [ [x.title] for x in qs ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

@sync_to_async
def getAnswer(question: str) -> str:
        
    qs = Question.objects.filter(title=question)
    
    if qs.exists():
        
        return qs[0].answer
    
    return '<b>☹️ Nimadur xato ketdi.</b> \n\nBotni ishga tushurish uchun /start ni bosing.'

@sync_to_async
def createUser(user: tgUser):
    
    qs = User.objects.filter(telegram_id=user.id)
    print('user checking ...')
    if not qs.exists():
        User.objects.create(
            username=user.username, 
            first_name=user.first_name, 
            last_name=user.last_name, 
            telegram_id=user.id
        )
    
    
    


print("Bot started ...")

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, message))

app.run_polling()