import sys
import sass
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot
from packages.applicationController import ApplicationController

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setApplicationDisplayName("Preon Suite")

    with open("style/style.qss") as f:
        _style = f.read()
        _style = sass.compile(string=_style)
        app.setStyleSheet(_style)

    mainWindow = ApplicationController()

    app.aboutToQuit.connect(mainWindow.quit)

    mainWindow.initScheduler()
    mainWindow.show()

    sys.exit(app.exec())