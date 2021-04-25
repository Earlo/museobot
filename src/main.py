#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.

"""Simple inline keyboard bot with multiple CallbackQueryHandlers.

This Bot uses the Updater class to handle the bot.
First, a few callback functions are defined as callback query handler. Then, those functions are
passed to the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot that uses inline keyboard that has multiple CallbackQueryHandlers arranged in a
ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line to stop the bot.
"""
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    CallbackContext,
)

from messages import WELCOME, QUESTION


from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.museobot
users = db.users
answers = db.answers
state = db.state

users.create_index("telegram_chat_id", unique=True)


from questions import QDict

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def getState():
    if len(list(state.find())) == 0:
        state.insert_one({
            "current_question": None,
        }).inserted_id
    return list(state.find())[0]

def getOptionText(options):
    i = 0
    r = ''
    for o in options:
        i += 1
        r += f'{i}: {o}\n'
    return r

def getQuestionText(question):
    q = QDict[question]
    options = q.options
    return QUESTION.format(q=q.text) + getOptionText(list(options.values()))

def getQuestionKeyboard(question):
    q = QDict[question]
    options = q.options
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(num, callback_data=name) for num, name in enumerate(options.keys(), start=1)
        ]
    ])

def setState(question_id):
    state.update_one({}, {'$set': {'current_question': question_id}})

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("")
    # jobs
    j = updater.job_queue
    getState()


    def sendMessage(update: Update, context: CallbackContext) -> None:
        if (update['message']['chat']['id'] == 96171182):
            try:
                text = ' '.join(update['message']['text'].split(' ')[1:])
                for c in users.find():
                    try:
                        context.bot.send_message(c['telegram_chat_id'], text, parse_mode="HTML")
                    except:
                        logger.info("User %s is missing. ID %s", c['telegram_chat_id'], update['message']['chat']['id'])
            except:
                update.message.reply_text(f"ei oo tollasta kyssärii :D, on vaan {list(QDict.keys())}")
        else:
            update.message.reply_text(f"Juu ei")


    def sendQuestion(update: Update, context: CallbackContext) -> None:
        if (update['message']['chat']['id'] == 96171182):
            try:
                key = update['message']['text'].split(' ')[1]
                text = getQuestionText(key)
                keyboard = getQuestionKeyboard(key)
                setState(key)
                for c in users.find():
                    chatId = c['telegram_chat_id']
                    try:
                        context.bot.send_message(chatId, text, parse_mode="HTML", reply_markup=keyboard)
                    except:
                        logger.info("User %s is missing. ID %s", chatId, update['message']['chat']['id'])

            except:
                update.message.reply_text(f"ei oo tollasta kyssärii :D, on vaan {list(QDict.keys())}")
        else:
            update.message.reply_text(f"Juu ei")

    def answer(update: Update, context: CallbackContext) -> None:
        """Show new choice of buttons"""
        query = update.callback_query
        query.answer()
        chatID = str( query.message.chat.id )
        currentQuestionId = getState()['current_question']
        key, _ = query.data.split("_")
        if currentQuestionId == key:
            currentQuestion = QDict[currentQuestionId]
            if db.answers.count_documents({'telegram_chat_id': chatID, "question": currentQuestionId}) == 0:
                answers.insert_one({
                    "telegram_chat_id": chatID,
                    "question": currentQuestionId,
                    "response": query.data,
                })
                if (query.data == currentQuestion.correct):
                    users.update_one(
                        {"telegram_chat_id": chatID},
                        {'$inc': {'score': 1}}
                    )
                text = getQuestionText(key) + f'\nVastasit {currentQuestion.options[query.data]}'
                query.edit_message_text(
                    text=text
                )
            else:
                query.edit_message_text(
                    text=f"Olit jo vastannut tähän kysymykseen"
                )
        else:
            query.edit_message_text(
                text=f"Kysymyksen vastausaika on umpeutunut"
            )


    def start(update: Update, context: CallbackContext) -> None:
        """Send message on `/start`."""
        user = update.message.from_user
        logger.info("User %s started the conversation. ID %s", user.first_name, update['message']['chat']['id'])
        try:
            users.insert_one({
                "telegram_chat_id": str( update.message.chat_id ),
                "score": 0,
            }).inserted_id
            update.message.reply_text(WELCOME)
        except:
            update.message.reply_text("Pingikset lens sinnekin :D")
        # j.run_once(once, 30)
        # Tell ConversationHandler that we're in state `FIRST` now
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("info", start))
    dispatcher.add_handler(CommandHandler("sendQuestion", sendQuestion))
    dispatcher.add_handler(CommandHandler("sendMessage", sendMessage))

    dispatcher.add_handler(CallbackQueryHandler(answer, pattern='^.*$'),)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
