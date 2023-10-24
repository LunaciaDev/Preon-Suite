class Task1(QObject):
    def __init__(self):
        super(Task1, self).__init__()
        self.data = 0

    def setData(self, data):
        self.data = data
        self.emitData.emit(1, self.data)

    def taskRun(self):
        self.data += 1
        self.emitData.emit(1, self.data)
        print("Task 1 done")
