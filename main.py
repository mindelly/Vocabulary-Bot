import telebot
import get_word
import config


bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    
    hello_button = telebot.types.InlineKeyboardMarkup()
    random_word_button = telebot.types.InlineKeyboardButton(text='📚 Random word, please!', callback_data='random')


    hello_button.add(random_word_button)

    bot.reply_to(message, 
    "This is the English dictionary bot. \n \
    I can help you with improving your vocabulary by sending you word definitions \n \
    from Oxford dictionary! (The list of the 5000 most popular words for an each level) \n \
    You can choose options below to start learning",
                                reply_markup = hello_button)
    


@bot.callback_query_handler(func = lambda call: True)
def answer_button(call):

    if call.data == 'random':
        all_data = get_word.pick_word(call.data)
        def_ex = all_data[0]
        word = all_data[1]
        level = all_data[2]
        word_class = all_data[3]

        text_message = f'{word} {level} {word_class} \n'

        for i in list(def_ex.keys()):
            text_message += i + '\n'
            for j in def_ex[i]:
                text_message += '*' + j + '\n'
        
    bot.send_message(call.message.chat.id, text_message)



                     


bot.infinity_polling()