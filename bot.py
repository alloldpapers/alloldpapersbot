import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8400705202:AAENgsxS7uqsHmMDOxeaaI9mKwuv7viVklY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("RPSC 1st Grade", callback_data="rpsc")
    markup.add(btn1)

    bot.send_message(message.chat.id,
                     "📚 Welcome to All Old Papers Bot\n\nSelect Exam:",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == "rpsc":
        markup = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton("Political Science", callback_data="polsci")
        markup.add(btn1)

        bot.edit_message_text("Select Subject:",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=markup)

    elif call.data == "polsci":
        markup = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton("2018 Paper", url="https://example.com/2018.pdf")
        btn2 = InlineKeyboardButton("2020 Paper", url="https://example.com/2020.pdf")
        btn3 = InlineKeyboardButton("2022 Paper", url="https://example.com/2022.pdf")
        btn4 = InlineKeyboardButton("2023 Paper", url="https://example.com/2023.pdf")

        markup.add(btn1, btn2)
        markup.add(btn3, btn4)

        bot.edit_message_text("Select Year:",
                              call.message.chat.id,
                              call.message.message_id,
                              reply_markup=markup)


bot.infinity_polling()
