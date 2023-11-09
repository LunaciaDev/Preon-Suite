from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot, QSize, QDate

from packages.ui.weatherWindowClass import Ui_weatherWindow

class WeatherWindow(QWidget):
    voiceAssistantClicked = Signal()

    def __init__(self):
        super(WeatherWindow, self).__init__()
        self.ui = Ui_weatherWindow()
        self.ui.setupUi(self)

        self.directionLookup = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        
        self.dummyCurrentWeather = {
            "description": "overcast clouds",
            "icon": "04n",
            "temp": 24.89,
            "feels_like": 25.86,
            "temp_min": 24.89,
            "temp_max": 24.89,
            "humidity": 93,
            "windSpeed": 1.48,
            "windDeg": 312
        }
        self.dummyPredictedWeather = [
        {
            "temp": 27.61,
            "feels_like": 31.41,
            "temp_min": 27.61,
            "temp_max": 27.61,
            "humidity": 82,
            "description": "broken clouds",
            "icon": "04d",
            "dt_txt": "2023-11-09 09:00:00"
        },
        {
            "temp": 27.2,
            "feels_like": 30.73,
            "temp_min": 27.2,
            "temp_max": 27.2,
            "humidity": 85,
            "description": "light rain",
            "icon": "10d",
            "dt_txt": "2023-11-10 09:00:00"
        },
        {
            "temp": 27.74,
            "feels_like": 31.6,
            "temp_min": 27.74,
            "temp_max": 27.74,
            "humidity": 81,
            "description": "broken clouds",
            "icon": "04d",
            "dt_txt": "2023-11-11 09:00:00"
        },
        {
            "temp": 26.99,
            "feels_like": 30.3,
            "temp_min": 26.99,
            "temp_max": 26.99,
            "humidity": 86,
            "description": "light rain",
            "icon": "10d",
            "dt_txt": "2023-11-12 09:00:00"
        },
        {
            "temp": 23.93,
            "feels_like": 24.91,
            "temp_min": 23.93,
            "temp_max": 23.93,
            "humidity": 97,
            "description": "heavy intensity rain",
            "icon": "10d",
            "dt_txt": "2023-11-13 09:00:00"
        }
    ]

        self.ui.openWeatherIcon.setIcon(QIcon("./icons/openWeather.svg").pixmap(QSize(69, 34)))
        self.ui.openWeatherIcon.setIconSize(QSize(69, 34))
        self.ui.openWeatherIcon.clicked.connect(self.onOpenWeatherLinkClicked)

        self.onReceiveWeatherData(self.dummyCurrentWeather, self.dummyPredictedWeather)

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
        self.ui.windSpeedLabel.setText(f"{self.directionLookup[int(round(currentWeather['windDeg'] / 45))]} {currentWeather['windSpeed']} m/s")
        self.ui.minMaxTempLabel.setText(f"H: {int(currentWeather['temp_max'])}°C L: {int(currentWeather['temp_min'])}°C")
        self.ui.humidityLabel.setText(f"Humidity: {currentWeather['humidity']}%")
        self.ui.weatherIcon.setPixmap(QIcon(self.getWeatherIconName(currentWeather['icon'])).pixmap(QSize(300, 300)))

        timekeeper = QDate.currentDate().addDays(1)

        self.ui.forecastTempLabel_1.setText(f"{int(forecastedWeather[0]['temp'])}°C")
        self.ui.forecastPerceivedLabel_1.setText(forecastedWeather[0]['description'].title())
        self.ui.forecastHighLowTempLabel_1.setText(f"H: {int(forecastedWeather[0]['temp_max'])}°C L: {int(forecastedWeather[0]['temp_min'])}°C")
        self.ui.forecastDateLabel_1.setText(f"{str(timekeeper.day()).zfill(2)}/{str(timekeeper.month()).zfill(2)}")
        self.ui.forecastWeatherIcon_1.setPixmap(QIcon(self.getWeatherIconName(forecastedWeather[0]['icon'])).pixmap(QSize(100, 100)))

        timekeeper = timekeeper.addDays(1)

        self.ui.forecastTempLabel_2.setText(f"{int(forecastedWeather[1]['temp'])}°C")
        self.ui.forecastPerceivedLabel_2.setText(forecastedWeather[1]['description'].title())
        self.ui.forecastHighLowTempLabel_2.setText(f"H: {int(forecastedWeather[1]['temp_max'])}°C L: {int(forecastedWeather[1]['temp_min'])}°C")
        self.ui.forecastDateLabel_2.setText(f"{str(timekeeper.day()).zfill(2)}/{str(timekeeper.month()).zfill(2)}")
        self.ui.forecastWeatherIcon_2.setPixmap(QIcon(self.getWeatherIconName(forecastedWeather[1]['icon'])).pixmap(QSize(100, 100)))

        timekeeper = timekeeper.addDays(1)

        self.ui.forecastTempLabel_3.setText(f"{int(forecastedWeather[2]['temp'])}°C")
        self.ui.forecastPerceivedLabel_3.setText(forecastedWeather[2]['description'].title())
        self.ui.forecastHighLowTempLabel_3.setText(f"H: {int(forecastedWeather[2]['temp_max'])}°C L: {int(forecastedWeather[2]['temp_min'])}°C")
        self.ui.forecastDateLabel_3.setText(f"{str(timekeeper.day()).zfill(2)}/{str(timekeeper.month()).zfill(2)}")
        self.ui.forecastWeatherIcon_3.setPixmap(QIcon(self.getWeatherIconName(forecastedWeather[2]['icon'])).pixmap(QSize(100, 100)))

        timekeeper = timekeeper.addDays(1)

        self.ui.forecastTempLabel_4.setText(f"{int(forecastedWeather[3]['temp'])}°C")
        self.ui.forecastPerceivedLabel_4.setText(forecastedWeather[3]['description'].title())
        self.ui.forecastHighLowTempLabel_4.setText(f"H: {int(forecastedWeather[3]['temp_max'])}°C L: {int(forecastedWeather[3]['temp_min'])}°C")
        self.ui.forecastDateLabel_4.setText(f"{str(timekeeper.day()).zfill(2)}/{str(timekeeper.month()).zfill(2)}")
        self.ui.forecastWeatherIcon_4.setPixmap(QIcon(self.getWeatherIconName(forecastedWeather[3]['icon'])).pixmap(QSize(100, 100)))

        timekeeper = timekeeper.addDays(1)

        self.ui.forecastTempLabel_5.setText(f"{int(forecastedWeather[4]['temp'])}°C")
        self.ui.forecastPerceivedLabel_5.setText(forecastedWeather[4]['description'].title())
        self.ui.forecastHighLowTempLabel_5.setText(f"H: {int(forecastedWeather[4]['temp_max'])}°C L: {int(forecastedWeather[4]['temp_min'])}°C")
        self.ui.forecastDateLabel_5.setText(f"{str(timekeeper.day()).zfill(2)}/{str(timekeeper.month()).zfill(2)}")
        self.ui.forecastWeatherIcon_5.setPixmap(QIcon(self.getWeatherIconName(forecastedWeather[4]['icon'])).pixmap(QSize(100, 100)))

    def getWeatherIconName(self, iconName):
        if (iconName[1] == '3' or iconName[1] == '4'):
            iconName = f"02{iconName[2]}"

        return f"./icons/{iconName}.svg"