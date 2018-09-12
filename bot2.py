from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from api_key import key

import ephem, logging
import datetime as dt

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot2.log'
                    )

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def planet_in_constellation(bot, update):
    date = dt.datetime.now().strftime('%Y/%m/%d')
    user_planet_str = update.message.text.split(' ')[1]
    user_planet_str = user_planet_str[0].upper() + user_planet_str[1:]
    try:
        user_planet = getattr(ephem, user_planet_str)
        user_planet = user_planet(date)
        user_constellation = ephem.constellation(user_planet)

        answer = 'Планета {} сегодня находится в созвездии {}'.format(user_planet_str, user_constellation[1])
        print(answer)
        update.message.reply_text(answer)
    except AttributeError:
        print('Сударь, вы несете какую-то дичь!')
        update.message.reply_text('Сударь, вы несете какую-то дичь!')



def main():
    mybot = Updater(key, request_kwargs=PROXY)


    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_in_constellation))


    mybot.start_polling()
    mybot.idle()

main()
