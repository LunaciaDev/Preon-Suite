from PySide6.QtWidgets import QWidget
from packages.ui.weatherWindowClass import Ui_weatherWindow

class WeatherWindow(QWidget):
    def __init__(self):
        super(WeatherWindow, self).__init__()
        self.ui = Ui_weatherWindow()
        self.ui.setupUi(self)