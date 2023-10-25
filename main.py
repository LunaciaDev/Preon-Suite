import sys
from PySide6.QtWidgets import QApplication
from packages.homeWindow import HomeWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setApplicationDisplayName("Preon Suite")

    with open("style/style.qss") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    mainWindow = HomeWindow()
    mainWindow.show()

    sys.exit(app.exec())