from audioop import add
from cgitb import text
#from itertools import product
#from pipes import Template
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
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage,LocationSendMessage,ImageSendMessage,VideoSendMessage,AudioSendMessage,TemplateSendMessage,CarouselTemplate,MessageAction,CarouselColumn
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
    elif(re.match("Where are you",message)):
        location_message = LocationSendMessage(
            title= "你知道這是什麼嗎?",
            address= "亞馬遜雨林",
            #座標經緯度
            latitude= -3.465085760983781,
            longitude=  -62.215912686683325
        )
        #傳送地圖訊息
        line_bot_api.reply_message(
            event.reply_token,location_message
        )
    elif(re.match("不可以色色",message)):
        image_message = ImageSendMessage(
            #設定原圖
            original_content_url="https://i.imgur.com/UnDldbZ.jpg",
            #設定預覽圖
            preview_image_url="https://i.imgur.com/qxWF0Ehh.jpg"
        )
        #傳送地圖訊息
        line_bot_api.reply_message(
            event.reply_token,image_message
        )
    elif(re.match("喵",message)):
        video_message = VideoSendMessage(
            #設定影片連結
            original_content_url="https://media.giphy.com/media/QMHoU66sBXqqLqYvGO/giphy.gif",
            preview_image_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.Q0HpYXqb_UAG1tIoue99-QHaEo%26pid%3DApi&f=1"
        )
        #傳送影片訊息
        line_bot_api.reply_message(
            event.reply_token,video_message
        )
    elif(re.match("Hanabira",message)):
        audio_message = AudioSendMessage(
            #設定音效檔
            original_content_url="https://b.ppy.sh/preview/332280.mp3",
            duration=30000
        )
        #傳送音效訊息
        line_bot_api.reply_message(
            event.reply_token,audio_message
        )
    if"Fan" in message:
        button_template_message = TemplateSendMessage(
            alt_text="你知道這是什麼嗎?",
            template=CarouselTemplate(
                coulums=[
                    CarouselColumn(
                        thumbnail_image_url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIF.ZhiK%252f%252fqNUBAX7pfX4%252fr9nw%26pid%3DApi&f=1",
                        title= "message" + "英文天才",
                        text = "Fan之Q",
                        actions = [
                            MessageAction(
                                label = message[3:] + "英文課程",
                                text = "英文課程資訊" + message[3:],
                            ),
                            MessageAction(
                                label = message[3:] + "發音課程",
                                text = "發音課程資訊" + message[3:],
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(
            event.reply_token,button_template_message
        )

if __name__ == "__main__":
    app.run()
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port,debug=True)
