# hw/led_controller.py
# 担当: HW
# 役割: GPIO経由でLEDを制御する

import time
import threading
from config import LED_PIN, LED_DURATION, LED_FREQUENCY

# ラズパイ以外の環境でもテストできるようにする
try:
    import RPi.GPIO as GPIO
    IS_RASPBERRY_PI = True
except ImportError:
    print("⚠️ RPi.GPIOが見つかりません。ダミーモードで起動します。")
    IS_RASPBERRY_PI = False


# GPIO初期化
def setup():
    if IS_RASPBERRY_PI:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)
        GPIO.output(LED_PIN, GPIO.LOW)
    print("✅ LED初期化完了")


# 点滅フラグ（スレッド間で共有）
_blinking = False


# LEDを点滅させる（別スレッドで実行）
def led_blink(duration=LED_DURATION, frequency=LED_FREQUENCY):
    global _blinking
    _blinking = True

    def blink_loop():
        global _blinking
        interval = 1 / (frequency * 2)
        end_time = time.time() + duration

        print(f"💡 LED点滅開始 ({frequency}Hz, {duration}秒)")

        while _blinking and time.time() < end_time:
            if IS_RASPBERRY_PI:
                GPIO.output(LED_PIN, GPIO.HIGH)
            else:
                print("LED: ON ")

            time.sleep(interval)

            if IS_RASPBERRY_PI:
                GPIO.output(LED_PIN, GPIO.LOW)
            else:
                print("LED: OFF")

            time.sleep(interval)

        _blinking = False
        print("💡 LED点滅終了")

    # メインループをブロックしないように別スレッドで実行
    thread = threading.Thread(target=blink_loop)
    thread.daemon = True
    thread.start()


# LEDを強制停止
def led_stop():
    global _blinking
    _blinking = False
    if IS_RASPBERRY_PI:
        GPIO.output(LED_PIN, GPIO.LOW)
    print("⏹️ LED強制停止")


# 終了時のGPIO後始末
def cleanup():
    led_stop()
    if IS_RASPBERRY_PI:
        GPIO.cleanup()
    print("🧹 GPIO後始末完了")