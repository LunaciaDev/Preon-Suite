from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot
from packages.ui.passwordWindow.passwordBaseWindowClass import Ui_passwordBaseWindow
from packages.passwordLoginWindow import PasswordLoginWindow

class PasswordWindow(QWidget):
    def __init__(self):
        super(PasswordWindow, self).__init__()
        self.ui = Ui_passwordBaseWindow()
        self.ui.setupUi(self)

        self.passwordLoginWindow = PasswordLoginWindow()

        self.ui.passwordWindowStack.addWidget(self.passwordLoginWindow)
        self.ui.passwordWindowStack.setCurrentIndex(0)

        self.passwordLoginWindow.loggedIn.connect(self.onLoggedIn)
    
    @Slot()
    def onLoggedIn(self):
        self.ui.passwordWindowStack.setCurrentIndex(1)