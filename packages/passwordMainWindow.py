from PySide6.QtWidgets import QWidget
from packages.ui.passwordWindow.passwordMainWindowClass import Ui_passwordMainWindow

class PasswordMainWindow(QWidget):
    def __init__(self):
        super(PasswordMainWindow, self).__init__()
        self.ui = Ui_passwordMainWindow();
        self.ui.setupUi(self)