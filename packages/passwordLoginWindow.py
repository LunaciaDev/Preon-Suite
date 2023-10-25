from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot
from packages.ui.passwordWindow.passwordLoginWindowClass import Ui_passwordLoginWindow

class PasswordLoginWindow(QWidget):
    validateCredential = Signal(str, str)
    createCredential = Signal(str, str)
    loggedIn = Signal()

    def __init__(self):
        super(PasswordLoginWindow, self).__init__()
        self.ui = Ui_passwordLoginWindow();
        self.ui.setupUi(self)
        
        self.ui.forgotPasswordLabel.linkActivated.connect(self.onForgetPasswordClicked)
        self.ui.registerButton.clicked.connect(self.onRegisterButtonClicked)
        self.ui.loginButton.clicked.connect(self.onLoginButtonClicked)
        self.ui.passwordLoginButton.clicked.connect(self.onSwitchToCredentalLoginClicked)

        self.ui.loginStack.setCurrentIndex(0)

        self.ui.wrongCredentialLabel.hide()
        self.ui.instructionLabel.hide()

    @Slot()
    def onSwitchToCredentalLoginClicked(self):
        self.ui.loginStack.setCurrentIndex(1)
    
    @Slot()
    def onForgetPasswordClicked(self):
        print("Forget Password Button Clicked")
    
    @Slot()
    def onRegisterButtonClicked(self):
        print("Register User button clicked")

    @Slot()
    def onLoginButtonClicked(self):
        print("Login button clicked")
        self.validateCredential.emit(self.ui.usernameInput, self.ui.passwordInput)

    @Slot(bool, str)
    def onValidationCompleted(self, success, labelValue):
        if (success):
            print("Login suceeded")
            self.ui.usernameInput.clear()
            self.ui.passwordInput.clear()
            self.loggedIn.emit()
            return
        
        #Just in case if they wanted it
        self.ui.wrongCredentialLabel.setText(labelValue)
        self.ui.wrongCredentialLabel.show()
        