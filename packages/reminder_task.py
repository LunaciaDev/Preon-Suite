import os
import time
from reminderClass import Reminder, ReminderManager
import threading

# Start up
os.system("clear")
reminder_list = ReminderManager()
reminder_list.load_reminders('reminders')
flag = threading.Event()
def TUI():
    # TUI
    while not flag.is_set():
        print("\nCURRENT REMINDERS: ")
        print("---------------\n")
        if reminder_list.is_empty():
            print("There is no reminder.\n")
            print("---------------\n")

        else:
            reminder_list.display_reminders()
            print("---------------\n")




        print("What do you want to do?")
        print("  0: exit")
        print("  1: Add new reminders.")
        print("  2: Remove reminders.")
        



        MainRequest=input("Input: ")

        os.system("clear")
        match MainRequest:
            # Add reminders
            case "1":
                sameName=1
                while sameName == 1:
                    Title = input("Title: ")
                    if reminder_list.is_same_name(Title):
                        os.system('clear')
                        print("Title already used")
                        sameName=1
                    else:
                        Description = input("Description: ")
                        Date = input("Date: ")

                        Time = input("Time: ")
                        reminder_list.add_reminder(Title,Description,  Date, Time)
                        reminder_list.display_reminders()
                        print("\n---------------\n")
                        sameName=0
                        reminder_list.sort_reminders()
                        os.system("clear")


            # Remove reminders
            case "2":
                print("Which reminder do you want to remove: ")
                reminder_list.display_reminders()
                print("Enter title: ")
                remove = input()
                reminder_list.remove_reminder(remove)
                reminder_list.display_reminders()
                print("\n---------------\n")
                os.system("clear")


            # Exit
            case "0":
                os.system("clear")
                print("Exiting...")
                print("Might take a few seconds...")
                flag.set()
                break



def Notify():
    while not flag.is_set():
        reminder_list.system_notify()



thread1 = threading.Thread(target = TUI)
thread2 = threading.Thread(target = Notify)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

reminder_list.save_reminders('reminders')



