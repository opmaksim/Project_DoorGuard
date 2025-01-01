import mysql.connector
import os
from datetime import datetime

# MySQL 데이터베이스 연결 설정
db_config = {
    'user': 'root',
    'password': 'qwer1234',
    'host': 'localhost',
    'database': 'image_upload',
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

def initialize_db():
    """ 테이블 생성 (없으면 생성) """
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS captured_images (
        id INT AUTO_INCREMENT PRIMARY KEY,
        upload_time DATETIME NOT NULL,
        filename VARCHAR(255) NOT NULL,
        image LONGBLOB NOT NULL
    )
    """)
    conn.commit()

def save_image_to_db(filename, image_data):
    """ 이미지 데이터베이스에 저장 """
    upload_time = datetime.now()
    try:
        cursor.execute("INSERT INTO captured_images (upload_time, filename, image) VALUES (%s, %s, %s)", (upload_time, filename, image_data))
        conn.commit()
        print(f'Successfully saved {filename} at {upload_time} to the database.')
    except mysql.connector.Error as err:
        print(f'Failed to save image to database: {err}')

def delete_images_from_db():
    """ 데이터베이스에서 이미지 삭제 """
    try:
        cursor.execute("DELETE FROM captured_images")
        conn.commit()
        folder_path = 'capture_image'
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All images have been deleted from the database.")
    except mysql.connector.Error as err:
        print(f'Failed to delete images from database: {err}')

def close_db():
    """ 데이터베이스 연결 종료 """
    cursor.close()
    conn.close()
