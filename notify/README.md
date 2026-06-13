# 通知モジュール - Slack連携

**担当** ：API.テスト
**役割** ：Slack Webhook実装・通知システム

## Webhook設定手順

1. Slack Workspace にログイン
2. 「Incoming Webhook」を検索・追加
3. 通知を送るチャンネルを選択
4. Webhook URL をコピー
5. `config.py` の `SLACK_WEBHOOK_URL` に貼り付け

## 実装方法

- `requests` ライブラリで Webhook URL に POST
- result 辞書を受け取り、Slack に通知

## カスタマイズ例

- 顔画像を添付する
- リッチテキスト（Markdown）で整形
- リアクション絵文字を追加