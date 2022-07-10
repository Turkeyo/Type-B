from audioop import add
from cgitb import text
#from itertools import product
#from pipes import Template
from flask import Flask, request, abort
import os
import re #判斷接收訊息
import randomChoice #隨機選擇圖片function
import time

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

#Channel access token
line_bot_api = LineBotApi('GMs6Tk96xQY4mxFbMB/DDgzwIphmIBuxaVrtEAdhdA+efTcRsYKeLseoIlTsab9/aEDaEGKLJgUlo9fohNT9dFILA6MwRtxe0t5j19BbR/4IiJoKgFMf+GXWtXVIyYFb0G/ReGkKlvYbLqQvxTLyDwdB04t89/1O/w1cDnyilFU=')
#Channel secret
handler = WebhookHandler('4b0e8e639bef445d9c9a9497573741cc')
#Development line id
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

#When user send message 當使用者發送訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #Get user message 取得使用者的訊息
    message = event.message.text
    reply(event,message)

#Judgment message content 判斷接收訊息
def reply(event,message):
    #If have "買卡" Words In the content
    if "抽卡" in message:
        buttons_template_message = TemplateSendMessage(
            alt_text="卡包選項",  #Not display on the reply message
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        #Display image
                        thumbnail_image_url="https://i.imgur.com/UnDldbZ.jpg",
                        #Message Title
                        title = "柴犬卡包",
                        #Message
                        text = "卡包",
                        actions = [
                            MessageAction(
                                label = "單抽",  #選擇項目
                                text = "柴犬抽1張"),    #使用者輸出
                            MessageAction(
                                label = "10連抽",
                                text = "柴犬抽10張"),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url="https://img.ruten.com.tw/s1/0/cf/1b/21917125126939_602.JPG",
                        title = message + "資訊",
                        text = "遊戲王卡包",
                        actions = [
                            MessageAction(
                                label = "普通卡",
                                text = "10包"),
                            MessageAction(
                                label = "豪華卡",
                                text = "100包"),
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    if(re.match("柴犬抽1張",message)):
        imgTitle,imgSrc = ""
        imgTitle = randomChoice.cho.choicetitle(imgTitle)
        imgSrc = randomChoice.cho.choicesrc(imgSrc)
        image_message = ImageSendMessage(
            #設定原圖
            original_content_url=imgSrc,
            #設定預覽圖
            preview_image_url = "https://gss0.baidu.com/-Po3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/0b7b02087bf40ad1b1aab867502c11dfa8ecceec.jpg"
        )
        line_bot_api.reply_message(
            event.reply_token,[TextSendMessage(text = imgTitle)]
        )
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
    elif(re.match("斗肉",message)):
        image_message = ImageSendMessage(
            #設定原圖
            original_content_url="https://gss0.baidu.com/-Po3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/86d6277f9e2f0708d3880a95e124b899a801f292.jpg",
            #設定預覽圖
            preview_image_url="https://i.imgur.com/qxWF0Ehh.jpg"
        )
        #傳送地圖訊息
        #line_bot_api.reply_message(
        #        event.reply_token,
        #        TextSendMessage("猛斯塔卡豆"))
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
    elif(re.match("Fan",message)):
        button_template_message = TemplateSendMessage(
            alt_text="你知道這是什麼嗎?",
            template=CarouselTemplate(
                coulums=[
                    CarouselColumn(
                        thumbnail_image_url="https://chenchenhouse.com//wp-content/uploads/2020/10/%E5%9C%96%E7%89%871-2.png",
                        title= "英文天才",
                        text = "Fan之Q",
                        actions=[
                            MessageAction( 
                                label= " 個股資訊",
                                text= "個股資訊"),
                            MessageAction( 
                                label= " 個股新聞",
                                text= "個股新聞")
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(
            event.reply_token, button_template_message
            )

if __name__ == "__main__":
    app.run()
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port,debug=True)
