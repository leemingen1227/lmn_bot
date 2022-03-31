# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('oebgIrvI9iac0gsZ+sRQK+ie9EnIVzNY66chS44ETv1gaJ7EWe1+qHocuJweQ0zaGmoUkHNsjrwRI7Z3WEwexRvLqpvPO5zhO1VhrDwP3PFecLENJE2I4S31lX0RKWEYxDHv1wK3+c0i5tOFvuP8eQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('df2a8349efb22b83aeda68b34034a2ab')

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