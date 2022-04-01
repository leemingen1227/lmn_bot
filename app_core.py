from __future__ import unicode_literals
import os
from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent

import configparser

from custom_models import utils, PhoebeTalks, PhoebeFlex

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 幫 "你-APP-的名字.herokuapp.com" 做一個家
@app.route("/")
def home():
    return render_template("home.html")


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

# 紀錄資料
@handler.add(MessageEvent, message=TextMessage)
def reply_text_message(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        reply = False
        
        if not reply:
            reply = PhoebeTalks.insert_record(event)
        
        if not reply:
            reply = PhoebeFlex.img_search_flex(event)
                    
        if not reply:
            reply = PhoebeTalks.img_search(event)
                    
        if not reply:
            reply = PhoebeTalks.pretty_echo(event)
            

if __name__ == "__main__":
    app.run()