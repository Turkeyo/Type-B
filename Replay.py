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