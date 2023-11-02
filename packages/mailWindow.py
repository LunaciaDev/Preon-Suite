from PySide6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Signal, Slot, QTimer
from packages.ui.mailWindow.mailWindowClass import Ui_mailWindow
import re

class MailWindow(QWidget):
    sendEmail = Signal(str, str, str)

    def __init__(self):
        super(MailWindow, self).__init__()
        self.ui = Ui_mailWindow();
        self.ui.setupUi(self)

        self.ui.mailStack.setCurrentIndex(0)
        self.ui.errorPopup.hide()
        self.ui.successPopup.hide()

        self.popupTimer = QTimer(self)
        self.popupTimer.setSingleShot(True)
        self.popupTimer.timeout.connect(self.hideAllPopup)

        self.emailRegex = re.compile(r".*@.*\..*")

        self.ui.composeEmailButton.clicked.connect(self.onComposeEmailButtonClicked)
        self.ui.discardEmailButton.clicked.connect(self.onDiscardEmailButtonClicked)
        self.ui.sendEmailButton.clicked.connect(self.onSendEmailButtonClicked)
        self.ui.previousPageButton.clicked.connect(self.onPreviousPageButtonClicked)
        self.ui.nextPageButton.clicked.connect(self.onNextPageButtonClicked)
        self.ui.refreshButton.clicked.connect(self.onRefreshButtonClicked)
        self.ui.inboxList.cellClicked.connect(self.onReceivedEmailClicked)
        self.ui.returnButton.clicked.connect(self.onReturnButtonClicked)
        self.ui.loginWithGoogleButton.clicked.connect(self.onGoogleLoginButtonClicked)
        
        self.ui.addressField.returnPressed.connect(self.onSendEmailButtonClicked)
        self.ui.titleField.returnPressed.connect(self.onSendEmailButtonClicked)

    ###### Ui Controller
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

    @Slot(int, int)
    def onReceivedEmailClicked(self, row, column):
        self.ui.mailStack.setCurrentIndex(3)

    def errorPopup(self, errorMsg):
        self.ui.errorPopup.setText(errorMsg)
        self.ui.errorPopup.show()
        self.popupTimer.start(3000)

    def successPopup(self, successMsg):
        self.ui.successPopup.setText(successMsg)
        self.ui.successPopup.show()
        self.popupTimer.start(3000)
    
    @Slot()
    def hideAllPopup(self):
        self.ui.errorPopup.hide()
        self.ui.successPopup.hide()
    ######

    ###### Forward to Backend Controller
    @Slot()
    def onSendEmailButtonClicked(self):
        if (self.emailRegex.match(self.ui.addressField.text()) is None):
            QMessageBox.critical(self, "Preon Suite", "The recipient's address is invalid. Please make sure that the address is proper.", QMessageBox.Ok)
            return

        self.sendEmail.emit(self.ui.addressField.text(), self.ui.titleField.text(), self.ui.contentField.toPlainText())
    
    @Slot()
    def onPreviousPageButtonClicked(self):
        print("Previous page clicked")
    
    @Slot()
    def onNextPageButtonClicked(self):
        print("Next page clicked")

    @Slot()
    def onRefreshButtonClicked(self):
        print("Refresh button clicked")
        self.setEmailList()
    
    @Slot()
    def onGoogleLoginButtonClicked(self):
        #binding to google login ig
        self.ui.mailStack.setCurrentIndex(1)

    ######

    ###### Receive data from backend controller
    @Slot()
    def setEmailList(self):
        randomMailData = [
            {
                "Title": "Lorem ipsum",
                "Author": "Somebody"
            },
            {
                "Title": "Hello!",
                "Author": "Someone"
            },
            {
                "Title": "Calling for volunteers!",
                "Author": "John Doe"
            }
        ]

        for i in range(len(randomMailData)):
            mail = randomMailData[i]
            self.ui.inboxList.setItem(i, 0, QTableWidgetItem(mail["Author"]))
            self.ui.inboxList.setItem(i, 1, QTableWidgetItem(mail["Title"]))

    @Slot()
    def onSentEmail(self):
        self.ui.titleField.clear()
        self.ui.addressField.clear()
        self.ui.contentField.clear()

    @Slot()
    def setEmailData(self):
        pass

    @Slot()
    def onLoggedInToGoogle(self):
        self.ui.mailStack.setCurrentIndex(1)
    ######