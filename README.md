[![Build Status](https://travis-ci.org/ttoleung/hkobservatory.svg?branch=master)](https://travis-ci.org/ttoleung/hkobservatory)

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

w = hkobservatory.weather()
print ("The weather today is %s" % w.condition())
~~~

produce the following result:

~~~
The weather today is light shower
~~~
