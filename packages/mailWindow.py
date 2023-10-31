from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import Signal, Slot
from packages.ui.mailWindow.mailWindowClass import Ui_mailWindow
import re

class MailWindow(QWidget):
    sendEmail = Signal(str, str, str)

    def __init__(self):
        super(MailWindow, self).__init__()
        self.ui = Ui_mailWindow();
        self.ui.setupUi(self)
        self.ui.mailStack.setCurrentIndex(1)
        self.ui.actionStack.setCurrentIndex(2)

        self.emailRegex = re.compile(r".*@.*\..*")

        self.ui.composeEmailButton.clicked.connect(self.onComposeEmailButtonClicked)
        self.ui.discardEmailButton.clicked.connect(self.onDiscardEmailButtonClicked)

    ###### Ui Controller
    @Slot()
    def onComposeEmailButtonClicked(self):

        self.ui.actionStack.setCurrentIndex(3)
    
    @Slot()
    def onDiscardEmailButtonClicked(self):
        self.ui.actionStack.setCurrentIndex(2)

    @Slot()
    def onReceivedEmailClicked(self):
        self.ui.actionStack.setCurrentIndex(1)
    ######

    ###### Forward to Backend Controller
    @Slot()
    def onSendEmailButtonClicked(self):
        if (self.emailRegex.match(self.ui.addressField.text()) is None):
            #do something
            return

        self.sendEmail.emit(self.ui.addressField.text(), self.ui.titleField.text(), self.ui.contentField.text())
