import requests

class HKOP(object):

    def __init__(self):
        self.url = 'http://rss.weather.gov.hk/rss/CurrentWeather.xml'
        self.request = requests.get(url=self.url)
        self.xml = self.request.text
        if "pic50.png" in self.xml:
            self.weather = "clear"
        elif "pic51.png" in self.xml:
            self.weather = "mostly clear"
        elif "pic52.png" in self.xml:
            self.weather = "mostly cloudy"
        elif "pic53.png" in self.xml:
            self.weather = "light shower"
        elif "pic54.png" in self.xml:
            self.weather = "heavy rain"
        elif "pic7" in self.xml:
            self.weather = "evening"
        else:
            self.weather = "unknown"

