from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from packages.ui.applicationControllerClass import Ui_MainWindow

from packages.passwordWindow import PasswordWindow
from packages.homeWindow import HomeWindow

from packages.password_tasks import password_tasks as PasswordTask

class ApplicationController(QMainWindow):
    def __init__(self):
        super(ApplicationController, self).__init__()
        self.ui = Ui_MainWindow();
        self.ui.setupUi(self)

        self.homeWindow = HomeWindow()
        self.passwordWindow = PasswordWindow()

        self.ui.applicationStack.addWidget(self.passwordWindow)
        self.ui.applicationStack.addWidget(self.homeWindow)

        self.passwordTask = PasswordTask()

        self.passwordTask.loginStatus.connect(self.passwordWindow.onValidationCompleted)
        self.passwordTask.registerStatus.connect(self.passwordWindow.onAccountRegistrated)
        self.passwordWindow.validateCredential.connect(self.passwordTask.login)
        self.passwordWindow.createCredential.connect(self.passwordTask.register)
        self.passwordWindow.loggedIn.connect(self.onLoggedIn)

        self.ui.applicationStack.setCurrentIndex(1)
    
    @Slot()
    def onLoggedIn(self):
        self.ui.applicationStack.setCurrentIndex(1)