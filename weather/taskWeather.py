import pyttsx3 # text to speech lib
import speech_recognition as sr 
import requests #url request lib
import datetime as dt 

class taskWeather:
    #CURRENTLY LEAVING PRINT(TEXT) FOR CHECKING, REMOVE B4 FINAL
    
    def __init__(self):
        self.API_KEY = open("SCHOOLIntroToCS\\project\\api_key.txt").read()
        self.CITY = "Binh Duong"
        self.URL = f"https://api.openweathermap.org/data/2.5/weather?q={self.CITY}&appid={self.API_KEY}"

        #initialize text to speech 
        self.txts_instance = pyttsx3.init()
        # setting up volume level between 0 and 1                     
        self.txts_instance.setProperty('volume',1.0) 
        #Default 200 word per minute, to slow down speech rate
        self.txts_instance.setProperty('rate', 130)

        #get weather data
        self.displayText = self.formatText()
        #get user's speech command
        self.command = self.listenCommand()
         
    def __contains__(self, key):
         return key in self.command
    
    def listenCommand(self):
        #listen to user speech command
        
        #initialize sr
        self.sr_instance = sr.Recognizer()
        #to listen for smaller voice (the higher the number the louder the speaker has to be)
        self.sr_instance.energy_threshold = 200
        #auto adjust energy threshold if neccessary
        self.sr_instance.dynamic_energy_threshold = True
        #max pause time between each word in spoken sentence in second
        self.sr_instance.pause_threshold = 0.8
        try:
            #initialize microphone
            with sr.Microphone() as mic:
                #adjust to background noise
                self.sr_instance.adjust_for_ambient_noise(mic)
                print("listening")
                #take input from mic
                audio = self.sr_instance.listen(mic)
                #set google sr to english with Singapore accent
                #works best durring testing, saying 'please' at start of sentence
                #helps it recognize better, prefer short over long sentence

                text = self.sr_instance.recognize_google(audio, language ="en-SG",show_all= False)
                print(text)
                return text.lower()
        except sr.UnknownValueError:
                    # if receive error just restart process
                    print("error occur")
                    self.sr_instance = sr.Recognizer()
                    self.listenCommand()
        except text is None:
                    # if nothing is recorded, restart process
                    print("error occur")
                    self.sr_instance = sr.Recognizer()
                    self.listenCommand()

    def processCommand(self,command,text):
    # if the user command contain the word 'weather'
    # dont contain 'not'
    # show to current weather via speech
    
        if ("weather" in command and "not" not in command):
            self.txts_instance.say(text)
            self.txts_instance.runAndWait()
            self.txts_instance.stop()
    
    def kelvinToCelsius (self,kelvin):
    #convert K to C degree
        return kelvin - 273.15

    def getData(self):
        #get weather data from open weather

        respond = requests.get(self.URL).json()

        #format current datetime to MM/DD/YYYY HH:MM
        dt_string = dt.datetime.now().strftime("%m/%d/%Y %H:%M")
        # read description (eg, cloud, sunny, snow...)
        sky_description = respond['weather'][0]['description']
        #read temp in K then convert to C
        temp_in_C = int(self.kelvinToCelsius(respond['main']['temp']))
        #read humidity in %
        humidity = respond['main']['humidity']
        #read wind speed in m/s
        wind_speed = respond['wind']['speed'] 
        #volumn of rain in the last 1hr in mm
        #if no rain then para 'rain' does not exist
        try:
            rain_last_1 = respond['rain']['1h']
        except:
            rain_last_1 = 0
        
        return dt_string, sky_description, temp_in_C, humidity, wind_speed, rain_last_1
        
    def formatText (self):
        #return a paragraph with all neccessary info

        dtS, skyDes, tempC, hum, windS, rain1 = self.getData()
        text = f"Hello, this is the report from {self.CITY}, it is currently {dtS} and the sky seems to be {skyDes} outside. The average temperature outside is {tempC} degree C and the humidity level is {hum} percent. Wind speed blows at a rate of {windS} meter per second. During the last 1 hour, there were {rain1} milimeters of rain. Have a nice day!"
        print(text)
        return text

    def runTask (self):
         self.processCommand(self.command,self.displayText)

task = taskWeather()
task.runTask()
