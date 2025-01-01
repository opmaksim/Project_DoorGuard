import subprocess
import os
import time

global existing_files
global current_files
directory_to_watch = r"D:\Study\Academy\Project_DoorGuard\capture_image"
def save_current_status():
    global existing_files
    existing_files = {f for f in os.listdir(directory_to_watch) if f.endswith('.png')}

def check_new_png():
    global existing_files
    global current_files
    current_files = {f for f in os.listdir(directory_to_watch) if f.endswith('.png')}
        
    # 새로 생긴 파일 탐지
    new_files = current_files - existing_files
        
    if new_files:
        print(f"New PNG files detected: {', '.join(new_files)}")
        import API.set_json
        subprocess.run(['python', 'API/send_message.py'], check=False)
        existing_files = current_files
