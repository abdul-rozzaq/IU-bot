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
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler, ConversationHandler
from asgiref.sync import sync_to_async

from config import TOKEN 

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

app = ApplicationBuilder().token(TOKEN).build()


main_buttons = ReplyKeyboardMarkup([
    ['📑 Universitetlar haqida ma\'lumot'],
    ['🖇 Savol Javob'],
    ['📬 Xizmatlar'],
    ['👨🏼‍💻 Admin bilan bog\'lanish'],
], resize_keyboard=True) 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   
    await createUser(update.effective_user)
    
    await update.message.reply_text(f'Assalomu alaykum {update.effective_user.first_name} \nMen <a href="https://t.me/islomiyuniversitetlar">Islomiy Universitetlar kanali</a> ning telegram botiman \n\nPastdagi tugmalar orqali savollaringizga javob olishingiz mumkin', 
        parse_mode='HTML', 
        reply_markup=main_buttons
    )


    

## Conversation

async def enter(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    buttons = await getButtons()
    await update.message.reply_text('Siz Savol Javob bo\'limidasiz \n\nOrtga qaytish uchun /cancel buyrug\'ini bosing.', reply_markup=buttons, parse_mode='HTML')
    
    
    return 0

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    answer = await getAnswer(update.message.text) 
    buttons = await getButtons()

    await update.message.reply_text(answer, reply_markup=buttons, parse_mode='HTML')
  
async def quit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Siz asosiy menyudasiz', reply_markup=main_buttons, parse_mode='HTML')
    
    return ConversationHandler.END

################################
## DB
################################


@sync_to_async
def getButtons():
    
    qs = Question.objects.all()
    
    buttons = [ [x.title] for x in qs ]
    
    buttons.append(['🔝 Asosiy menyu'])
    
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
    
    
app.add_handler(CommandHandler("start", start))

conv_handler = ConversationHandler(
    entry_points=[
        MessageHandler(filters.Regex(r'(🖇 Savol Javob)'), enter)
    ],
    # 🖇 Savol Javob
    states={
        0: [MessageHandler(filters.Regex(r'(🔝 Asosiy menyu)'), quit), CommandHandler('cancel', quit), MessageHandler(filters.TEXT, message), ]
    },
    fallbacks=[]
)
app.add_handler(conv_handler)

app.run_polling()