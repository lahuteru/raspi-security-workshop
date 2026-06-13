# main.py
# 担当: API・テスト
# 役割: 全モジュールを繋ぐメインループ

import cv2
from config import CAMERA_INDEX

from ai.face_recognition  import recognize_face, load_known_faces
from hw.led_controller    import setup, led_blink, cleanup
from logger.event_logger  import EventLogger
from notify.slack_notify  import notify_slack


def main():
    # 初期化
    known_db = load_known_faces()
    logger   = EventLogger()
    setup()

    cap = cv2.VideoCapture(CAMERA_INDEX)
    print("🎥 カメラ起動 - 顔認識を開始します")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("⚠️ カメラ映像を取得できません")
                break

            # ① 顔認識（AIリード）
            result = recognize_face(frame, known_db)

            if result:
                print(f"👤 検知: {result['status']} / {result['name']}")

                # ② ログ記録（メンバーC）
                logger.log_event(result)

                # ③ 不審者なら通知 + LED点滅
                if result["status"] == "unknown":
                    notify_slack(result)              # PM(あなた)
                    led_blink(duration=5, frequency=20)  # HWリード

    except KeyboardInterrupt:
        print("\n🛑 終了します")

    finally:
        cap.release()
        cleanup()


if __name__ == "__main__":
    main()