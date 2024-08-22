#3f8705496304c853df32c77b2f4bfed9
#import keyboard
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt




class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label = QLabel("",self)
        self.emoji_label = QLabel("",self)
        self.description_label = QLabel("",self)
        self.initiateUI()
    



    def initiateUI(self):
        self.setWindowTitle("Weather")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.get_weather_button.setObjectName("get_weather_button")

        self.setStyleSheet("""
            *{
                           font-family: Quicksand;
                           font-size: 20px;
            }
            QLabel, QPushButton{
            font-family: Quicksand;
            }
            QLabel#city_label{
                           font-size: 20px;
                           font-weight: bold;
                           
            }
            QLineEdit#city_input{
                           font-size: 20px;
            }
            QPushButton#get_weather_button{
                           font-size: 20px;
                           font-weight: bold;
            }
            QLabel#temperature_label{
                           font-size: 20px;
            }
            QPushButton#get_weather_button{
                           font-size:20px;
                           font weight:bold;
            }
            QLabel#temperature_label{
                           font-size:30px;
            }
            QLabel#emoji_label{
                           font-size:50px;
                           font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                           font-size: 20px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

        #keyboard.wait('enter')
        #self.get_weather()
        





    def get_weather(self):
        print("You get the weather") #to check in terminal if its working

        api_key = f"3f8705496304c853df32c77b2f4bfed9"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            
        try:  
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError:
            match response.status_code:
                case 400:
                    self.display_error("Error 400: Bad request")
                    self.description_label.setText("")
                    self.emoji_label.setText("")
                case 401:
                    self.display_error("Error 401: Unauthorized")
                    self.description_label.setText("")
                    self.emoji_label.setText("")
                case 402:
                    self.display_error("Error 402: Payment required")
                    self.description_label.setText("")
                    self.emoji_label.setText("")
                case 403:
                    self.display_error("Error 403: Forbidden")
                    self.description_label.setText("")
                    self.emoji_label.setText("")
                case 404:
                    self.display_error("City not found")
                    self.description_label.setText("")
                    self.emoji_label.setText("")
                case 500:
                    self.display_error("Error 500: Internal server error")
                    self.description_label.setText("")
                    self.emoji_label.setText("")
                case 502:
                    self.display_error("Error 502: Bad gateway")
                    self.description_label.setText("")
                    self.emoji_label.setText("")
                case 503:
                    self.display_error("Error 503: Service unavailable. Please try again later.")
                    self.description_label.setText("")
                    self.emoji_label.setText("")
                case 504:
                    self.display_error("Error 504: Gateway timed out")
                    self.description_label.setText("")
                    self.emoji_label.setText("")
                case _:
                    self.display_error(f"HTTP error occured\n{http_error}")
                    self.description_label.setText("")
                    self.emoji_label.setText("")


        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error\nPlease check your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error\nRequest timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")







    def display_error(self, message):
        self.temperature_label.setText(message)






    def display_weather(self,data):

        temperature_c = data["main"]["temp"]-273.15
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_c:.1f}°C") 
        self.description_label.setText(weather_description)

        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.get_weather_emoji(weather_id))







    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id<= 232:
            return "⛈️"
        elif 300<=weather_id<=321:
            return "🌦️"
        elif 500<=weather_id<=531:
            return "🌧️"
        elif 600<=weather_id<=622:
            return "🌨️"
        elif 701<=weather_id<=781:
            return "💨"
        elif weather_id==800:
            return "🌤️"
        elif 800<=weather_id<=804:
            return "🌥️"
        

if __name__== "__main__":
    app = QApplication(sys.argv)
    weatherapp = WeatherApp()
    weatherapp.show()
    sys.exit(app.exec_())