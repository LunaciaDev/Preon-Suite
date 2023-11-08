# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weatherWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

class Ui_weatherWindow(object):
    def setupUi(self, weatherWindow):
        if not weatherWindow.objectName():
            weatherWindow.setObjectName(u"weatherWindow")
        weatherWindow.resize(1080, 720)

        self.retranslateUi(weatherWindow)

        QMetaObject.connectSlotsByName(weatherWindow)
    # setupUi

    def retranslateUi(self, weatherWindow):
        weatherWindow.setWindowTitle(QCoreApplication.translate("weatherWindow", u"Form", None))
    # retranslateUi

