# ai/face_recognition.py
# 担当: 画像AI
# 役割: カメラ映像から顔を検出・認識し、既知/未知を判定する

import cv2
import numpy as np
import pickle
import mediapipe as mp
from datetime import datetime
from config import FACE_THRESHOLD, CAMERA_INDEX


# 既知人物DBの読み込み
def load_known_faces(db_path="ai/known_faces.pkl"):
    try:
        with open(db_path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("⚠️ 既知人物DBが見つかりません。空のDBで起動します。")
        return {}


# 顔の埋め込みベクトル同士の距離を計算
def calculate_distance(embedding1, embedding2):
    return np.linalg.norm(embedding1 - embedding2)


# メイン関数：フレームを受け取り、認識結果を返す
def recognize_face(frame, known_db):
    mp_face = mp.solutions.face_detection

    with mp_face.FaceDetection(min_detection_confidence=0.5) as detector:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        detection_result = detector.process(rgb_frame)

        # 顔が検出されなかった場合
        if not detection_result.detections:
            return None

        # 最初に検出された顔を使用
        detection = detection_result.detections[0]
        bboxC = detection.location_data.relative_bounding_box
        h, w, _ = frame.shape
        x = int(bboxC.xmin * w)
        y = int(bboxC.ymin * h)
        fw = int(bboxC.width * w)
        fh = int(bboxC.height * h)
        face_image = frame[y:y+fh, x:x+fw]

        # 顔の埋め込みベクトルを抽出（簡易版）
        face_resized = cv2.resize(face_image, (128, 128))
        embedding = face_resized.flatten().astype(np.float32)
        embedding /= np.linalg.norm(embedding)

        # 既知人物DBと比較
        min_distance = 999
        matched_name = None

        for name, db_embeddings in known_db.items():
            for db_emb in db_embeddings:
                dist = calculate_distance(embedding, db_emb)
                if dist < min_distance:
                    min_distance = dist
                    matched_name = name

        # 閾値で既知/未知を判定
        if min_distance < FACE_THRESHOLD:
            status = "known"
            name   = matched_name
        else:
            status = "unknown"
            name   = None

        # インターフェース仕様書に準拠した戻り値
        return {
            "status"    : status,
            "name"      : name,
            "confidence": round(1 - min_distance, 2),
            "timestamp" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "face_image": face_image
        }