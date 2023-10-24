from PySide6.QtWidgets import QMainWindow
from packages.ui.mainWindowClass import Ui_MainWindow
from packages.homeWindow import HomeWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.homePage = HomeWindow()

        self.ui.pageStack.addWidget(self.homePage)
        self.ui.pageStack.setCurrentIndex(1)