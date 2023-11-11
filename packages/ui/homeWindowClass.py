# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_homeWindow(object):
    def setupUi(self, homeWindow):
        if not homeWindow.objectName():
            homeWindow.setObjectName(u"homeWindow")
        homeWindow.setWindowModality(Qt.NonModal)
        homeWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(homeWindow.sizePolicy().hasHeightForWidth())
        homeWindow.setSizePolicy(sizePolicy)
        homeWindow.setMaximumSize(QSize(1280, 720))
        self.horizontalLayout = QHBoxLayout(homeWindow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftPanel = QWidget(homeWindow)
        self.leftPanel.setObjectName(u"leftPanel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftPanel.sizePolicy().hasHeightForWidth())
        self.leftPanel.setSizePolicy(sizePolicy1)
        self.leftPanel.setMinimumSize(QSize(200, 0))
        self.leftPanel.setMaximumSize(QSize(200, 16777215))
        self.leftPanel.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.leftPanel)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.appLabel = QLabel(self.leftPanel)
        self.appLabel.setObjectName(u"appLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.appLabel.sizePolicy().hasHeightForWidth())
        self.appLabel.setSizePolicy(sizePolicy2)
        self.appLabel.setMinimumSize(QSize(0, 225))
        self.appLabel.setMaximumSize(QSize(16777215, 300))
        self.appLabel.setTextFormat(Qt.AutoText)
        self.appLabel.setScaledContents(False)
        self.appLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.appLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.appLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.homeButton = QToolButton(self.leftPanel)
        self.buttonGroup = QButtonGroup(homeWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.homeButton)
        self.homeButton.setObjectName(u"homeButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy3)
        self.homeButton.setMinimumSize(QSize(170, 50))
        self.homeButton.setMaximumSize(QSize(175, 50))
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeButton.setFocusPolicy(Qt.ClickFocus)
        self.homeButton.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u"../icons/emptyIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon)
        self.homeButton.setCheckable(True)
        self.homeButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.homeButton)

        self.mailButton = QToolButton(self.leftPanel)
        self.buttonGroup.addButton(self.mailButton)
        self.mailButton.setObjectName(u"mailButton")
        sizePolicy3.setHeightForWidth(self.mailButton.sizePolicy().hasHeightForWidth())
        self.mailButton.setSizePolicy(sizePolicy3)
        self.mailButton.setMinimumSize(QSize(170, 50))
        self.mailButton.setMaximumSize(QSize(175, 50))
        self.mailButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.mailButton.setFocusPolicy(Qt.ClickFocus)
        self.mailButton.setLayoutDirection(Qt.LeftToRight)
        self.mailButton.setIcon(icon)
        self.mailButton.setCheckable(True)
        self.mailButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.mailButton)

        self.weatherButton = QToolButton(self.leftPanel)
        self.buttonGroup.addButton(self.weatherButton)
        self.weatherButton.setObjectName(u"weatherButton")
        sizePolicy3.setHeightForWidth(self.weatherButton.sizePolicy().hasHeightForWidth())
        self.weatherButton.setSizePolicy(sizePolicy3)
        self.weatherButton.setMinimumSize(QSize(170, 50))
        self.weatherButton.setMaximumSize(QSize(175, 50))
        self.weatherButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.weatherButton.setFocusPolicy(Qt.ClickFocus)
        self.weatherButton.setLayoutDirection(Qt.LeftToRight)
        self.weatherButton.setIcon(icon)
        self.weatherButton.setCheckable(True)
        self.weatherButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.weatherButton)

        self.reminderButton = QToolButton(self.leftPanel)
        self.buttonGroup.addButton(self.reminderButton)
        self.reminderButton.setObjectName(u"reminderButton")
        sizePolicy3.setHeightForWidth(self.reminderButton.sizePolicy().hasHeightForWidth())
        self.reminderButton.setSizePolicy(sizePolicy3)
        self.reminderButton.setMinimumSize(QSize(170, 50))
        self.reminderButton.setMaximumSize(QSize(175, 50))
        self.reminderButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.reminderButton.setFocusPolicy(Qt.ClickFocus)
        self.reminderButton.setLayoutDirection(Qt.LeftToRight)
        self.reminderButton.setIcon(icon)
        self.reminderButton.setCheckable(True)
        self.reminderButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.reminderButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.registerFaceIDButton = QToolButton(self.leftPanel)
        self.registerFaceIDButton.setObjectName(u"registerFaceIDButton")

        self.horizontalLayout_3.addWidget(self.registerFaceIDButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.rightPanel = QStackedWidget(homeWindow)
        self.rightPanel.setObjectName(u"rightPanel")
        sizePolicy3.setHeightForWidth(self.rightPanel.sizePolicy().hasHeightForWidth())
        self.rightPanel.setSizePolicy(sizePolicy3)
        self.rightPanel.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.rightPanel)


        self.retranslateUi(homeWindow)

        QMetaObject.connectSlotsByName(homeWindow)
    # setupUi

    def retranslateUi(self, homeWindow):
        homeWindow.setWindowTitle("")
        self.appLabel.setText(QCoreApplication.translate("homeWindow", u"Preon Suite\\n\"A suite of small things that make life better\"", None))
        self.homeButton.setText(QCoreApplication.translate("homeWindow", u"Home", None))
        self.mailButton.setText(QCoreApplication.translate("homeWindow", u"Mail", None))
        self.weatherButton.setText(QCoreApplication.translate("homeWindow", u"Weather", None))
        self.reminderButton.setText(QCoreApplication.translate("homeWindow", u"Reminders", None))
        self.registerFaceIDButton.setText(QCoreApplication.translate("homeWindow", u"Create Face ID", None))
    # retranslateUi

