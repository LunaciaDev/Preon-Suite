from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot, Signal, QThread
from packages.ui.applicationControllerClass import Ui_MainWindow

from packages.passwordWindow import PasswordWindow
from packages.homeWindow import HomeWindow
from packages.faceIDWindow import FaceIDWindow

from packages.password_tasks import password_tasks as PasswordTask
from packages.faceIDTask import FaceIDTask

from packages.scheduler import Scheduler

class ApplicationController(QMainWindow):
    terminateThread = Signal()
    startFaceIDRegistration = Signal(str)
    initTask = Signal()

    def __init__(self):
        super(ApplicationController, self).__init__()
        self.ui = Ui_MainWindow();
        self.ui.setupUi(self)

        # initialize underlying UIs
        self.homeWindow = HomeWindow()
        self.passwordWindow = PasswordWindow()
        self.faceIDRegisterWindow = FaceIDWindow()

        self.ui.applicationStack.addWidget(self.passwordWindow)
        self.ui.applicationStack.addWidget(self.homeWindow)
        self.ui.applicationStack.addWidget(self.faceIDRegisterWindow)

        # initialize password-related tasks
        self.passwordTask = PasswordTask()

        # initialize a thread for FaceID
        self.faceIDThread = QThread()
        self.faceIDTask = FaceIDTask(self.faceIDThread)
        self.faceIDTask.moveToThread(self.faceIDThread)

        # prepare connections for password/FaceID tasks
        self.terminateThread.connect(self.faceIDTask.terminateThread)
        self.passwordTask.loginStatus.connect(self.passwordWindow.onValidationCompleted)
        self.passwordTask.registerStatus.connect(self.passwordWindow.onAccountRegistrated)
        self.passwordWindow.validateCredential.connect(self.passwordTask.login)
        self.passwordWindow.createCredential.connect(self.passwordTask.register)
        self.passwordWindow.loggedIn.connect(self.onLoggedIn)

        self.faceIDTask.userVerified.connect(self.onLoggedIn)
        self.faceIDTask.sendImageSignIn.connect(self.passwordWindow.setLoginCameraFeed)
        self.passwordWindow.interruptFaceIDLogin.connect(self.faceIDTask.interruptFaceIDSignIn)
        self.passwordWindow.startFaceIDLogin.connect(self.faceIDTask.verifyUser)
        self.startFaceIDRegistration.connect(self.faceIDTask.registerUser)

        self.faceIDRegisterWindow.cancelRegistration.connect(self.faceIDTask.interruptFaceIDRegister)
        self.faceIDRegisterWindow.cancelRegistration.connect(self.cancelRegisterFaceID)
        self.faceIDTask.sendImageRegister.connect(self.faceIDRegisterWindow.setLoginCameraFeed)
        self.faceIDTask.finishRegistration.connect(self.faceIDRegisterWindow.onFinishRegistration)

        self.homeWindow.ui.registerFaceIDButton.clicked.connect(self.registerFaceID)

        self.passwordWindow.loggedIn.connect(self.homeWindow.dashboardWindow.onLoggedIn)
        self.faceIDTask.userVerified.connect(self.homeWindow.dashboardWindow.onLoggedIn)

        self.ui.applicationStack.setCurrentIndex(0)
        self.faceIDThread.start()
    
    @Slot()
    def cancelRegisterFaceID(self):
        self.ui.applicationStack.setCurrentIndex(1)

    @Slot()
    def registerFaceID(self):
        self.ui.applicationStack.setCurrentIndex(2)
        self.startFaceIDRegistration.emit(self.username)
    
    @Slot(str)
    def onLoggedIn(self, username):
        self.ui.applicationStack.setCurrentIndex(1)
        self.username = username
        self.initTask.emit()
    
    def initScheduler(self):
        self.workerThread = QThread()
        self.schedulerWorker = Scheduler(self.workerThread)
        self.schedulerWorker.moveToThread(self.workerThread)

        self.workerThread.started.connect(self.schedulerWorker.run)

        self.terminateThread.connect(self.schedulerWorker.terminateThread)

        #temporary var for quick access
        mailWindow = self.homeWindow.mailWindow
        reminderWindow = self.homeWindow.reminderWindow
        SCHMail = self.schedulerWorker.mailTask
        reminderTask = self.schedulerWorker.reminderTask

        #Wiring for Mail Module
        mailWindow.googleRegistration.connect(SCHMail.generateToken)
        mailWindow.sendEmail.connect(SCHMail.sendEmail)
        mailWindow.refreshPage.connect(SCHMail.CheckInbox)

        #Wiring for Weather Module
        self.schedulerWorker.weatherTask.sendWeatherData.connect(self.homeWindow.weatherWindow.onReceiveWeatherData)

        SCHMail.credentialsValidity.connect(mailWindow.onGotLoginStatus)
        SCHMail.inboxPayload.connect(mailWindow.setEmailList)
        SCHMail.sentEmail.connect(mailWindow.onSentEmail)

        #Wiring for Reminder Module
        reminderWindow.removeReminder.connect(reminderTask.remove_reminder)
        reminderWindow.addReminder.connect(reminderTask.add_reminder)
        reminderWindow.editReminder.connect(reminderTask.edit_reminder)
        reminderWindow.saveToMarkdown.connect(reminderTask.save_to_markdown)
        reminderTask.sendReminderList.connect(reminderWindow.refreshReminders)

        #Wiring for task initialization
        self.initTask.connect(self.schedulerWorker.mailTask.signIn)
        self.initTask.connect(self.schedulerWorker.weatherTask.getData)
        self.initTask.connect(self.schedulerWorker.reminderTask.load_reminders)
        
        self.workerThread.start()

    @Slot()
    def quit(self):
        self.terminateThread.emit()
        self.faceIDThread.wait()
        self.workerThread.wait()