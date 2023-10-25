# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'passwordBaseWindow.ui'
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

class Ui_passwordBaseWindow(object):
    def setupUi(self, passwordBaseWindow):
        if not passwordBaseWindow.objectName():
            passwordBaseWindow.setObjectName(u"passwordBaseWindow")
        passwordBaseWindow.resize(1080, 720)
        self.horizontalLayout = QHBoxLayout(passwordBaseWindow)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.passwordWindowStack = QStackedWidget(passwordBaseWindow)
        self.passwordWindowStack.setObjectName(u"passwordWindowStack")

        self.horizontalLayout.addWidget(self.passwordWindowStack)


        self.retranslateUi(passwordBaseWindow)

        QMetaObject.connectSlotsByName(passwordBaseWindow)
    # setupUi

    def retranslateUi(self, passwordBaseWindow):
        passwordBaseWindow.setWindowTitle(QCoreApplication.translate("passwordBaseWindow", u"Form", None))
    # retranslateUi

