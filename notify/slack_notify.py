# notify/slack_notify.py
# 担当: API・テスト
# 役割: 不審者検知時にSlackへ通知する

import requests
from config import SLACK_WEBHOOK_URL


# インターフェース仕様書に準拠した関数
def notify_slack(result):
    if result is None:
        return

    message = (
        f"🚨 *不審者を検知しました！*\n"
        f"時刻: {result['timestamp']}\n"
        f"信頼度: {result['confidence']}\n"
        f"→ LED爆速点滅で威嚇中..."
    )

    response = requests.post(
        SLACK_WEBHOOK_URL,
        json={"text": message}
    )

    if response.status_code == 200:
        print("✅ Slack通知送信完了")
    else:
        print(f"⚠️ Slack通知失敗: {response.status_code}")