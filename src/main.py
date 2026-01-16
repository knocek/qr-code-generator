# src/main.py
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from src.main_window import MainWindow
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ICON_PATH = BASE_DIR / "assets" / "icons" / "app-icon.png"


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(str(ICON_PATH)))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
