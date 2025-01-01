import cv2
import time
import os
from API.execute_api import save_current_status, check_new_png
from datetime import datetime
from image_processing import apply_mosaic, detect_faces
from database import save_image_to_db
from PIL import Image, ImageTk

base_output_dir = 'capture_image'
if not os.path.exists(base_output_dir):
    os.makedirs(base_output_dir)  # 기본 폴더가 없으면 생성

camera_running = False
cap = None
mosaic_enabled = True
last_saved_time = None  # 초기화

def start_camera(label):
    global cap, camera_running, last_saved_time
    if not camera_running:
        cap = cv2.VideoCapture(0)
        camera_running = True
        last_saved_time = time.time()  # 카메라 시작 시 초기화
        process_video_stream(label)

def stop_camera():
    global cap, camera_running
    if camera_running:
        camera_running = False
        if cap:
            cap.release()
        cv2.destroyAllWindows()

def process_video_stream(label):
    global last_saved_time
    capture_interval = 10  # 10초 간격으로 이미지 저장

    while camera_running:
        ret, frame = cap.read()
        save_current_status()
        if not ret:
            break

        # 얼굴 감지
        detections = detect_faces(frame)
        if detections:
            current_time = time.time()

            for detection in detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                face_roi = frame[y:y+h, x:x+w]

                if face_roi.size > 0 and mosaic_enabled:
                    face_roi_mosaic = apply_mosaic(face_roi, mosaic_size=10)
                    frame[y:y+h, x:x+w] = face_roi_mosaic

            # 10초마다 이미지 저장
            if last_saved_time is None or current_time - last_saved_time >= capture_interval:
                timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
                filename = f'full_capture_{timestamp}.png'
                file_path = os.path.join(base_output_dir, filename)

                cv2.imwrite(file_path, frame)
                print(f'Successfully saved {filename} to local folder.')

                _, buffer = cv2.imencode('.png', frame)
                image_data = buffer.tobytes()
                save_image_to_db(filename, image_data)

                last_saved_time = current_time  # 마지막 저장 시간 업데이트
                check_new_png()

        # 프레임을 GUI에 업데이트
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame_rgb)
        image_tk = ImageTk.PhotoImage(image)
        label.config(image=image_tk)
        label.image = image_tk

        # ESC 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == 27:
            break

    stop_camera()

def toggle_mosaic():
    global mosaic_enabled
    mosaic_enabled = not mosaic_enabled
    return mosaic_enabled
