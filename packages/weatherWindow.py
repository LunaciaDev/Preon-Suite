from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot, QSize, QDateTime

from packages.ui.weatherWindowClass import Ui_weatherWindow

class WeatherWindow(QWidget):
    voiceAssistantClicked = Signal()

    def __init__(self):
        super(WeatherWindow, self).__init__()
        self.ui = Ui_weatherWindow()
        self.ui.setupUi(self)

        self.directionLookup = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        
        self.ui.openWeatherIcon.setIcon(QIcon("./icons/openWeather.svg").pixmap(QSize(69, 34)))
        self.ui.openWeatherIcon.setIconSize(QSize(69, 34))
        self.ui.openWeatherIcon.clicked.connect(self.onOpenWeatherLinkClicked)

    @Slot()
    def onVoiceAssistantClicked(self):
        # push it to backend
        pass

    @Slot()
    def onOpenWeatherLinkClicked(self):
        QDesktopServices.openUrl("https://openweathermap.org/")

    @Slot(dict, list)
    def onReceiveWeatherData(self, currentWeather, forecastedWeather):
        #hard coding time!
        #even through the UI has structure, it's rough..

        self.ui.temperatureLabel.setText(f"{int(currentWeather['temp'])}°C")
        self.ui.perceivedTempLabel.setText(f"Feels like {int(currentWeather['feels_like'])}°C")
        self.ui.weatherTypeLabel.setText(currentWeather['description'].title())
        self.ui.windSpeedLabel.setText(f"Wind: {self.directionLookup[int(currentWeather['windDeg'] / 45)]} {currentWeather['wind_speed']} m/s")
        self.ui.minMaxTempLabel.setText(f"H: {int(currentWeather['temp_max'])}°C L: {int(currentWeather['temp_min'])}°C")
        self.ui.humidityLabel.setText(f"Humidity: {currentWeather['humidity']}%")
        self.ui.weatherIcon.setPixmap(QIcon(self.getWeatherIconName(currentWeather['icon'])).pixmap(QSize(300, 300)))

        self.ui.forecastTempLabel_1.setText(f"{int(forecastedWeather[0]['temp'])}°C")
        self.ui.forecastPerceivedLabel_1.setText(forecastedWeather[0]['description'].title())
        self.ui.forecastHighLowTempLabel_1.setText(f"H: {int(forecastedWeather[0]['temp_max'])}°C L: {int(forecastedWeather[0]['temp_min'])}°C")
        self.ui.forecastDateLabel_1.setText(f"{forecastedWeather[0]['dt_txt'][8:10]}/{forecastedWeather[0]['dt_txt'][5:7]}")
        self.ui.forecastTimeLabel_1.setText(f"{forecastedWeather[0]['dt_txt'][11:16]}")
        self.ui.forecastWeatherIcon_1.setPixmap(QIcon(self.getWeatherIconName(forecastedWeather[0]['icon'])).pixmap(QSize(100, 100)))

        self.ui.forecastTempLabel_2.setText(f"{int(forecastedWeather[1]['temp'])}°C")
        self.ui.forecastPerceivedLabel_2.setText(forecastedWeather[1]['description'].title())
        self.ui.forecastHighLowTempLabel_2.setText(f"H: {int(forecastedWeather[1]['temp_max'])}°C L: {int(forecastedWeather[1]['temp_min'])}°C")
        self.ui.forecastDateLabel_2.setText(f"{forecastedWeather[1]['dt_txt'][8:10]}/{forecastedWeather[1]['dt_txt'][5:7]}")
        self.ui.forecastTimeLabel_2.setText(f"{forecastedWeather[1]['dt_txt'][11:16]}")
        self.ui.forecastWeatherIcon_2.setPixmap(QIcon(self.getWeatherIconName(forecastedWeather[1]['icon'])).pixmap(QSize(100, 100)))

        self.ui.forecastTempLabel_3.setText(f"{int(forecastedWeather[2]['temp'])}°C")
        self.ui.forecastPerceivedLabel_3.setText(forecastedWeather[2]['description'].title())
        self.ui.forecastHighLowTempLabel_3.setText(f"H: {int(forecastedWeather[2]['temp_max'])}°C L: {int(forecastedWeather[2]['temp_min'])}°C")
        self.ui.forecastDateLabel_3.setText(f"{forecastedWeather[2]['dt_txt'][8:10]}/{forecastedWeather[2]['dt_txt'][5:7]}")
        self.ui.forecastTimeLabel_3.setText(f"{forecastedWeather[2]['dt_txt'][11:16]}")
        self.ui.forecastWeatherIcon_3.setPixmap(QIcon(self.getWeatherIconName(forecastedWeather[2]['icon'])).pixmap(QSize(100, 100)))

        self.ui.forecastTempLabel_4.setText(f"{int(forecastedWeather[3]['temp'])}°C")
        self.ui.forecastPerceivedLabel_4.setText(forecastedWeather[3]['description'].title())
        self.ui.forecastHighLowTempLabel_4.setText(f"H: {int(forecastedWeather[3]['temp_max'])}°C L: {int(forecastedWeather[3]['temp_min'])}°C")
        self.ui.forecastDateLabel_4.setText(f"{forecastedWeather[3]['dt_txt'][8:10]}/{forecastedWeather[3]['dt_txt'][5:7]}")
        self.ui.forecastTimeLabel_4.setText(f"{forecastedWeather[3]['dt_txt'][11:16]}")
        self.ui.forecastWeatherIcon_4.setPixmap(QIcon(self.getWeatherIconName(forecastedWeather[3]['icon'])).pixmap(QSize(100, 100)))

        self.ui.forecastTempLabel_5.setText(f"{int(forecastedWeather[4]['temp'])}°C")
        self.ui.forecastPerceivedLabel_5.setText(forecastedWeather[4]['description'].title())
        self.ui.forecastHighLowTempLabel_5.setText(f"H: {int(forecastedWeather[4]['temp_max'])}°C L: {int(forecastedWeather[4]['temp_min'])}°C")
        self.ui.forecastDateLabel_5.setText(f"{forecastedWeather[4]['dt_txt'][8:10]}/{forecastedWeather[4]['dt_txt'][5:7]}")
        self.ui.forecastTimeLabel_5.setText(f"{forecastedWeather[4]['dt_txt'][11:16]}")
        self.ui.forecastWeatherIcon_5.setPixmap(QIcon(self.getWeatherIconName(forecastedWeather[4]['icon'])).pixmap(QSize(100, 100)))

        self.ui.forecastTempLabel_6.setText(f"{int(forecastedWeather[5]['temp'])}°C")
        self.ui.forecastPerceivedLabel_6.setText(forecastedWeather[5]['description'].title())
        self.ui.forecastHighLowTempLabel_6.setText(f"H: {int(forecastedWeather[5]['temp_max'])}°C L: {int(forecastedWeather[5]['temp_min'])}°C")
        self.ui.forecastDateLabel_6.setText(f"{forecastedWeather[5]['dt_txt'][8:10]}/{forecastedWeather[5]['dt_txt'][5:7]}")
        self.ui.forecastTimeLabel_6.setText(f"{forecastedWeather[5]['dt_txt'][11:16]}")
        self.ui.forecastWeatherIcon_6.setPixmap(QIcon(self.getWeatherIconName(forecastedWeather[5]['icon'])).pixmap(QSize(100, 100)))


    def getWeatherIconName(self, iconName):
        if (iconName[1] == '3' or iconName[1] == '4'):
            iconName = f"02{iconName[2]}"

        return f"./icons/{iconName}.svg"