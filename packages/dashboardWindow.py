from PySide6.QtWidgets import QWidget
from packages.ui.dashboardWindowClass import Ui_dashboardBaseWindow

class DashboardWindow(QWidget):
    def __init__(self):
        super(DashboardWindow, self).__init__()
        self.ui = Ui_dashboardBaseWindow()
        self.ui.setupUi(self)