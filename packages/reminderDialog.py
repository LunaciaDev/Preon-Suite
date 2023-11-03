from PySide6.QtCore import Qt, Slot, Signal, QDate, QTime
from PySide6.QtWidgets import QDialog

from packages.ui.reminderDialogClass import Ui_reminderDialog

class ReminderDialog(QDialog):
    dialogAccepted = Signal(QDate, QTime, str, str)

    def __init__(self, ignoredReminderObject):
        super(ReminderDialog, self).__init__()
        self.ui = Ui_reminderDialog()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        
        self.ui.reminderErrorLabel.hide()

        if ignoredReminderObject is None:
            self.ui.reminderDate.setDate(QDate.currentDate())
            self.ui.reminderTime.setTime(QTime.currentTime())
            self.ui.label_5.setText("Creating reminder")
            self.setWindowTitle("Creating reminder")
        else:
            self.ui.label_5.setText("Editing reminder")
            self.setWindowTitle("Editing reminder")
            temp = ignoredReminderObject["date"].strip().split("-")
            self.ui.reminderDate.setDate(QDate(int(temp[2]), int(temp[1]), int(temp[0])))
            temp = ignoredReminderObject["time"].strip().split(":")
            self.ui.reminderTime.setTime(QTime(int(temp[0]), int(temp[1])))
            self.ui.reminderTitle.setText(ignoredReminderObject["title"])
            self.ui.reminderDescription.setText(ignoredReminderObject["description"])

        self.ignoredReminderObject = ignoredReminderObject

    @Slot()
    def accept(self):
        if (self.ui.reminderTitle.text() == ""):
            self.ui.reminderErrorLabel.setText("Title must not be empty")
            self.ui.reminderErrorLabel.show()
            return
        
        try:
            self.titleLookup.index(self.ui.reminderTitle.text())
        except:
            #Do nothing if it found a match
            pass
        else:
            #Executed if a match is found
            if (self.ui.reminderTitle.text() != self.ignoredReminderObject["title"]):
                self.ui.reminderErrorLabel.setText("Title is already used!")
                self.ui.reminderErrorLabel.show()
                return
        
        self.dialogAccepted.emit(self.ui.reminderDate.date(), self.ui.reminderTime.time(), 
                                 self.ui.reminderTitle.text(), self.ui.reminderDescription.text())
        super().accept()
    
    @Slot()
    def reject(self):
        super().reject()
