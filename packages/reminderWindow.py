from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Slot, QDate, QTime, Signal, QTimer

from packages.ui.reminderWindowClass import Ui_reminderWindow

from packages.reminderDialog import ReminderDialog

class ReminderWindow(QWidget):
    removeReminder = Signal(int)
    addReminder = Signal(str, str, str, str)
    editReminder = Signal(int, str, str, str, str)
    saveToMarkdown = Signal()

    def __init__(self):
        super(ReminderWindow, self).__init__()
        self.ui = Ui_reminderWindow()
        self.ui.setupUi(self)

        self.popupTimer = QTimer(self)
        self.popupTimer.setSingleShot(True)
        self.popupTimer.timeout.connect(self.hideAllPopup)

        self.ui.addReminderButton.clicked.connect(self.onAddReminderButtonClicked)
        self.ui.removeReminderButton.clicked.connect(self.onRemoveSelectedReminderButtonClicked)
        self.ui.editReminderButton.clicked.connect(self.onEditSelectedReminderButtonClicked)
        self.ui.reminderTable.cellClicked.connect(self.onRowSelected)
        self.ui.exportMarkdownButton.clicked.connect(self.onExportMarkdownButtonClicked)

        self.ui.removeReminderButton.setEnabled(False)
        self.ui.editReminderButton.setEnabled(False)
        self.hideAllPopup()

        # Doing nasty hacks to the table since I can't do it in QDesigner
        self.ui.reminderTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # Prepare a title list for dialog lookup
        self.reminderList = []
        self.reminderTitleList = []

    def disableEditRemove(self):
        self.ui.removeReminderButton.setEnabled(False)
        self.ui.editReminderButton.setEnabled(False)

    def errorPopup(self, errorMsg):
        self.ui.errorPopup.setText(errorMsg)
        self.ui.errorPopup.show()
        self.popupTimer.start(3000)

    def successPopup(self, successMsg):
        self.ui.successPopup.setText(successMsg)
        self.ui.successPopup.show()
        self.popupTimer.start(3000)

    @Slot()
    def hideAllPopup(self):
        self.ui.errorPopup.hide()
        self.ui.successPopup.hide()

    # UI Control
    @Slot(bool)
    def onMarkdownExported(self, success):
        if success:
            self.successPopup("Exported reminders to markdown")
        else:
            self.errorPopup("Failed to export to markdown")

    @Slot()
    def onExportMarkdownButtonClicked(self):
        self.saveToMarkdown.emit()

    @Slot()
    def onAddReminderButtonClicked(self):
        self.disableEditRemove()
        dialog = ReminderDialog(None)
        dialog.dialogAccepted.connect(self.onDialogFinish)
        dialog.exec()

    @Slot()
    def onRemoveSelectedReminderButtonClicked(self):
        self.removeReminder.emit(self.ui.reminderTable.currentRow())

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
        strDate = f"{str(date.day()).zfill(2)}/{str(date.month()).zfill(2)}/{date.year()}"
        strTime = f"{str(time.hour()).zfill(2)}:{str(time.minute()).zfill(2)}"

        if table.currentRow() == -1:
            self.addReminder.emit(title, description, strDate, strTime)
            return

        #Edit a reminder entry
        self.editReminder.emit(table.currentRow(), title, description, strDate, strTime)

    @Slot(list)
    def refreshReminders(self, reminderList):
        table = self.ui.reminderTable
        currentRow = 0

        self.reminderList = reminderList
        self.reminderTitleList = []

        table.setRowCount(0)
        self.disableEditRemove()

        for item in reminderList:
            table.insertRow(currentRow)
            table.setItem(currentRow, 0, QTableWidgetItem(item.get_date()))
            table.setItem(currentRow, 1, QTableWidgetItem(item.get_time()))
            table.setItem(currentRow, 2, QTableWidgetItem(item.get_title()))
            table.setItem(currentRow, 3, QTableWidgetItem(item.get_description()))
            self.reminderTitleList.append(item.get_title)
            currentRow += 1