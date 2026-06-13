# logger/event_logger.py
# 担当: メンバーC
# 役割: 顔認識イベントをCSVに記録し、顔画像を保存する

import csv
import cv2
from datetime import datetime
from pathlib import Path
from config import LOG_DIR


class EventLogger:
    def __init__(self):
        self.log_dir  = Path(LOG_DIR)
        self.face_dir = self.log_dir / "faces"
        self.csv_path = self.log_dir / "events.csv"

        # ディレクトリ作成
        self.log_dir.mkdir(exist_ok=True)
        self.face_dir.mkdir(exist_ok=True)

        # CSVのヘッダーを書く（初回のみ）
        if not self.csv_path.exists():
            with open(self.csv_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=[
                    "timestamp", "status", "name",
                    "confidence", "image_path"
                ])
                writer.writeheader()

        print(" ロガー初期化完了")


    def log_event(self, result):
        if result is None:
            return

        # 顔画像を保存
        image_path = ""
        if result["face_image"] is not None:
            filename   = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
            image_path = str(self.face_dir / filename)
            cv2.imwrite(image_path, result["face_image"])

        # CSVに記録
        with open(self.csv_path, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "timestamp", "status", "name",
                "confidence", "image_path"
            ])
            writer.writerow({
                "timestamp" : result["timestamp"],
                "status"    : result["status"],
                "name"      : result["name"] or "",
                "confidence": result["confidence"],
                "image_path": image_path
            })

        print(f"ログ記録: {result['status']} ({result['timestamp']})")