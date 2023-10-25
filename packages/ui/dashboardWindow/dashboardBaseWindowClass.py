# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardBaseWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_dashboardBaseWindow(object):
    def setupUi(self, dashboardBaseWindow):
        if not dashboardBaseWindow.objectName():
            dashboardBaseWindow.setObjectName(u"dashboardBaseWindow")
        dashboardBaseWindow.resize(1080, 720)
        self.verticalLayout = QVBoxLayout(dashboardBaseWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(dashboardBaseWindow)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(dashboardBaseWindow)

        QMetaObject.connectSlotsByName(dashboardBaseWindow)
    # setupUi

    def retranslateUi(self, dashboardBaseWindow):
        dashboardBaseWindow.setWindowTitle(QCoreApplication.translate("dashboardBaseWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("dashboardBaseWindow", u"This is da dashboard", None))
    # retranslateUi

