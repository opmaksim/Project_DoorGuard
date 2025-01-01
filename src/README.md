## ⚙️ **작동 흐름**
1. **시스템 초기화**:
   - `main.py` 실행 시 데이터베이스 초기화 및 GUI 실행.
   - `initialize_db()` 함수로 테이블 생성.

2. **실시간 얼굴 감지**:
   - `camera.py`에서 OpenCV와 Mediapipe로 얼굴 감지.
   - 10초마다 감지된 이미지를 로컬에 저장.

3. **데이터 저장 및 관리**:
   - `database.py`로 감지된 이미지를 DB에 저장.
   - GUI를 통해 로컬 및 DB 데이터를 삭제 가능.

4. **카카오톡 알림 전송**:
   - `execute_api.py`로 새 이미지 확인 후 `send_message.py` 호출.
   - API 인증 및 메시지 전송.

5. **GUI 제어**:
   - `gui.py`에서 촬영 시작/중지, 모자이크 효과, 데이터 삭제 기능 제공.

## 💻 **코드 설명**
### **1. Camera.py**
- 얼굴 감지 및 모자이크 처리: `detect_faces`와 `apply_mosaic` 호출.
- 10초 간격으로 이미지 저장: `cv2.imwrite`.

### **2. Database.py**
- 테이블 생성 및 데이터 저장: `save_image_to_db`로 MariaDB 관리.
- 모든 데이터 삭제: `delete_images_from_db`.

### **3. GUI.py**
- QT 기반 버튼 및 라벨 UI 구성.
- 실시간 스트림과 버튼 동작 제어.

### **4. Execute_API.py**
- 새 이미지 생성 여부 확인: `check_new_png`.
- 카카오톡 API 호출: `send_message.py`.