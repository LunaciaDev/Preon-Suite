import time
from PySide6.QtCore import QObject, Slot, QTimer

from packages.GmailTask import GmailTask
from packages.taskWeather import taskWeather as WeatherTask
from packages.reminderClass import ReminderManager

class Scheduler(QObject):

    def __init__(self, thread):
        super(Scheduler, self).__init__()
        self.myThread = thread

        self.mailTask = GmailTask()
        self.mailTask.moveToThread(thread)

        self.weatherTask = WeatherTask()
        self.weatherTask.moveToThread(thread)

        self.reminderTask = ReminderManager()
        self.reminderTask.moveToThread(thread)

        self.taskList = [
            (self.mailTask.CheckInbox, 300000), # 5mins CD every run
            (self.weatherTask.getData, 300000),  # 5mins CD every run
            (self.reminderTask.system_notify, 60000) # 1min CD every run
        ]
        self.clockList = []

    def run(self):
        for task in self.taskList:
            temp = QTimer(self)
            temp.timeout.connect(task[0])
            temp.start(task[1])
            self.clockList.append(temp)
    
    @Slot()
    def terminateThread(self):
        self.reminderTask.save_reminders()
        for clock in self.clockList:
            clock.stop()
        self.myThread.quit()