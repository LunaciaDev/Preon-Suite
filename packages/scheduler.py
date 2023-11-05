import time
from PySide6.QtCore import QObject, Slot, QTimer, Signal

from packages.GmailTask import GmailTask

class Task():
    def __init__(self, _pTask, _Delay, _Period):
        self.pTask = _pTask
        self.Delay = _Delay
        self.Period = _Period

    pTask = None
    Delay = 0
    Period = 0
    RunMe = 0
    TaskID = -1

class Scheduler():
    TICK = 5000
    SCH_MAX_TASKS = 40
    SCH_tasks_G = []
    current_index_task = 0

    def __init__(self):
        return

    def SCH_Init(self):
        self.current_index_task = 0

    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        if self.current_index_task < self.SCH_MAX_TASKS:
            aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
            aTask.TaskID = self.current_index_task
            self.SCH_tasks_G.append(aTask)
            self.current_index_task += 1
        else:
            print("PrivateTasks are full!!!")

    def SCH_Update(self):
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].Delay > 0:
                self.SCH_tasks_G[i].Delay -= 1
            else:
                self.SCH_tasks_G[i].Delay = self.SCH_tasks_G[i].Period
                self.SCH_tasks_G[i].RunMe += 1

    def SCH_Dispatch_Tasks(self):
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].RunMe > 0:
                self.SCH_tasks_G[i].RunMe -= 1
                self.SCH_tasks_G[i].pTask()

    def SCH_Delete(self, aTask):
        return

    def SCH_GenerateID(self):
        return -1

class SchedulerController(QObject):
    def __init__(self):
        super(SchedulerController, self).__init__()
        self.mailTask = GmailTask()
        self.scheduler = Scheduler()
        self.stopTimer = False

        self.scheduler.SCH_Init()

        self.scheduler.SCH_Add_Task(self.mailTask.CheckInbox, 0, 60) # 5 mins

    def run(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.triggerScheduler)
        self.timer.start(5000)
    
    @Slot()
    def triggerScheduler(self):
        self.scheduler.SCH_Update()
        self.scheduler.SCH_Dispatch_Tasks()

    @Slot()
    def terminateThread(self):
        self.timer.stop()