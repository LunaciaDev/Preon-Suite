from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot
from packages.ui.homeWindowClass import Ui_homeWindow
from packages.mailWindow import MailWindow
from packages.passwordWindow import PasswordWindow
from packages.dashboardWindow import DashboardWindow

class HomeWindow(QWidget):
    def __init__(self):
        super(HomeWindow, self).__init__()
        self.ui = Ui_homeWindow();
        self.ui.setupUi(self)
        
        self.mailWindow = MailWindow()
        self.passwordWindow = PasswordWindow()
        self.dashboardWindow = DashboardWindow()

        self.ui.buttonGroup.setId(self.ui.homeButton, 0)
        self.ui.buttonGroup.setId(self.ui.passwordButton, 1)
        self.ui.buttonGroup.setId(self.ui.mailButton, 2)

        self.ui.homeButton.setChecked(True)

        self.ui.rightPanel.addWidget(self.dashboardWindow)
        self.ui.rightPanel.addWidget(self.passwordWindow)
        self.ui.rightPanel.addWidget(self.mailWindow)
        self.ui.rightPanel.setCurrentIndex(0)

        for button in self.ui.buttonGroup.buttons():
            button.clicked.connect(self.onPanelButtonClicked)

    @Slot()
    def onPanelButtonClicked(self):
        self.ui.rightPanel.setCurrentIndex(self.ui.buttonGroup.checkedId())