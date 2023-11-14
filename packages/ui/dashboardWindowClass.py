# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardWindow.ui'
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
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.welcomeMessage = QLabel(dashboardBaseWindow)
        self.welcomeMessage.setObjectName(u"welcomeMessage")
        self.welcomeMessage.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.welcomeMessage)


        self.retranslateUi(dashboardBaseWindow)

        QMetaObject.connectSlotsByName(dashboardBaseWindow)
    # setupUi

    def retranslateUi(self, dashboardBaseWindow):
        dashboardBaseWindow.setWindowTitle(QCoreApplication.translate("dashboardBaseWindow", u"Form", None))
        self.welcomeMessage.setText(QCoreApplication.translate("dashboardBaseWindow", u"TextLabel", None))
    # retranslateUi

