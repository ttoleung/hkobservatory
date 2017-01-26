[![Build Status](https://travis-ci.org/ttoleung/HKO-python.svg?branch=master)](https://travis-ci.org/ttoleung/HKO-python)

# hkobservatory
Return a weather object based on weather reported by HK Observatory

# Installation
We recommend installation using pip
~~~
pip install hkobservatory
~~~

# Quick Start Guide
~~~python
import hkobservatory

my_weather = hkobservatory.weather()
print ("The weather today is %s" % my_weather.condition())
~~~

produce the following result:

~~~
The weather today is light shower
~~~
