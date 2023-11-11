import requests #url request lib
from PySide6.QtCore import QTime, Signal, QObject

class taskWeather(QObject):
    sendWeatherData = Signal(dict, list)

    def __init__(self):
        super(taskWeather, self).__init__()
        self.API_KEY = open("./packages/api_key.txt").read()
        #lat and lon for Binh Duong
        self.lat = "11.11039993747999"
        self.lon = "106.61480419825017"
        self.current_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&units=metric&appid={self.API_KEY}"
        self.forecast_URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={self.lat}&lon={self.lon}&units=metric&appid={self.API_KEY}&cnt=40"

        #dict of values for current weather
        self.current = {}
        #list of dict of forecast values for the next 5 days
        self.forecast = []
       
    def getData(self):

        #get current weather data from open weather
        respond = requests.get(self.current_URL).json()
        # read description (eg, cloud, sunny, snow...)
        self.current["description"] = respond['weather'][0]['description']
        self.current["icon"] = respond['weather'][0]['icon']
        #read temp in C
        self.current["temp"] = respond['main']['temp']
        #read how temp feels like (?) in c
        self.current["feels_like"] = respond['main']['feels_like']
        self.current["temp_min"] = respond['main']['temp_min']
        self.current["temp_max"] = respond['main']['temp_max']
        #read humidity in %
        self.current["humidity"] = respond['main']['humidity']
        #read wind speed in m/s
        self.current["wind_speed"] = respond['wind']['speed']
        self.current["windDeg"] = respond['wind']['deg'] 
        #forecast next 5 days
        respond = requests.get(self.forecast_URL).json()
        
        root = 0
        currentTime = QTime.currentTime().hour()
        currentTime -= currentTime % 3

        for item in respond["list"]:

            if int(item["dt_txt"][11:13]) == currentTime:
                break

            root += 1
        
        root += 4

        for i in range(6):
            # root should be the nearest report behind the time the user is in.
            # plus 4 to advance it by 12 hours

            temp ={}
            temp["temp"] = respond["list"][root]["main"]["temp"]
            temp["feels_like"] = respond["list"][root]["main"]["feels_like"]
            temp["temp_min"] = respond["list"][root]["main"]["temp_min"]
            temp["temp_max"] = respond["list"][root]["main"]["temp_max"]
            temp["humidity"] = respond["list"][root]["main"]["humidity"]
            temp["description"] = respond["list"][root]["weather"][0]["description"]
            temp["icon"] = respond["list"][root]["weather"][0]["icon"]
            temp["dt_txt"] = respond["list"][root]["dt_txt"]
            self.forecast.append(temp)

            root += 4

        self.sendWeatherData.emit(self.current, self.forecast)