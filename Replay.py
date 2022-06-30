from cgitb import text
from itertools import product
from flask import Flask, request, abort
import os
from main import line_bot_api,handler

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

def reply(event,message):
    if(message == "早安"):
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(event.message.text + "創造者"))

if __name__ == "__main__":
    app.run()
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port,debug=True)