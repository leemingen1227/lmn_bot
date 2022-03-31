# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('0wVkfDMGnf1DV1zdj4HcKy59Iua0Xrtdov23X0itf0i6ViAUP6zDU5akEsgUU8AMGmoUkHNsjrwRI7Z3WEwexRvLqpvPO5zhO1VhrDwP3PGEblt4o4AaE8CbiEUR9aYfo1jLEsMS1wc1vDZdkagQUAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6382fdd65cc543cd0da0e26942f920ca')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()