# Raspberry Pi セキュリティシステム

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 プロジェクト概要

顔認識 × Slack通知 × LED爆速点滅を組み合わせたIoTセキュリティシステム。

訪問者の顔を自動認識して誰が来たかを判定し、Slackで通知します。  
不審者の場合は、遠隔からラズパイのLEDを爆速点滅させて威嚇します。

## 🎯 プロジェクト規模

- **チーム規模** ：4人
- **開発期間** ：4週間
- **主要技術** ：Python、OpenCV、mediapipe、Raspberry Pi GPIO、Slack API

## 👥 チーム構成

| 役割 | 担当 | 主な業務 |
|------|------|--------|
| **画像AI** | メンバーA | 顔認識・判定ロジック |
| **HW** | メンバーB | ラズパイセットアップ・LED制御 |
| **通知&ログ** | メンバーC | イベント記録・ログシステム |
| **API・テスト** | メンバーD | Slack連携・統合テスト |

## 🛠️ 技術スタック

- **言語** ：Python 3.9+
- **画像処理** ：OpenCV、mediapipe
- **ハードウェア** ：Raspberry Pi 4、カメラモジュール、LED
- **API** ：Slack Messaging Webhook
- **バージョン管理** ：Git/GitHub

## 📦 セットアップ

### 必要な環境

- Raspberry Pi 4（4GB）
- Raspberry Pi Camera Module または USB Webcam
- LED × 1
- 抵抗、トランジスタなど電子部品
- Python 3.9+

### インストール手順

```bash
# リポジトリをクローン
git clone https://github.com/xx/raspi-security-workshop.git
cd raspi-security-workshop

# 仮想環境を作成
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存ライブラリをインストール
pip install -r requirements.txt

# タイムゾーンを設定（ラズパイのみ）
sudo timedatectl set-timezone Asia/Tokyo
```

### 実行方法

```bash
python3 main.py
```

## 📖 ドキュメント

- [インターフェース仕様書](./INTERFACE.md) - モジュール間の契約書
- [AIリード](./ai/README.md) - 顔認識実装ガイド
- [HWリード](./hw/README.md) - ハードウェアセットアップガイド
- [ロギング](./logger/README.md) - ログシステム
- [Slack通知](./notify/README.md) - 通知システム

## 🎓 学んだこと

- ✅ マルチモジュール開発設計
- ✅ チームでのインターフェース設計
- ✅ IoT × Web API × AI の統合実装
- ✅ リアルタイムシステムの開発
- ✅ チーム開発でのコミュニケーション
