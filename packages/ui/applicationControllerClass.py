# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'applicationController.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_applicationController(object):
    def setupUi(self, applicationController):
        if not applicationController.objectName():
            applicationController.setObjectName(u"applicationController")
        applicationController.resize(1280, 720)
        self.horizontalLayout = QHBoxLayout(applicationController)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.applicationStack = QStackedWidget(applicationController)
        self.applicationStack.setObjectName(u"applicationStack")

        self.horizontalLayout.addWidget(self.applicationStack)


        self.retranslateUi(applicationController)

        self.applicationStack.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(applicationController)
    # setupUi

    def retranslateUi(self, applicationController):
        applicationController.setWindowTitle(QCoreApplication.translate("applicationController", u"Form", None))
    # retranslateUi

