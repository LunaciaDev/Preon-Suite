class Task1:
    def __init__(self):
        self.data = 0

    def setData(self, data):
        self.data = data

    def taskRun(self):
        self.data += 1
        print("Task 1 done")

temp = Task1
temp.taskRun()