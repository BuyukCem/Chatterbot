from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

english_bot = ChatBot("ChatBotName", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

train_list = ['Hello, who can help you',
              'I would like to buy a movie ticket.',
              'Ok, for what movie?',
              'Monty python and the holy Grail',
              'ok we have taken your request into account']

list_trainer = ListTrainer(english_bot)
list_trainer.train(train_list)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
