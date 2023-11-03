from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Slot, QDate, QTime

from packages.ui.reminderWindowClass import Ui_reminderWindow

from packages.reminderDialog import ReminderDialog

class ReminderWindow(QWidget):
    def __init__(self):
        super(ReminderWindow, self).__init__()
        self.ui = Ui_reminderWindow()
        self.ui.setupUi(self)

        self.ui.addReminderButton.clicked.connect(self.onAddReminderButtonClicked)
        self.ui.removeReminderButton.clicked.connect(self.onRemoveSelectedReminderButtonClicked)
        self.ui.editReminderButton.clicked.connect(self.onEditSelectedReminderButtonClicked)
        self.ui.reminderTable.cellClicked.connect(self.onRowSelected)

        self.ui.removeReminderButton.setEnabled(False)
        self.ui.editReminderButton.setEnabled(False)

        # Doing nasty hacks to the table since I can't do it in QDesigner
        self.ui.reminderTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # Prepare a title list for dialog lookup
        # hook up to back end to fetch the list of reminders
        # probably need another signal
        self.reminderList = []

    # UI Control
    @Slot()
    def onAddReminderButtonClicked(self):
        self.ui.reminderTable.setCurrentCell(-1, -1)
        dialog = ReminderDialog(None)
        dialog.dialogAccepted.connect(self.onDialogFinish)
        dialog.exec()

    @Slot()
    def onRemoveSelectedReminderButtonClicked(self):
        #remove it from back-end
        self.ui.reminderTable.removeRow(self.ui.reminderTable.currentRow())
        self.ui.reminderTable.setCurrentCell(-1, -1)
        self.ui.removeReminderButton.setEnabled(False)
        self.ui.editReminderButton.setEnabled(False)

    @Slot()
    def onEditSelectedReminderButtonClicked(self):
        dialog = ReminderDialog(self.reminderList[self.ui.reminderTable.currentRow()])
        dialog.dialogAccepted.connect(self.onDialogFinish)
        dialog.exec()

    @Slot(int, int)
    def onRowSelected(self, row, column):
        self.ui.removeReminderButton.setEnabled(True)
        self.ui.editReminderButton.setEnabled(True)

    @Slot(QDate, QTime, str, str)
    def onDialogFinish(self, date, time, title, description):
        table = self.ui.reminderTable
        strDate = f"{str(date.day()).zfill(2)}-{str(date.month()).zfill(2)}-{date.year()}"
        strTime = f"{str(time.hour()).zfill(2)}:{str(time.minute()).zfill(2)}"

        if table.currentRow() == -1:
            #Add a reminder entry
            self.reminderList.append({"title": title, "description": description, "time": strTime, "date": strDate})
            endRow = table.rowCount()
            table.insertRow(endRow)
            table.setItem(endRow, 0, QTableWidgetItem(f"{str(date.day()).zfill(2)}/{str(date.month()).zfill(2)}/{date.year()}"))
            table.setItem(endRow, 1, QTableWidgetItem(strTime))
            table.setItem(endRow, 2, QTableWidgetItem(title))
            table.setItem(endRow, 3, QTableWidgetItem(description))
            return

        #Edit a reminder entry
        self.reminderList[table.currentRow()] = {"title": title, "description": description, "time": strTime, "date": strDate}
        table.setItem(table.currentRow(), 0, QTableWidgetItem(f"{str(date.day()).zfill(2)}/{str(date.month()).zfill(2)}/{date.year()}"))
        table.setItem(table.currentRow(), 1, QTableWidgetItem(strTime))
        table.setItem(table.currentRow(), 2, QTableWidgetItem(title))
        table.setItem(table.currentRow(), 3, QTableWidgetItem(description))