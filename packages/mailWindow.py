from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Signal, Slot, QTimer
from packages.ui.mailWindowClass import Ui_mailWindow
import re

class MailWindow(QWidget):
    sendEmail = Signal(str, str, str)
    refreshPage = Signal()
    googleRegistration = Signal()

    def __init__(self):
        super(MailWindow, self).__init__()
        self.ui = Ui_mailWindow();
        self.ui.setupUi(self)

        self.refreshAllowed = True

        self.popupTimer = QTimer(self)
        self.popupTimer.setSingleShot(True)
        self.popupTimer.timeout.connect(self.hideAllPopup)

        self.refreshTimer = QTimer(self)
        self.refreshTimer.setSingleShot(True)
        self.refreshTimer.timeout.connect(self.enableRefresh)

        self.emailRegex = re.compile(r".*@.*\..*")

        self.ui.composeEmailButton.clicked.connect(self.onComposeEmailButtonClicked)
        self.ui.discardEmailButton.clicked.connect(self.onDiscardEmailButtonClicked)
        self.ui.sendEmailButton.clicked.connect(self.onSendEmailButtonClicked)
        self.ui.refreshButton.clicked.connect(self.onRefreshButtonClicked)
        self.ui.returnButton.clicked.connect(self.onReturnButtonClicked)
        self.ui.loginWithGoogleButton.clicked.connect(self.onGoogleLoginButtonClicked)
        
        self.ui.addressField.returnPressed.connect(self.onSendEmailButtonClicked)
        self.ui.titleField.returnPressed.connect(self.onSendEmailButtonClicked)

        self.ui.inboxList.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.ui.errorPopup.hide()
        self.ui.successPopup.hide()

    def enableRefresh(self):
        self.refreshAllowed = True
    
    def errorPopup(self, errorMsg):
        self.ui.errorPopup.setText(errorMsg)
        self.ui.errorPopup.show()
        self.popupTimer.start(3000)

    def successPopup(self, successMsg):
        self.ui.successPopup.setText(successMsg)
        self.ui.successPopup.show()
        self.popupTimer.start(3000)

    ###### Ui Controller
    @Slot(bool)
    def onGotLoginStatus(self, loggedIn):
        if loggedIn:
            self.ui.mailStack.setCurrentIndex(1)

    @Slot()
    def onReturnButtonClicked(self):
        self.ui.mailStack.setCurrentIndex(1)
        self.ui.inboxList.setCurrentCell(-1, -1)

    @Slot()
    def onComposeEmailButtonClicked(self):
        self.ui.mailStack.setCurrentIndex(2)
    
    @Slot()
    def onDiscardEmailButtonClicked(self):
        self.ui.addressField.clear()
        self.ui.titleField.clear()
        self.ui.contentField.clear()
        self.ui.mailStack.setCurrentIndex(1)
    
    @Slot()
    def hideAllPopup(self):
        self.ui.errorPopup.hide()
        self.ui.successPopup.hide()
    ######

    ###### Forward to Backend Controller
    @Slot()
    def onSendEmailButtonClicked(self):
        if (self.emailRegex.match(self.ui.addressField.text()) is None):
            # TODO: MEMORY LEAK HERE
            QMessageBox.critical(self, "Preon Suite", "The recipient's address is invalid. Please make sure that the address is proper.", QMessageBox.Ok)
            return

        self.sendEmail.emit(self.ui.addressField.text(), self.ui.titleField.text(), self.ui.contentField.toPlainText())

    @Slot()
    def onRefreshButtonClicked(self):
        if self.refreshAllowed:
            self.refreshPage.emit()
            self.refreshAllowed = False
            self.refreshTimer.start(60)
            return

        self.errorPopup("You are refreshing too fast!")
    
    @Slot()
    def onGoogleLoginButtonClicked(self):
        self.googleRegistration.emit()

    ######

    ###### Receive data from backend controller
    @Slot(list)
    def setEmailList(self, mailPayload):
        for i in range(len(mailPayload)):
            self.cachedMail = mailPayload[i]
            self.ui.inboxList.setItem(i, 0, QTableWidgetItem(self.cachedMail["sender"].split("<")[0].strip()))
            self.ui.inboxList.setItem(i, 1, QTableWidgetItem(self.cachedMail["subject"]))

    @Slot()
    def onSentEmail(self):
        self.ui.titleField.clear()
        self.ui.addressField.clear()
        self.ui.contentField.clear()
        self.ui.mailStack.setCurrentIndex(1)
        self.successPopup("Email Sent!")
    ######