from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot, Signal, QThread
from packages.ui.applicationControllerClass import Ui_MainWindow

from packages.passwordWindow import PasswordWindow
from packages.homeWindow import HomeWindow

from packages.password_tasks import password_tasks as PasswordTask

from packages.scheduler import Scheduler

class ApplicationController(QMainWindow):
    terminateThread = Signal()
    initMailTask = Signal()

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

        self.ui.applicationStack.setCurrentIndex(0)
    
    @Slot()
    def onLoggedIn(self):
        self.ui.applicationStack.setCurrentIndex(1)
        self.initMailTask.emit()
    
    def initScheduler(self):
        self.thread = QThread()
        self.schedulerWorker = Scheduler(self.thread)
        self.schedulerWorker.moveToThread(self.thread)

        self.thread.started.connect(self.schedulerWorker.run)

        self.terminateThread.connect(self.schedulerWorker.terminateThread)

        #temporary var for quick access
        mailWindow = self.homeWindow.mailWindow
        SCHMail = self.schedulerWorker.mailTask

        #Wiring for Mail Module
        mailWindow.googleRegistration.connect(SCHMail.generateToken)
        mailWindow.sendEmail.connect(SCHMail.sendEmail)
        mailWindow.refreshPage.connect(SCHMail.CheckInbox)

        SCHMail.credentialsValidity.connect(mailWindow.onGotLoginStatus)
        SCHMail.inboxPayload.connect(mailWindow.setEmailList)
        SCHMail.sentEmail.connect(mailWindow.onSentEmail)
        self.initMailTask.connect(SCHMail.signIn)
        
        self.thread.start()

    @Slot()
    def quit(self):
        self.terminateThread.emit()
        self.thread.quit()
        self.thread.wait()