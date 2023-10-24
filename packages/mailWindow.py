from PySide6.QtWidgets import QWidget
from packages.ui.mailBaseWindowClass import Ui_mailBaseWindow

class MailWindow(QWidget):
    def __init__(self):
        super(MailWindow, self).__init__()
        self.ui = Ui_mailBaseWindow();
        self.ui.setupUi(self)