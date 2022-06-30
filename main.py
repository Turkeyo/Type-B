from audioop import add
from cgitb import text
from itertools import product
from flask import Flask, request, abort
import os
import re #判斷接收訊息

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage,LocationSendMessage
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
    reply(event,message)

def reply(event,message):
    #判斷接收訊息
    if(re.match("早安",message)):
        line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(event.message.text))
    elif(re.match("Duck不必",message)):
        #貼圖編號網站https://developers.line.biz/en/docs/messaging-api/sticker-list/#sticker-definitions
        #設定貼圖
        sticker_message = StickerSendMessage(
                package_id='789',
                sticker_id='10855'
        )
        #傳送貼圖訊息
        line_bot_api.reply_message(
            event.reply_token,sticker_message
        )
    elif(re.match("Where are you")):
        location_message = LocationSendMessage(
            title= "你知道這是什麼嗎?",
            address= "亞馬遜雨林",
            #座標經緯度
            latitude= -3.465240904243103,
            longitude=  -62.215848348909105
        )
        #傳送地圖訊息
        line_bot_api.reply_message(
            event.reply_token,location_message
        )
if __name__ == "__main__":
    app.run()
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port,debug=True)
