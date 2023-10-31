from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot
from packages.ui.passwordWindow.passwordWindowClass import Ui_passwordWindow

class PasswordWindow(QWidget):
    validateCredential = Signal(str, str)
    createCredential = Signal(str, str)
    loggedIn = Signal()

    def __init__(self):
        super(PasswordWindow, self).__init__()
        self.ui = Ui_passwordWindow();
        self.ui.setupUi(self)
        
        self.ui.registerButton.clicked.connect(self.onRegisterButtonClicked)
        self.ui.loginButton.clicked.connect(self.onLoginButtonClicked)
        self.ui.passwordLoginButton.clicked.connect(self.onSwitchToCredentalLoginClicked)
        self.ui.backToLoginButton.clicked.connect(self.onSwitchToCredentalLoginClicked)
        self.ui.createAccountButton.clicked.connect(self.onCreateAccountButtonClicked)
        self.ui.usernameInput.returnPressed.connect(self.onLoginButtonClicked)
        self.ui.passwordInput.returnPressed.connect(self.onLoginButtonClicked)
        self.ui.createUsernameInput.returnPressed.connect(self.onCreateAccountButtonClicked)
        self.ui.createPasswordInput.returnPressed.connect(self.onCreateAccountButtonClicked)
        self.ui.confirmPasswordInput.returnPressed.connect(self.onCreateAccountButtonClicked)

        #TODO: Check if user have Face ID
        #if (have FaceID):
        #   self.ui.loginStack.setCurrentIndex(0)
        #else:
        self.ui.loginStack.setCurrentIndex(1)

        self.ui.wrongCredentialLabel.hide()
        self.ui.createAccountErrorLabel.hide()
        self.ui.instructionLabel.hide()

    # Registration Control #
    @Slot()
    def onCreateAccountButtonClicked(self):
        if (self.ui.createPasswordInput.text() == "" or self.ui.createUsernameInput.text() == ""):
            self.ui.createAccountErrorLabel.setText("You must fill in the username and password.")
            self.ui.createAccountErrorLabel.show()
            return

        if (self.ui.createPasswordInput.text() == self.ui.confirmPasswordInput.text()):
            self.createCredential.emit(self.ui.createUsernameInput.text(), self.ui.createPasswordInput.text())
            return

        self.ui.createAccountErrorLabel.setText("Password does not match.")
        self.ui.createAccountErrorLabel.show()

    @Slot(bool)
    def onAccountRegistrated(self, success):
        self.ui.createUsernameInput.setText("")
        self.ui.createPasswordInput.setText("")
        self.ui.confirmPasswordInput.setText("")
        self.ui.createAccountErrorLabel.hide()

        self.loggedIn.emit()
    ######

    # User Interface Control #
    @Slot()
    def onSwitchToCredentalLoginClicked(self):
        self.ui.loginStack.setCurrentIndex(1)

    @Slot()
    def onRegisterButtonClicked(self):
        self.ui.loginStack.setCurrentIndex(2)
    ######

    # Login Control #
    @Slot()
    def onLoginButtonClicked(self):
        self.validateCredential.emit(self.ui.usernameInput.text(), self.ui.passwordInput.text())

    @Slot(bool)
    def onValidationCompleted(self, success):
        if (success):
            self.ui.usernameInput.setText("")
            self.ui.passwordInput.setText("")
            self.ui.wrongCredentialLabel.hide()
            self.loggedIn.emit()

            return
        
        self.ui.wrongCredentialLabel.show()
    ######