from flask import Flask, render_template, redirect, request, session, g, url_for
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import botDb as BD

app = Flask(__name__) 
english_bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("./data/data.json")
app.secret_key = BD.si

@app.route("/")
def index():
     return render_template("index.html")

@app.route("/get", methods=['GET','POST'])
def get_bot_response():
     userText = request.args.get("msg")
     return str(english_bot.get_response(userText))

if __name__ == "__main__":
     app.run(debug = True)
