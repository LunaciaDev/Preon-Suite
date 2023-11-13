import json
from datetime import datetime
from plyer import notification

from PySide6.QtCore import Signal, Slot, QObject

class Reminder:
    def __init__(self, title, description, date, time):
        self.title = title
        self.date = date
        self.time = time
        self.description = description
    
    def get_title(self):
        return self.title
    def set_title(self, title):
         self.title = title

    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description

    def get_time(self):
        return self.time
    def set_time(self, time):
        self.time = time

    def get_date(self):
        return self.date
    def set_date(self, date):
        self.date = date

class ReminderManager(QObject):
    sendReminderList = Signal(list)
    exportedReminder = Signal(bool)

    def __init__(self):
        super(ReminderManager, self).__init__()
        self.reminders = []
    
    @Slot(str, str, str, str)
    def add_reminder(self, title, description, date, time):
        reminder = Reminder(title, description, date, time)
        self.reminders.append(reminder)
        self.sort_reminders()
        self.sendReminderList.emit(self.reminders)
    
    @Slot(int, str, str, str, str)
    def edit_reminder(self, index, title, description, date, time):
        self.reminders[index] = Reminder(title, description, date, time)
        self.sort_reminders()
        self.sendReminderList.emit(self.reminders)
    
    @Slot(int)
    def remove_reminder(self, index):
        self.reminders.pop(index)
        self.sendReminderList.emit(self.reminders)
    
    def sort_reminders(self):
        self.reminders.sort(key=lambda x: x.date)  
        self.reminders.sort(key=lambda d: d.time, reverse = True)

    def save_reminders(self):
        with open('./packages/reminders.json', 'w') as file:
            json.dump([vars(reminder) for reminder in self.reminders], file)

    @Slot()
    def load_reminders(self):
        with open('./packages/reminders.json', 'r') as file:
            data = json.load(file)
            self.reminders = [Reminder(**reminder_data) for reminder_data in data]
        
        self.sendReminderList.emit(self.reminders)

    @Slot()
    def save_to_markdown(self):
        with open('./reminder.md', 'w') as file:
            file.write("# Reminders\n\n")
            for reminder in self.reminders:
                file.write(f"## {reminder.title}\n")
                file.write(f"{reminder.date}\n")
                file.write(f"{reminder.time}\n")
                file.write(f"{reminder.description}\n\n")

        self.exportedReminder.emit(True)

    def system_notify(self):
        now = datetime.now()
        for reminder in self.reminders:
            reminder_datetime = datetime.strptime(f"{reminder.date} {reminder.time}", "%d/%m/%Y %H:%M")               
            if now >= reminder_datetime:
                notification.notify(
                    title = reminder.title,
                    message = reminder.description,
                    timeout = 5
                )
                self.reminders.remove(reminder)
        
        self.sendReminderList.emit(self.reminders)
