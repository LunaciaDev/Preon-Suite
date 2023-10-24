from PySide6.QtWidgets import QWidget
from packages.ui.passwordBaseWindowClass import Ui_passwordBaseWindow

class PasswordWindow(QWidget):
    def __init__(self):
        super(PasswordWindow, self).__init__()
        self.ui = Ui_passwordBaseWindow()
        self.ui.setupUi(self)