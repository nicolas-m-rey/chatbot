# imports
from flask import Flask, render_template, request
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

# create ChatBot
chatbot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# app routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get")
# function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()
