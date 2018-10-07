import telegram
from telegram.ext import Updater, CommandHandler, BaseFilter, MessageHandler, Filters
from time import sleep
from quotescript import getQuotes
import random as rand

token_bot = # put authentication token here
update_id = None

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hi. Number of quotes is %d. Write /help for info.', 146)           

def helpu(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='How to quiz: \n /qq quiz - to get a quote \n /qq guess - to write a gues \n /qq ga - to get the answer if you cannot figure it out')

def startQuiz(bot, update, args):
    if args[0] == 'quiz': 
        rand_var = rand.randint(0,146)
        print(rand_var)
        global  answer_from_pool
        quote_from_pool, answer_from_pool = getQuotes(rand_var)
        bot.send_message(chat_id=update.message.chat_id, text=quote_from_pool)
    elif args[0] == 'ga':
        bot.send_message(chat_id=update.message.chat_id, text='The answer is:')
        print(answer_from_pool)
        bot.send_message(chat_id=update.message.chat_id, text=answer_from_pool)
    else:
        input_length = len(args)
        input = " ".join(args)
        input2 = input.lower()
        answer_reworked = answer_from_pool.replace(',', '')
        answer_reworked2 = answer_reworked.lower()
        split_answer = answer_reworked2.split()
        print(split_answer)
        print(input2)
        check_mark = 0
        input_tf = False
        for i in range(0, len(split_answer)):
            if len(split_answer) < 2:
                if split_answer[i] in input2:
                    check_mark = 1;
                    bot.send_message(chat_id=update.message.chat_id, text='Correct! The answer is: \n')
                    bot.send_message(chat_id=update.message.chat_id, text=answer_from_pool)
                    input_tf = True
                    break
            else:
                if split_answer[i] in input2:
                    check_mark = check_mark +1;
                    if check_mark >= 2:
                        bot.send_message(chat_id=update.message.chat_id, text='Correct! The answer is: \n')
                        bot.send_message(chat_id=update.message.chat_id, text=answer_from_pool)
                        input_tf = True
                        break
        if input_tf == False:
            bot.send_message(chat_id=update.message.chat_id, text='Wrong, guess again.')


def main():
    bot = telegram.Bot(token=token_bot)
    updater = Updater(token=token_bot)
    dispatcher = updater.dispatcher

    #start_handler = CommandHandler('hej', start)
    #dispatcher.add_handler(start_handler)

    
    helpu_handler = CommandHandler('help', helpu)
    dispatcher.add_handler(helpu_handler)

    start_quiz_handler = CommandHandler('qq', startQuiz, pass_args=True)
    dispatcher.add_handler(start_quiz_handler)
    
    while True:
        try:
            updater.start_polling()
        except Exception:
            time.sleep(2)
            

    updater.idle()


if __name__ == '__main__':
    main()
