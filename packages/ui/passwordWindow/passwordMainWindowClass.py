# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordMainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_passwordMainWindow(object):
    def setupUi(self, passwordMainWindow):
        if not passwordMainWindow.objectName():
            passwordMainWindow.setObjectName(u"passwordMainWindow")
        passwordMainWindow.resize(1080, 720)
        self.label = QLabel(passwordMainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 340, 261, 21))

        self.retranslateUi(passwordMainWindow)

        QMetaObject.connectSlotsByName(passwordMainWindow)
    # setupUi

    def retranslateUi(self, passwordMainWindow):
        passwordMainWindow.setWindowTitle(QCoreApplication.translate("passwordMainWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("passwordMainWindow", u"Logged In Successfully", None))
    # retranslateUi

