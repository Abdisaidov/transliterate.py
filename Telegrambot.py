#transliterate.py dan funksiyan chaqirib olib krilldan lotinga, lotindan krillga o'tkazish uchun algoritmlarni yozamiz.

from transliterate import to_cyrillic, to_latin
import telebot 
TOKEN = '6265818363:AAHmjOQfqoZRQIDXclzMpN3vKWvTuPfucLk'
bot = telebot.TeleBot(TOKEN, parse_mode=None) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum va rohmatulloh. Xush kelibsiz!"
    javob += "\n\nBu bot sizning matnlaringizni криллдан-lotinga, lotindan-криллга o'zgaritirib beradi."
    javob += "\n\n Diqqat! Bot faqat tekst shaklidagi xabarlarga javob beradi, emoji va stikerlarga bot javob bermasligi yoki noto'g'ri javob berishi mumkin."
    javob += "\n\nMurojaat va qo'shimcha takliflar uchun @saidov0911 bilan bog'lanishingiz mumkin."
    javob += "\n\nMatnni kiriting:"
    bot.reply_to(message, javob)
	
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg= message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))
     
bot.polling() 
