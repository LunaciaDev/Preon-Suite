import requests #url request lib

class taskWeather:
    
    def __init__(self):
        self.API_KEY = open("SCHOOL\\IntroToCS\\project\\api_key.txt").read()
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
        for i in range(5,45,8):
            # forecast always starts at 18h, interval = 3h,
            # so 9h of next day starts at pos 5
            # plus 8 to the next day at 9h

            temp ={}
            temp["temp"] = respond["list"][i]["main"]["temp"]
            temp["feels_like"] = respond["list"][i]["main"]["feels_like"]
            temp["temp_min"] = respond["list"][i]["main"]["temp_min"]
            temp["temp_max"] = respond["list"][i]["main"]["temp_max"]
            temp["humidity"] = respond["list"][i]["main"]["humidity"]
            temp["description"] = respond["list"][i]["weather"][0]["description"]
            temp["icon"] = respond["list"][i]["weather"][0]["icon"]
            temp["dt_txt"] = respond["list"][i]["dt_txt"]
            self.forecast.append(temp)
    
    def runTask(self):
        self.getData()


task = taskWeather()
task.runTask()
