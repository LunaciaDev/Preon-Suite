# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mailWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)

class Ui_mailWindow(object):
    def setupUi(self, mailWindow):
        if not mailWindow.objectName():
            mailWindow.setObjectName(u"mailWindow")
        mailWindow.resize(1080, 720)
        mailWindow.setMaximumSize(QSize(1080, 720))
        mailWindow.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(mailWindow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.mailStack = QStackedWidget(mailWindow)
        self.mailStack.setObjectName(u"mailStack")
        self.mailStack.setMaximumSize(QSize(1080, 720))
        self.mailStack.setStyleSheet(u"")
        self.permissionWindow = QWidget()
        self.permissionWindow.setObjectName(u"permissionWindow")
        self.gridLayout = QGridLayout(self.permissionWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 303, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(347, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.permissionWindow)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.loginWithGoogleButton = QToolButton(self.permissionWindow)
        self.loginWithGoogleButton.setObjectName(u"loginWithGoogleButton")
        self.loginWithGoogleButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        iconThemeName = u"mail-unread"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.loginWithGoogleButton.setIcon(icon)
        self.loginWithGoogleButton.setIconSize(QSize(16, 16))
        self.loginWithGoogleButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_2.addWidget(self.loginWithGoogleButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(347, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 302, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.mailStack.addWidget(self.permissionWindow)
        self.mainWindow = QWidget()
        self.mainWindow.setObjectName(u"mainWindow")
        self.horizontalLayout_7 = QHBoxLayout(self.mainWindow)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.inbox = QWidget(self.mainWindow)
        self.inbox.setObjectName(u"inbox")
        self.verticalLayout_4 = QVBoxLayout(self.inbox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.inboxAddress = QLabel(self.inbox)
        self.inboxAddress.setObjectName(u"inboxAddress")

        self.horizontalLayout_4.addWidget(self.inboxAddress)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.composeEmailButton = QToolButton(self.inbox)
        self.composeEmailButton.setObjectName(u"composeEmailButton")
        self.composeEmailButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.composeEmailButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.previousPageButton = QToolButton(self.inbox)
        self.previousPageButton.setObjectName(u"previousPageButton")
        self.previousPageButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"icons/go-previous-symbolic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previousPageButton.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.previousPageButton)

        self.refreshButton = QToolButton(self.inbox)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"icons/view-refresh-symbolic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.refreshButton)

        self.nextPageButton = QToolButton(self.inbox)
        self.nextPageButton.setObjectName(u"nextPageButton")
        self.nextPageButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"icons/go-next-symbolic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nextPageButton.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.nextPageButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.inboxList = QTableWidget(self.inbox)
        if (self.inboxList.columnCount() < 2):
            self.inboxList.setColumnCount(2)
        if (self.inboxList.rowCount() < 10):
            self.inboxList.setRowCount(10)
        self.inboxList.setObjectName(u"inboxList")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inboxList.sizePolicy().hasHeightForWidth())
        self.inboxList.setSizePolicy(sizePolicy)
        self.inboxList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.inboxList.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.inboxList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.inboxList.setAutoScroll(False)
        self.inboxList.setAutoScrollMargin(0)
        self.inboxList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.inboxList.setTabKeyNavigation(False)
        self.inboxList.setProperty("showDropIndicator", False)
        self.inboxList.setDragDropOverwriteMode(False)
        self.inboxList.setAlternatingRowColors(False)
        self.inboxList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.inboxList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.inboxList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.inboxList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.inboxList.setShowGrid(False)
        self.inboxList.setWordWrap(False)
        self.inboxList.setCornerButtonEnabled(False)
        self.inboxList.setRowCount(10)
        self.inboxList.setColumnCount(2)
        self.inboxList.horizontalHeader().setVisible(False)
        self.inboxList.horizontalHeader().setHighlightSections(False)
        self.inboxList.horizontalHeader().setStretchLastSection(True)
        self.inboxList.verticalHeader().setVisible(False)
        self.inboxList.verticalHeader().setCascadingSectionResizes(False)
        self.inboxList.verticalHeader().setDefaultSectionSize(58)
        self.inboxList.verticalHeader().setHighlightSections(False)
        self.inboxList.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.inboxList)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pageCount = QLabel(self.inbox)
        self.pageCount.setObjectName(u"pageCount")
        self.pageCount.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.pageCount)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addWidget(self.inbox)

        self.actionStack = QStackedWidget(self.mainWindow)
        self.actionStack.setObjectName(u"actionStack")
        self.viewEmail = QWidget()
        self.viewEmail.setObjectName(u"viewEmail")
        self.verticalLayout_3 = QVBoxLayout(self.viewEmail)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.receivedEmailAddress = QLabel(self.viewEmail)
        self.receivedEmailAddress.setObjectName(u"receivedEmailAddress")

        self.verticalLayout_3.addWidget(self.receivedEmailAddress)

        self.receivedEmailTitle = QLabel(self.viewEmail)
        self.receivedEmailTitle.setObjectName(u"receivedEmailTitle")

        self.verticalLayout_3.addWidget(self.receivedEmailTitle)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.receivedEmailContent = QTextEdit(self.viewEmail)
        self.receivedEmailContent.setObjectName(u"receivedEmailContent")
        self.receivedEmailContent.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.receivedEmailContent)

        self.actionStack.addWidget(self.viewEmail)
        self.blankPage = QWidget()
        self.blankPage.setObjectName(u"blankPage")
        self.verticalLayout_7 = QVBoxLayout(self.blankPage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.informationStack = QStackedWidget(self.blankPage)
        self.informationStack.setObjectName(u"informationStack")
        self.noInternetConnection = QWidget()
        self.noInternetConnection.setObjectName(u"noInternetConnection")
        self.verticalLayout_6 = QVBoxLayout(self.noInternetConnection)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.label_4 = QLabel(self.noInternetConnection)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMinimumSize(QSize(128, 128))
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setPixmap(QPixmap(u"icons/network-wireless-disconnected-symbolic.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.label_2 = QLabel(self.noInternetConnection)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)

        self.informationStack.addWidget(self.noInternetConnection)
        self.empty = QWidget()
        self.empty.setObjectName(u"empty")
        self.informationStack.addWidget(self.empty)
        self.emailSent = QWidget()
        self.emailSent.setObjectName(u"emailSent")
        self.verticalLayout_5 = QVBoxLayout(self.emailSent)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_10 = QSpacerItem(20, 246, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.label_6 = QLabel(self.emailSent)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(128, 128))
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setPixmap(QPixmap(u"icons/checkbox-checked-symbolic.svg"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.label_5 = QLabel(self.emailSent)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.verticalSpacer_9 = QSpacerItem(20, 245, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)

        self.informationStack.addWidget(self.emailSent)

        self.verticalLayout_7.addWidget(self.informationStack)

        self.actionStack.addWidget(self.blankPage)

        self.horizontalLayout_7.addWidget(self.actionStack)

        self.mailStack.addWidget(self.mainWindow)
        self.composeEmail = QWidget()
        self.composeEmail.setObjectName(u"composeEmail")
        self.verticalLayout_8 = QVBoxLayout(self.composeEmail)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.addressField = QLineEdit(self.composeEmail)
        self.addressField.setObjectName(u"addressField")

        self.verticalLayout_8.addWidget(self.addressField)

        self.titleField = QLineEdit(self.composeEmail)
        self.titleField.setObjectName(u"titleField")

        self.verticalLayout_8.addWidget(self.titleField)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.contentField = QTextEdit(self.composeEmail)
        self.contentField.setObjectName(u"contentField")

        self.verticalLayout_8.addWidget(self.contentField)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.discardEmailButton = QToolButton(self.composeEmail)
        self.discardEmailButton.setObjectName(u"discardEmailButton")

        self.horizontalLayout_3.addWidget(self.discardEmailButton)

        self.sendEmailButton = QToolButton(self.composeEmail)
        self.sendEmailButton.setObjectName(u"sendEmailButton")

        self.horizontalLayout_3.addWidget(self.sendEmailButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.mailStack.addWidget(self.composeEmail)

        self.horizontalLayout.addWidget(self.mailStack)


        self.retranslateUi(mailWindow)

        QMetaObject.connectSlotsByName(mailWindow)
    # setupUi

    def retranslateUi(self, mailWindow):
        mailWindow.setWindowTitle(QCoreApplication.translate("mailWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("mailWindow", u"Please login to your email account", None))
        self.loginWithGoogleButton.setText(QCoreApplication.translate("mailWindow", u"Login with Google", None))
        self.inboxAddress.setText(QCoreApplication.translate("mailWindow", u"Inbox <21323142@student.vgu.edu.vn>", None))
        self.composeEmailButton.setText(QCoreApplication.translate("mailWindow", u"Compose Email", None))
        self.previousPageButton.setText(QCoreApplication.translate("mailWindow", u"Previous", None))
        self.refreshButton.setText(QCoreApplication.translate("mailWindow", u"Refresh", None))
        self.nextPageButton.setText(QCoreApplication.translate("mailWindow", u"Next", None))
        self.pageCount.setText(QCoreApplication.translate("mailWindow", u"1-10 of 325", None))
        self.receivedEmailAddress.setText(QCoreApplication.translate("mailWindow", u"From: John Doe <0123456789@student.vgu.edu.vn>", None))
        self.receivedEmailTitle.setText(QCoreApplication.translate("mailWindow", u"Calling for Volunteers!", None))
        self.receivedEmailContent.setHtml(QCoreApplication.translate("mailWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("mailWindow", u"You are disconnected from the Internet.", None))
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("mailWindow", u"Email Sent!", None))
        self.addressField.setPlaceholderText(QCoreApplication.translate("mailWindow", u"To", None))
        self.titleField.setText("")
        self.titleField.setPlaceholderText(QCoreApplication.translate("mailWindow", u"Title", None))
        self.contentField.setPlaceholderText(QCoreApplication.translate("mailWindow", u"Content...", None))
        self.discardEmailButton.setText(QCoreApplication.translate("mailWindow", u"Discard", None))
        self.sendEmailButton.setText(QCoreApplication.translate("mailWindow", u"Send", None))
    # retranslateUi

