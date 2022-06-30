from cgitb import text
from itertools import product
from flask import Flask, request, abort
import os
import Replay
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('GMs6Tk96xQY4mxFbMB/DDgzwIphmIBuxaVrtEAdhdA+efTcRsYKeLseoIlTsab9/aEDaEGKLJgUlo9fohNT9dFILA6MwRtxe0t5j19BbR/4IiJoKgFMf+GXWtXVIyYFb0G/ReGkKlvYbLqQvxTLyDwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4b0e8e639bef445d9c9a9497573741cc')
line_bot_api.push_message('U4a4203a9016e01ae9310c692a606d2ed', TextSendMessage(text='BOT啟動成功'))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#當使用者發送訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #取得使用者的訊息
    message = event.message.text

    if(message == "早安"):
        Replay.reply(event,message)
        #line_bot_api.reply_message(
        #        event.reply_token,
        #        TextSendMessage(event.message.text + "創造者"))

if __name__ == "__main__":
    app.run()
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port,debug=True)