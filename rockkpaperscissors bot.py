import telebot
import conf
import time
from telebot import types
from random import randint


bot = telebot.TeleBot(conf.TOKEN)

users_answers = {}   #dictionary for the answers users send



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hey! I am a bot for the "Rock, Paper, Scissors" game! Type /play to start!')

@bot.message_handler(commands=['play'])
def play(message):
    answer = ''
    win_cond = ''
    # создаем клавиатуру
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    # добавляем на нее три кнопки
    button1 = types.KeyboardButton(text="Rock")
    button2 = types.KeyboardButton(text="Paper")
    button3 = types.KeyboardButton(text="Scissors")
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)

    bot.send_message(message.chat.id, "Let's start! Make a choice!", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def make_a_guess(message):
    if message.text == 'Rock' or message.text == 'Paper' or message.text == 'Scissors':

        bots_answer_num = randint(1, 3)  # getting a random answer for the bots choice
        if bots_answer_num == 1:
            bots_answer = 'Rock'
        elif bots_answer_num == 2:
            bots_answer = 'Paper'
        elif bots_answer_num == 3:
            bots_answer = 'Scissors'

        if message.text == 'Rock':
            answer = 'Rock'
            win_cond = 'Scissors'  # win-condition = the choice bot has to make to lose
            bot.send_message(message.chat.id, "Rock! Nice choice! Let's have a look at mine!")
        if message.text == 'Paper':
            answer = 'Paper'
            win_cond = 'Rock'
            bot.send_message(message.chat.id, "Paper! Nice choice! Let's have a look at mine!")
        if message.text == 'Scissors':
            answer = 'Scissors'
            win_cond = 'Paper'
            bot.send_message(message.chat.id, "Scissors! Nice choice! Let's have a look at mine!")

        if bots_answer == win_cond:  # giving user a result
            result = 'You won! Congratulations!'
        elif bots_answer == answer:
            result = 'Draw! We are still friends!'
        else:
            result = 'You lost! Better luck next time!'

        time.sleep(1)# ИНТРИЖКАААААА
        bot.send_message(message.chat.id, '1...')

        time.sleep(1)  # ИНТРИЖКАААААА
        bot.send_message(message.chat.id, '2...')

        time.sleep(1)  # ИНТРИЖКАААААА
        bot.send_message(message.chat.id, '3...')


        bot.send_message(message.chat.id, f'My choice is... {bots_answer}! {result}')

        time.sleep(2)
        bot.send_message(message.chat.id, 'To play again, type /play')
    else:
        bot.send_message(message.chat.id, "Unknown command! Type /start to play!")


bot.polling(none_stop=True)