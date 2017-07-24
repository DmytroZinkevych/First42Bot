import telebot
import random
import secrets
from telebot import types
from datetime import datetime

token = "REPLACE_IT_WITH_A_TOKEN_OF_THE_BOT"
bot = telebot.TeleBot(token)

print("Бот запустився... Поїхали!")


error_message = "You entered incorrect data.\nTry another command or see /help for more info."

welcome_message =   "*Welcome to First42Bot!*\n\nHere is the list of commands:\n\n" + \
                    "/average - Get an average value of entered numbers\n" + \
                    "/coin - Flip a coin\n" + \
                    "/dice - Roll the dice\n" + \
                    "/randint - Get a random integer from the specified interval\n\n" + \
                    "/help - Get help"

help_message =  "*Commands:*\n\n" + \
                "/average - *Get an average value of entered numbers*\n" + \
                "Just enter as much numbers as you want. " + \
                "Numbers are real and should be separated by only one space. You shouldn't specify their amount.\n" + \
                "\n/coin - *Gives result of flipping a coin*\n\n" + \
                "/dice - *Gives result of rolling two dices*\n\n" + \
                "/randint - *Get a random integer from the specified interval*\n" + \
                "You should write two integers which define an interval (and are included into it). " + \
                "First is a minimum and second is a maximum desirable number. " + \
                "Second number should be greater than first.\n\n" + \
                "/help - *Get help*"


randint_mode = False
average_mode = False


markup = types.ReplyKeyboardMarkup(True)
markup.row('/coin', '/average')
markup.row('/dice', '/randint')
markup.row('/help')
hide_markup = types.ReplyKeyboardRemove()


def cancel_all():
    global randint_mode, average_mode
    randint_mode = False
    average_mode = False


def find_average(message):
    nums = message.text.split(' ')
    n = len(nums)
    if n < 1:
        bot.send_message(message.chat.id, error_message, reply_markup=markup)
        return
    summary = 0
    for num in nums:
        try:
            num = num.replace(',', '.')
            summary += float(num)
        except ValueError:
            bot.send_message(message.chat.id, error_message)
            return
    bot.send_message(message.chat.id, "Average = " + str(summary / n), reply_markup=markup)


def find_randint(message):
    nums = message.text.split(' ')
    n = len(nums)
    if n < 2:
        bot.send_message(message.chat.id, error_message, reply_markup=markup)
        return
    for i in range(n):
        nums[i] = nums[i].replace(',', '.')
        if not nums[i].isnumeric():
            bot.send_message(message.chat.id, error_message, reply_markup=markup)
            return
        nums[i] = int(nums[i])
    if nums[0] >= nums[1]:
        bot.send_message(message.chat.id, error_message, reply_markup=markup)
        return
    d = 0 - nums[0]
    r = secrets.randbelow(nums[1] + d + 1)
    r -= d
    bot.send_message(message.chat.id, "Random integer = " + str(r), reply_markup=markup)


# --------------------------- Command handlers ----------------------------------

@bot.message_handler(commands=['average'])
def average_activate(message):
    global average_mode
    cancel_all()
    average_mode = True
    bot.send_message(message.chat.id, "Enter numbers (separated by 1 space):", reply_markup=hide_markup)


@bot.message_handler(commands=['coin'])
def trow_coin(message):
    cancel_all()
    sides = ['Heads', 'Tails']
    random.seed(datetime.now().microsecond)
    bot.send_message(message.chat.id, random.choice(sides), reply_markup=markup)


@bot.message_handler(commands=['dice'])
def trow_dice(message):
    cancel_all()
    now = datetime.now()
    random.seed((now.microsecond ** now.second) // now.minute)
    a = random.randrange(1, 7)
    b = secrets.randbelow(6) + 1
    bot.send_message(message.chat.id, str(a) + ' ' + str(b), reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_handle(message):
    cancel_all()
    bot.send_message(message.chat.id, help_message, parse_mode='Markdown', reply_markup=markup)


@bot.message_handler(commands=['randint'])
def randint_activate(message):
    global randint_mode
    cancel_all()
    randint_mode = True
    bot.send_message(message.chat.id, "Enter minimal and maximal possible integers (separated by 1 space):", reply_markup=hide_markup)


@bot.message_handler(commands=['start'])
def com_handle(message):
    cancel_all()
    bot.send_message(message.chat.id, welcome_message, parse_mode='Markdown', reply_markup=markup)

# --------------------------- Command handlers ----------------------------------


@bot.message_handler(content_types=["text"])
def active_command(message):
    global average_mode, randint_mode

    if average_mode:
        find_average(message)
    elif randint_mode:
        find_randint(message)
    else:
        bot.send_message(message.chat.id, "I didn't catch that...\nTry another command or see /help for more info.", reply_markup=markup)

    cancel_all()


if __name__ == '__main__':
    bot.polling(none_stop=True)
