from flask import Flask, request, abort

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

line_bot_api = LineBotApi('yOaQQsJbnkxelO5SSOVZYJVAM+Fzom6dF/cgyJsYjlvl7PIz3BM9ODcJJlvhhm9zaEDaEGKLJgUlo9fohNT9dFILA6MwRtxe0t5j19BbR/7UgAZVHv5L5+GpTUueIoxOHc9Kd4Xg1ICr3k05+fBE1gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4e802ae6d8938982b9662aec5f81630d')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()