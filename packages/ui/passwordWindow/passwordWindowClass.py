# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_passwordWindow(object):
    def setupUi(self, passwordWindow):
        if not passwordWindow.objectName():
            passwordWindow.setObjectName(u"passwordWindow")
        passwordWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(passwordWindow.sizePolicy().hasHeightForWidth())
        passwordWindow.setSizePolicy(sizePolicy)
        passwordWindow.setMinimumSize(QSize(1280, 720))
        passwordWindow.setMaximumSize(QSize(1280, 720))
        self.horizontalLayout_2 = QHBoxLayout(passwordWindow)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.loginStack = QStackedWidget(passwordWindow)
        self.loginStack.setObjectName(u"loginStack")
        self.loginStack.setEnabled(True)
        self.loginStack.setMinimumSize(QSize(0, 0))
        self.loginStack.setMaximumSize(QSize(123132, 123132))
        self.faceIDLogin = QWidget()
        self.faceIDLogin.setObjectName(u"faceIDLogin")
        self.gridLayout_2 = QGridLayout(self.faceIDLogin)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_7 = QSpacerItem(20, 151, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(324, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.faceIDCameraFeed = QLabel(self.faceIDLogin)
        self.faceIDCameraFeed.setObjectName(u"faceIDCameraFeed")
        sizePolicy.setHeightForWidth(self.faceIDCameraFeed.sizePolicy().hasHeightForWidth())
        self.faceIDCameraFeed.setSizePolicy(sizePolicy)
        self.faceIDCameraFeed.setMinimumSize(QSize(300, 300))
        self.faceIDCameraFeed.setAutoFillBackground(False)
        self.faceIDCameraFeed.setFrameShape(QFrame.NoFrame)
        self.faceIDCameraFeed.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.faceIDCameraFeed)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_10 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_10)

        self.label_5 = QLabel(self.faceIDLogin)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)

        self.instructionLabel = QLabel(self.faceIDLogin)
        self.instructionLabel.setObjectName(u"instructionLabel")
        self.instructionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.instructionLabel)

        self.verticalSpacer_9 = QSpacerItem(20, 160, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.passwordLoginButton = QToolButton(self.faceIDLogin)
        self.passwordLoginButton.setObjectName(u"passwordLoginButton")
        self.passwordLoginButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.passwordLoginButton)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(324, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 67, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 2, 1, 1, 1)

        self.loginStack.addWidget(self.faceIDLogin)
        self.credentalLogin = QWidget()
        self.credentalLogin.setObjectName(u"credentalLogin")
        self.gridLayout = QGridLayout(self.credentalLogin)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(338, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(338, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 201, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.credentalLogin)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.wrongCredentialLabel = QLabel(self.credentalLogin)
        self.wrongCredentialLabel.setObjectName(u"wrongCredentialLabel")
        self.wrongCredentialLabel.setFrameShape(QFrame.Box)
        self.wrongCredentialLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.wrongCredentialLabel)

        self.verticalSpacer_3 = QSpacerItem(10, 5, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_3 = QLabel(self.credentalLogin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setOpenExternalLinks(False)

        self.verticalLayout.addWidget(self.label_3)

        self.usernameInput = QLineEdit(self.credentalLogin)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setEnabled(True)

        self.verticalLayout.addWidget(self.usernameInput)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.credentalLogin)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.passwordInput = QLineEdit(self.credentalLogin)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passwordInput)

        self.verticalSpacer_5 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.loginButton = QToolButton(self.credentalLogin)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(60, 0))
        self.loginButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginButton.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.horizontalLayout_3.addWidget(self.loginButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.registerButton = QToolButton(self.credentalLogin)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.registerButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.loginStack.addWidget(self.credentalLogin)
        self.createCredential = QWidget()
        self.createCredential.setObjectName(u"createCredential")
        self.gridLayout_3 = QGridLayout(self.createCredential)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_16 = QSpacerItem(20, 231, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_16, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(345, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_13, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.createCredential)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)

        self.verticalSpacer_11 = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)

        self.createAccountErrorLabel = QLabel(self.createCredential)
        self.createAccountErrorLabel.setObjectName(u"createAccountErrorLabel")
        self.createAccountErrorLabel.setFrameShape(QFrame.Box)
        self.createAccountErrorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.createAccountErrorLabel)

        self.verticalSpacer_12 = QSpacerItem(10, 8, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_12)

        self.label_7 = QLabel(self.createCredential)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setOpenExternalLinks(False)

        self.verticalLayout_3.addWidget(self.label_7)

        self.createUsernameInput = QLineEdit(self.createCredential)
        self.createUsernameInput.setObjectName(u"createUsernameInput")
        self.createUsernameInput.setEnabled(True)

        self.verticalLayout_3.addWidget(self.createUsernameInput)

        self.verticalSpacer_13 = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_13)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.createCredential)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.createPasswordInput = QLineEdit(self.createCredential)
        self.createPasswordInput.setObjectName(u"createPasswordInput")
        self.createPasswordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.createPasswordInput)

        self.verticalSpacer_17 = QSpacerItem(20, 8, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_17)

        self.label_9 = QLabel(self.createCredential)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.confirmPasswordInput = QLineEdit(self.createCredential)
        self.confirmPasswordInput.setObjectName(u"confirmPasswordInput")
        self.confirmPasswordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.confirmPasswordInput)

        self.verticalSpacer_14 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_14)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_12)

        self.backToLoginButton = QToolButton(self.createCredential)
        self.backToLoginButton.setObjectName(u"backToLoginButton")
        self.backToLoginButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.backToLoginButton)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_16)

        self.createAccountButton = QToolButton(self.createCredential)
        self.createAccountButton.setObjectName(u"createAccountButton")
        self.createAccountButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.createAccountButton)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_14)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(345, 8, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_15, 1, 2, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 230, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_15, 2, 1, 1, 1)

        self.loginStack.addWidget(self.createCredential)

        self.horizontalLayout_2.addWidget(self.loginStack)


        self.retranslateUi(passwordWindow)

        self.loginStack.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(passwordWindow)
    # setupUi

    def retranslateUi(self, passwordWindow):
        passwordWindow.setWindowTitle(QCoreApplication.translate("passwordWindow", u"Form", None))
        self.faceIDCameraFeed.setText("")
        self.label_5.setText(QCoreApplication.translate("passwordWindow", u"Please keep your face in the camera's view", None))
        self.instructionLabel.setText(QCoreApplication.translate("passwordWindow", u"smth", None))
        self.passwordLoginButton.setText(QCoreApplication.translate("passwordWindow", u"Sign in using password instead", None))
        self.label_4.setText(QCoreApplication.translate("passwordWindow", u"Sign in to your Account", None))
        self.wrongCredentialLabel.setText(QCoreApplication.translate("passwordWindow", u"Incorrect username or password.", None))
        self.label_3.setText(QCoreApplication.translate("passwordWindow", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("passwordWindow", u"Password", None))
        self.passwordInput.setText("")
        self.loginButton.setText(QCoreApplication.translate("passwordWindow", u"Login", None))
        self.registerButton.setText(QCoreApplication.translate("passwordWindow", u"Create an Account", None))
        self.label_6.setText(QCoreApplication.translate("passwordWindow", u"Create an Account", None))
        self.createAccountErrorLabel.setText(QCoreApplication.translate("passwordWindow", u"Password does not match.", None))
        self.label_7.setText(QCoreApplication.translate("passwordWindow", u"Username", None))
        self.label_8.setText(QCoreApplication.translate("passwordWindow", u"Password", None))
        self.createPasswordInput.setText("")
        self.label_9.setText(QCoreApplication.translate("passwordWindow", u"Re-enter your password", None))
        self.confirmPasswordInput.setText("")
        self.backToLoginButton.setText(QCoreApplication.translate("passwordWindow", u"Back to Login", None))
        self.createAccountButton.setText(QCoreApplication.translate("passwordWindow", u"Create an Account", None))
    # retranslateUi

