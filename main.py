import sys
from ui.app import App

if __name__ == "__main__":
    file_path = sys.argv[1]
    console_app = App(file_path)
    console_app.start_app()