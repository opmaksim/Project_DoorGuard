import tkinter as tk
from tkinter import messagebox
import threading
from camera import start_camera, stop_camera, toggle_mosaic
from database import delete_images_from_db

def start_camera_thread(label):
    threading.Thread(target=start_camera, args=(label,), daemon=True).start()

def create_gui():
    root = tk.Tk()
    root.title("DoorGuard 스마트 캠")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame)
    label.pack()

    tk.Button(frame, text="촬영 시작", command=lambda: start_camera_thread(label)).pack(fill='x')
    tk.Button(frame, text="촬영 중지", command=stop_camera).pack(fill='x')
    tk.Button(frame, text="모자이크 on/off", command=lambda: messagebox.showinfo("Mosaic Effect", f"Mosaic effect is now {'enabled' if toggle_mosaic() else 'disabled'}")).pack(fill='x')
    tk.Button(frame, text="모든 삭진 삭제 (DB + Local)", command=delete_images_from_db).pack(fill='x')
    tk.Button(frame, text="프로그램 종료", command=root.quit).pack(fill='x')

    root.after(100, lambda: start_camera_thread(label))  # Start camera after 100 ms to ensure GUI is fully loaded

    root.mainloop()
