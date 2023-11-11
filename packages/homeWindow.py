from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot

from packages.ui.homeWindowClass import Ui_homeWindow

from packages.mailWindow import MailWindow
from packages.dashboardWindow import DashboardWindow
from packages.reminderWindow import ReminderWindow
from packages.weatherWindow import WeatherWindow

class HomeWindow(QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.ui = Ui_homeWindow();
        self.ui.setupUi(self)
        
        self.mailWindow = MailWindow()
        self.dashboardWindow = DashboardWindow()
        self.reminderWindow = ReminderWindow()
        self.weatherWindow = WeatherWindow()

        self.ui.buttonGroup.setId(self.ui.homeButton, 0)
        self.ui.buttonGroup.setId(self.ui.mailButton, 1)
        self.ui.buttonGroup.setId(self.ui.weatherButton, 2)
        self.ui.buttonGroup.setId(self.ui.reminderButton, 3)

        self.ui.homeButton.setChecked(True)

        self.ui.rightPanel.addWidget(self.dashboardWindow)
        self.ui.rightPanel.addWidget(self.mailWindow)
        self.ui.rightPanel.addWidget(self.weatherWindow)
        self.ui.rightPanel.addWidget(self.reminderWindow)
        self.ui.rightPanel.setCurrentIndex(0)

        for button in self.ui.buttonGroup.buttons():
            button.clicked.connect(self.onPanelButtonClicked)

    @Slot()
    def onPanelButtonClicked(self):
        target = self.ui.buttonGroup.checkedId()
        self.ui.rightPanel.setCurrentIndex(target)
