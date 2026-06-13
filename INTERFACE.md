# インターフェース仕様書

**最終更新：2025-06-13**  
**担当：メンバーで編集

---

## 📦 データ形式（AIリード → 全員共通）

AIリードの `recognize_face()` が返す辞書の形式。  
全員がこの形式を前提にコードを書くこと。

```python
result = {
    "status"    : "known" or "unknown",
    "name"      : "Tanaka" or None,
    "confidence": 0.91,
    "timestamp" : "2025-01-15 14:30:45",
    "face_image": np.array(...)
}
```

| キー名 | 型 | 内容 | 例 |
|--------|-----|------|------|
| status | str | "known" か "unknown" のみ | "unknown" |
| name | str/None | 既知なら名前、未知はNone | "Tanaka" or None |
| confidence | float | 信頼度 0.0〜1.0 | 0.91 |
| timestamp | str | "YYYY-MM-DD HH:MM:SS"形式 | "2025-01-15 14:30:45" |
| face_image | ndarray | 顔部分のnumpy配列 | np.array(...) |

---

## 🔌 関数一覧

| 誰が作る | 関数名 | 引数 | やること |
|---------|--------|------|---------|
| AIリード | recognize_face(frame) | カメラ映像 | 顔認識して result を返す |
| HWリード | led_blink(duration, frequency) | 秒数, Hz | LED点滅開始 |
| HWリード | led_stop() | なし | LED停止 |
| メンバーC | log_event(result) | result辞書 | ログ記録 |
| PM(あなた) | notify_slack(result) | result辞書 | Slack通知 |

---

## 🔄 メインの流れ

メインループはAPI・テストが管理する。

```python
result = recognize_face(frame)      # ① 画像AI
log_event(result)                   # ② 通知・ログ

if result["status"] == "unknown":
    notify_slack(result)            # ③ API・テスト
    led_blink(duration=5, frequency=20)  # ④ HW
```

---

## ⚠️ ルール

- 関数名・引数は勝手に変えない
- 変更したいときはメンバーに一言連絡
- この仕様を変更する場合は必ず全員に通知

## 変更履歴

| 日付 | 変更内容 | 担当者 |
|------|---------|--------|
| 2025-06-13 | 初版作成 | メンバーＤ |