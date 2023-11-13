# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'faceIDWindow.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_faceIDWindow(object):
    def setupUi(self, faceIDWindow):
        if not faceIDWindow.objectName():
            faceIDWindow.setObjectName(u"faceIDWindow")
        faceIDWindow.resize(1280, 720)
        self.gridLayout = QGridLayout(faceIDWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_8 = QSpacerItem(20, 77, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(414, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.faceIDCameraFeed = QLabel(faceIDWindow)
        self.faceIDCameraFeed.setObjectName(u"faceIDCameraFeed")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
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

        self.infoLabel = QLabel(faceIDWindow)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.infoLabel)

        self.verticalSpacer_9 = QSpacerItem(20, 160, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)

        self.cancelButton = QToolButton(faceIDWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_4.addWidget(self.cancelButton)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(414, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 26, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 2, 1, 1, 1)


        self.retranslateUi(faceIDWindow)

        QMetaObject.connectSlotsByName(faceIDWindow)
    # setupUi

    def retranslateUi(self, faceIDWindow):
        faceIDWindow.setWindowTitle(QCoreApplication.translate("faceIDWindow", u"Form", None))
        self.faceIDCameraFeed.setText("")
        self.infoLabel.setText(QCoreApplication.translate("faceIDWindow", u"Please keep your face in the camera's view", None))
        self.cancelButton.setText(QCoreApplication.translate("faceIDWindow", u"Cancel", None))
    # retranslateUi

