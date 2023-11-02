# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reminderDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QFormLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QSizePolicy, QSpacerItem,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_reminderDialog(object):
    def setupUi(self, reminderDialog):
        if not reminderDialog.objectName():
            reminderDialog.setObjectName(u"reminderDialog")
        reminderDialog.resize(581, 414)
        self.verticalLayout = QVBoxLayout(reminderDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(reminderDialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setScaledContents(False)

        self.horizontalLayout.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.reminderErrorLabel = QLabel(reminderDialog)
        self.reminderErrorLabel.setObjectName(u"reminderErrorLabel")
        self.reminderErrorLabel.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.reminderErrorLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setContentsMargins(12, -1, 12, -1)
        self.label = QLabel(reminderDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.reminderDate = QDateEdit(reminderDialog)
        self.reminderDate.setObjectName(u"reminderDate")
        self.reminderDate.setCalendarPopup(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.reminderDate)

        self.label_2 = QLabel(reminderDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.reminderTime = QTimeEdit(reminderDialog)
        self.reminderTime.setObjectName(u"reminderTime")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.reminderTime)

        self.label_3 = QLabel(reminderDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.reminderTitle = QLineEdit(reminderDialog)
        self.reminderTitle.setObjectName(u"reminderTitle")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.reminderTitle)

        self.label_4 = QLabel(reminderDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.reminderDescription = QLineEdit(reminderDialog)
        self.reminderDescription.setObjectName(u"reminderDescription")
        self.reminderDescription.setMinimumSize(QSize(0, 210))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.reminderDescription)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(reminderDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.reminderDate)
        self.label_2.setBuddy(self.reminderTime)
        self.label_3.setBuddy(self.reminderTitle)
        self.label_4.setBuddy(self.reminderDescription)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.reminderDate, self.reminderTime)
        QWidget.setTabOrder(self.reminderTime, self.reminderTitle)
        QWidget.setTabOrder(self.reminderTitle, self.reminderDescription)

        self.retranslateUi(reminderDialog)
        self.buttonBox.rejected.connect(reminderDialog.reject)
        self.buttonBox.accepted.connect(reminderDialog.accept)

        QMetaObject.connectSlotsByName(reminderDialog)
    # setupUi

    def retranslateUi(self, reminderDialog):
        reminderDialog.setWindowTitle(QCoreApplication.translate("reminderDialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("reminderDialog", u"Editing Reminder", None))
        self.reminderErrorLabel.setText(QCoreApplication.translate("reminderDialog", u"Title must not be empty", None))
        self.label.setText(QCoreApplication.translate("reminderDialog", u"Date", None))
        self.reminderDate.setDisplayFormat(QCoreApplication.translate("reminderDialog", u"dd/MM/yyyy", None))
        self.label_2.setText(QCoreApplication.translate("reminderDialog", u"Time", None))
        self.reminderTime.setDisplayFormat(QCoreApplication.translate("reminderDialog", u"hh:mm", None))
        self.label_3.setText(QCoreApplication.translate("reminderDialog", u"Title", None))
        self.label_4.setText(QCoreApplication.translate("reminderDialog", u"Description", None))
    # retranslateUi

