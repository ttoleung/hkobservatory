import requests

class weather(object):

    def __init__(self):
        self.url = 'http://rss.weather.gov.hk/rss/CurrentWeather.xml'
        self.request = requests.get(url=self.url)
        self.xml = self.request.text
        if "pic50.png" in self.xml:
            self.condition = "clear"
        elif "pic51.png" in self.xml:
            self.condition = "mostly clear"
        elif "pic52.png" in self.xml:
            self.condition = "partly clear"
        elif "pic53.png" in self.xml:
            self.condition = "chance of shower"
        elif "pic54.png" in self.xml:
            self.condition = "scattered shower"
        elif "pic60.png" in self.xml:
            self.condition = "cloudy"
        elif "pic61.png" in self.xml:
            self.condition = "very cloudy"
        elif "pic62.png" in self.xml:
            self.condition = "light rain"
        elif "pic63.png" in self.xml:
            self.condition = "heavy rain"
        elif "pic64.png" in self.xml:
            self.condition = "heavy rain"
        elif "pic65.png" in self.xml:
            self.condition = "thunderstorm"
        elif "pic7" in self.xml:
            self.condition = "evening"
        elif "pic8" in self.xml:
            self.condition = "others"
        else:
            self.condition = "unknown"

