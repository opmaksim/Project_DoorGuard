from gui import create_gui
from database import initialize_db, close_db

if __name__ == "__main__":
    initialize_db()
    create_gui()
    close_db()
