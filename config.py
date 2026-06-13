# config.py
# 全員共通の設定ファイル
# ここを変えるときは必ずメンバーに連絡すること

# Slack
#ダミーです。実際には自分のワークスペースのWebhook URLを入れてください。
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/xxx/yyy/zzz"

# 顔認識
FACE_THRESHOLD = 0.6       # 不審者判定の閾値（0〜1）
CAMERA_INDEX   = 0         # カメラのデバイス番号

# LED
LED_PIN        = 17        # GPIO ピン番号
LED_DURATION   = 5         # 点滅する秒数
LED_FREQUENCY  = 20        # 1秒間の点滅回数（Hz）

# ログ
LOG_DIR        = "./logs"  # ログの保存先