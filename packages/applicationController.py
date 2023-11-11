from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot, Signal, QThread
from packages.ui.applicationControllerClass import Ui_MainWindow

from packages.passwordWindow import PasswordWindow
from packages.homeWindow import HomeWindow

from packages.password_tasks import password_tasks as PasswordTask

from packages.scheduler import Scheduler

class ApplicationController(QMainWindow):
    terminateThread = Signal()
    initTask = Signal()

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
        self.workerThread.wait()