# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reminderWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QToolButton, QVBoxLayout, QWidget)

class Ui_reminderWindow(object):
    def setupUi(self, reminderWindow):
        if not reminderWindow.objectName():
            reminderWindow.setObjectName(u"reminderWindow")
        reminderWindow.resize(1080, 720)
        self.verticalLayout = QVBoxLayout(reminderWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(reminderWindow)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addReminderButton = QToolButton(reminderWindow)
        self.addReminderButton.setObjectName(u"addReminderButton")
        self.addReminderButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.addReminderButton)

        self.editReminderButton = QToolButton(reminderWindow)
        self.editReminderButton.setObjectName(u"editReminderButton")
        self.editReminderButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.editReminderButton)

        self.removeReminderButton = QToolButton(reminderWindow)
        self.removeReminderButton.setObjectName(u"removeReminderButton")
        self.removeReminderButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.removeReminderButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.reminderTable = QTableWidget(reminderWindow)
        if (self.reminderTable.columnCount() < 4):
            self.reminderTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.reminderTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.reminderTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.reminderTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.reminderTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.reminderTable.setObjectName(u"reminderTable")
        self.reminderTable.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.reminderTable.setFocusPolicy(Qt.NoFocus)
        self.reminderTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.reminderTable.setAutoScroll(False)
        self.reminderTable.setAutoScrollMargin(0)
        self.reminderTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.reminderTable.setTabKeyNavigation(False)
        self.reminderTable.setProperty("showDropIndicator", False)
        self.reminderTable.setDragDropOverwriteMode(False)
        self.reminderTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.reminderTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.reminderTable.setShowGrid(False)
        self.reminderTable.setGridStyle(Qt.SolidLine)
        self.reminderTable.setSortingEnabled(False)
        self.reminderTable.setCornerButtonEnabled(False)
        self.reminderTable.setRowCount(0)
        self.reminderTable.setColumnCount(4)
        self.reminderTable.horizontalHeader().setVisible(True)
        self.reminderTable.horizontalHeader().setHighlightSections(False)
        self.reminderTable.horizontalHeader().setStretchLastSection(True)
        self.reminderTable.verticalHeader().setVisible(False)
        self.reminderTable.verticalHeader().setMinimumSectionSize(30)
        self.reminderTable.verticalHeader().setDefaultSectionSize(40)
        self.reminderTable.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.reminderTable)


        self.retranslateUi(reminderWindow)

        QMetaObject.connectSlotsByName(reminderWindow)
    # setupUi

    def retranslateUi(self, reminderWindow):
        reminderWindow.setWindowTitle(QCoreApplication.translate("reminderWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("reminderWindow", u"Here are your reminders:", None))
        self.addReminderButton.setText(QCoreApplication.translate("reminderWindow", u"Add New Reminder", None))
        self.editReminderButton.setText(QCoreApplication.translate("reminderWindow", u"Edit Selected Reminder", None))
        self.removeReminderButton.setText(QCoreApplication.translate("reminderWindow", u"Remove Selected Reminder", None))
        ___qtablewidgetitem = self.reminderTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("reminderWindow", u"Date", None));
        ___qtablewidgetitem1 = self.reminderTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("reminderWindow", u"Time", None));
        ___qtablewidgetitem2 = self.reminderTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("reminderWindow", u"Title", None));
        ___qtablewidgetitem3 = self.reminderTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("reminderWindow", u"Description", None));
    # retranslateUi

