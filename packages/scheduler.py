import time
from PySide6.QtCore import QObject, Slot, QTimer, Signal

from packages.GmailTask import GmailTask

class Scheduler(QObject):
    def __init__(self, thread):
        super(Scheduler, self).__init__()
        self.myThread = thread

        self.mailTask = GmailTask()
        self.mailTask.moveToThread(thread)

        self.taskList = [
            (self.mailTask.CheckInbox, 300000)
        ]
        self.clockList = []

    def run(self):
        print(self.thread)
        for task in self.taskList:
            temp = QTimer(self)
            temp.timeout.connect(task[0])
            temp.start(task[1])
            self.clockList.append(temp)
    
    @Slot()
    def terminateThread(self):
        for clock in self.clockList:
            clock.stop()
        self.myThread.quit()