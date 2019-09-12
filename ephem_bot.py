"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TOKEN
from settings import PROXY
from datetime import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def send_planet_constellation(bot, update):
    user_text= update.message.text
    #try to get planet name from text
    try:
        planet_name = user_text.split()[1]
        #create planet instance
        planet = getattr(ephem,planet_name)()
    except (AttributeError, IndexError):
        update.message.reply_text("Try another planet.")
    
    planet.compute(datetime.now())
    constellation = ephem.constellation(planet)[1]
    update.message.reply_text(f'{planet_name} in {constellation} today.')


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main(token, proxy):
    mybot = Updater(token, request_kwargs=proxy)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", send_planet_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main(TOKEN,PROXY)
