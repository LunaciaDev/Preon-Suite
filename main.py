import sys
from PySide6.QtWidgets import QApplication
from packages.mainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    with open("style/style.qss") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())