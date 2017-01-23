import requests

class HKO(object):

    def __init__(self):
        self.url = 'http://rss.weather.gov.hk/rss/CurrentWeather.xml'
        self.request = requests.get(url=self.url)
        self.xml = self.request.text
        if "pic50.png" in self.xml:
            self.weather = "clear"
        elif "pic51.png" in self.xml:
            self.weather = "mostly clear"
        elif "pic52.png" in self.xml:
            self.weather = "partly clear"
        elif "pic53.png" in self.xml:
            self.weather = "chance of shower"
        elif "pic54.png" in self.xml:
            self.weather = "scattered shower"
        elif "pic60.png" in self.xml:
            self.weather = "cloudy"
        elif "pic61.png" in self.xml:
            self.weather = "very cloudy"
        elif "pic62.png" in self.xml:
            self.weather = "light rain"
        elif "pic63.png" in self.xml:
            self.weather = "heavy rain"
        elif "pic64.png" in self.xml:
            self.weather = "heavy rain"
        elif "pic65.png" in self.xml:
            self.weather = "thunderstorm"


        elif "pic7" in self.xml:
            self.weather = "evening"
        else:
            self.weather = "unknown"

