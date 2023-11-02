from PySide6.QtCore import Qt, Slot, Signal, QDate, QTime
from PySide6.QtWidgets import QDialog

from packages.ui.reminderDialogClass import Ui_reminderDialog

class ReminderDialog(QDialog):
    dialogAccepted = Signal(QDate, QTime, str, str)

    def __init__(self, titleLookup, ignoreTitle):
        super(ReminderDialog, self).__init__()
        self.ui = Ui_reminderDialog()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        
        self.ui.reminderErrorLabel.hide()

        self.titleLookup = titleLookup
        self.ignoreTitle = ignoreTitle

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
            if (self.ui.reminderTitle.text() != self.ignoreTitle):
                self.ui.reminderErrorLabel.setText("Title is already used!")
                self.ui.reminderErrorLabel.show()
                return
        
        self.dialogAccepted.emit(self.ui.reminderDate.date(), self.ui.reminderTime.time(), 
                                 self.ui.reminderTitle.text(), self.ui.reminderDescription.text())
        super().accept()
    
    @Slot()
    def reject(self):
        super().reject()
