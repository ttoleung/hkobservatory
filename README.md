[![Build Status](https://travis-ci.org/ttoleung/HKO-python.svg?branch=master)](https://travis-ci.org/ttoleung/HKO-python)

# HKO-python
Return a weather object based on weather reported by HK Observatory

# Quick Start Guide

~~~python
import hkop

hko = hkop.HKOP()
print ("The weather today is %s" % hko.weather)
~~~

produce the following result:

~~~
The weather today is light shower
~~~
