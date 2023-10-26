from PySide6.QtWidgets import QWidget
from packages.ui.applicationControllerClass import Ui_applicationController
from packages.passwordWindow import PasswordWindow
from packages.homeWindow import HomeWindow

class ApplicationController(QWidget):
    def __init__(self):
        super(ApplicationController, self).__init__()
        self.ui = Ui_applicationController();
        self.ui.setupUi(self)

        self.homeWindow = HomeWindow()
        self.passwordWindow = PasswordWindow()

        self.ui.applicationStack.addWidget(self.passwordWindow)
        self.ui.applicationStack.addWidget(self.homeWindow)

        self.ui.applicationStack.setCurrentIndex(0)