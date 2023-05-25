import random
import telebot

bot = telebot.TeleBot("5926594127:AAHXx34PBlMnMFVha-LsCqFGcg9Mm-g1Nfg", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name= message.from_user.first_name
    bot.reply_to(message, "Hello "+ user_name +", welcome")

@bot.message_handler(commands=['game'])
def guess_number(message):
    computer_number=random.randint(10,40)

    while True:

        # t=bot.send_message(message.chat.id,"guess the number:")
        user_number= message.from_user

        if computer_number==user_number:
            print("you win")
            print("👏")
            break

        elif computer_number>user_number:
            print("boro bala")
            print("")

        elif computer_number<user_number:
            print("bia paeen")
            print("")



bot.infinity_polling()