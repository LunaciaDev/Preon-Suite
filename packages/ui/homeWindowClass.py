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
        self.horizontalLayout = QHBoxLayout(homeWindow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftPanel = QWidget(homeWindow)
        self.leftPanel.setObjectName(u"leftPanel")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftPanel.sizePolicy().hasHeightForWidth())
        self.leftPanel.setSizePolicy(sizePolicy)
        self.leftPanel.setMinimumSize(QSize(180, 0))
        self.leftPanel.setMaximumSize(QSize(200, 16777215))
        self.leftPanel.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.leftPanel)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.appLabel = QLabel(self.leftPanel)
        self.appLabel.setObjectName(u"appLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.appLabel.sizePolicy().hasHeightForWidth())
        self.appLabel.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy2)
        self.homeButton.setMinimumSize(QSize(170, 50))
        self.homeButton.setMaximumSize(QSize(175, 50))
        self.homeButton.setCursor(QCursor(Qt.PointingHandCursor))
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
        sizePolicy2.setHeightForWidth(self.mailButton.sizePolicy().hasHeightForWidth())
        self.mailButton.setSizePolicy(sizePolicy2)
        self.mailButton.setMinimumSize(QSize(170, 50))
        self.mailButton.setMaximumSize(QSize(175, 50))
        self.mailButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.mailButton.setLayoutDirection(Qt.LeftToRight)
        self.mailButton.setIcon(icon)
        self.mailButton.setCheckable(True)
        self.mailButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.mailButton)

        self.weatherButton = QToolButton(self.leftPanel)
        self.buttonGroup.addButton(self.weatherButton)
        self.weatherButton.setObjectName(u"weatherButton")
        sizePolicy2.setHeightForWidth(self.weatherButton.sizePolicy().hasHeightForWidth())
        self.weatherButton.setSizePolicy(sizePolicy2)
        self.weatherButton.setMinimumSize(QSize(170, 50))
        self.weatherButton.setMaximumSize(QSize(175, 50))
        self.weatherButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.weatherButton.setLayoutDirection(Qt.LeftToRight)
        self.weatherButton.setIcon(icon)
        self.weatherButton.setCheckable(True)
        self.weatherButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.weatherButton)

        self.toolButton_7 = QToolButton(self.leftPanel)
        self.buttonGroup.addButton(self.toolButton_7)
        self.toolButton_7.setObjectName(u"toolButton_7")
        sizePolicy2.setHeightForWidth(self.toolButton_7.sizePolicy().hasHeightForWidth())
        self.toolButton_7.setSizePolicy(sizePolicy2)
        self.toolButton_7.setMinimumSize(QSize(170, 50))
        self.toolButton_7.setMaximumSize(QSize(175, 50))
        self.toolButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_7.setLayoutDirection(Qt.LeftToRight)
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setCheckable(True)
        self.toolButton_7.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.toolButton_7)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(5, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.rightPanel = QStackedWidget(homeWindow)
        self.rightPanel.setObjectName(u"rightPanel")
        sizePolicy2.setHeightForWidth(self.rightPanel.sizePolicy().hasHeightForWidth())
        self.rightPanel.setSizePolicy(sizePolicy2)
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
        self.toolButton_7.setText(QCoreApplication.translate("homeWindow", u"TBA", None))
    # retranslateUi

