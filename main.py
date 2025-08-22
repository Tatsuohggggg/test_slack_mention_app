import os
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.message(re.compile(r"(@管理者|＠管理者|@admin|＠admin|@administrator|＠administrator|@かんりしゃ|＠かんりしゃ)"))
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    text = f"<@U0388TCPGBC> <@U035YK0F2NL> <@U062XV8QYBC> <@U08KUHFG0H4> <@U04K6FCP3H8> <@U0388T44E3D> <@U01BMT22EKS> <@U053DF9MWGJ> <@U03SF0U4HTR> <@U08N4U82U3Y>"
    
    # スレッドに返信する場合
    thread_ts = message.get('thread_ts') or message['ts']  # 既にスレッド内なら thread_ts、そうでなければメッセージ自体の ts
    channel = message['channel']
    
    say(text, thread_ts=thread_ts, channel=channel)

@app.message(re.compile(r"(@エンジニア|＠エンジニア|@engineer|＠engineer|@えんじにあ|＠えんじにあ)"))
def mention_engineer(message, say):
    # エンジニアにメンションする処理を追加
    text = f"<@U0388TCPGBC> <@U035YK0F2NL> <@U062XV8QYBC> <@U08KUHFG0H4> <@U04K6FCP3H8> <@U0388T44E3D> <@U08N4U82U3Y>"
    
    thread_ts = message.get('thread_ts') or message['ts']
    channel = message['channel']
    
    say(text, thread_ts=thread_ts, channel=channel)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()