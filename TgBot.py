import telebot
from telebot import types

questions = [
    {"question": "Какого цвета холодильник: ",
     "answers": ["белый", "черный", "синий"],
     "correct": 1},
    {"question": "МОП в стойло?",
     "answers": ["да", "нет"],
     "correct": 0},
    {"question": "Сколько задач из дз-4 по дискре вы решили ?",
     "answers": ["недостаточно", "мало", "не все"],
     "correct": 2},
]

user_data = {}

with open('token.txt', 'r') as file:
    token = file.read().replace('\n', '')


bot = telebot.TeleBot(token)

# СТАРТУУУЕМ !!!!!!!!!!
@bot.message_handler(commands=['start'])
def start_quiz(message):
    user_data[message.chat.id] = {"score": 0, "question_number": 0}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Начать викторину!"))
    bot.send_message(message.chat.id, f'Привет, {message.from_user.username}! Готов пройти викторину?', reply_markup=markup)


# Начало викторины
@bot.message_handler(func = lambda message: message.text == 'Начать викторину!')
def ask_question(message):
    chat_id = message.chat.id
    qnumber = user_data[chat_id]["question_number"]

    if qnumber < len(questions):
        question = questions[qnumber]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        for answer in question["answers"]:
            markup.add(types.KeyboardButton(answer))

        bot.send_message(chat_id, question["question"], reply_markup=markup)

    else:
        show_result(message) # это будет описано позже в коде :)


# Стартуем заново
@bot.message_handler(func = lambda message: message.text == 'Начать заново!')
def restart_quiz(message):
    user_data[message.chat.id] = {"score": 0, "question_number": 0}
    ask_question(message)


# Проверка ответа
@bot.message_handler(func = lambda message: True)
def answer_check(message):
    chat_id = message.chat.id
    qnumber = user_data[chat_id]["question_number"]

    if qnumber < len(questions):
        user_answer = message.text
        question = questions[qnumber]

        if user_answer in question["answers"]:
            correct_answer = question["answers"][question["correct"]]

            if user_answer == correct_answer:
                user_data[chat_id]["score"] += 1

            user_data[chat_id]["question_number"] += 1
            ask_question(message)
        else:
            bot.send_message(chat_id, "Выберите один из вариантов ответа!")
    else:
        show_result(message)


# Показать результат
def show_result(message):
    chat_id = message.chat.id
    score = user_data[chat_id]["score"]

    bot.send_message(chat_id, f'Поздравляю, ваш результат: {score} из {len(questions)}')

    bot.send_photo(chat_id, 'https://pouch.jumpshare.com/preview/sPccPYATwjcfaHknGRPxsHFCUaxJKWDRQjn70osS_-CEyLau1AL9xAP79WDhwQG61ajejlReetA1ZvEiHswrI_k_3ZbqpPRYDU7SYKSgNo8')

    user_data[chat_id]["question_number"] = 0
    user_data[chat_id]["score"] = 0

    # Сюда же воткнем кнопка начать заново
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Начать заново!"))
    bot.send_message(chat_id, "Хотите попробовать еще раз?", reply_markup=markup)



bot.infinity_polling(timeout = 10, long_polling_timeout=5)
