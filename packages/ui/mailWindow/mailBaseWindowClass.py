# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mailBaseWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_mailBaseWindow(object):
    def setupUi(self, mailBaseWindow):
        if not mailBaseWindow.objectName():
            mailBaseWindow.setObjectName(u"mailBaseWindow")
        mailBaseWindow.resize(1080, 720)
        self.horizontalLayout = QHBoxLayout(mailBaseWindow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(mailBaseWindow)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.retranslateUi(mailBaseWindow)

        QMetaObject.connectSlotsByName(mailBaseWindow)
    # setupUi

    def retranslateUi(self, mailBaseWindow):
        mailBaseWindow.setWindowTitle(QCoreApplication.translate("mailBaseWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("mailBaseWindow", u"This is da mail window", None))
    # retranslateUi

