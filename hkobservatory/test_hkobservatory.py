import pytest
import hkobservatory


def test_url_exist():
    my_weather = hkobservatory.weather()
    assert "Error" not in my_weather.xml


def test_known_condition():
    my_weather = hkobservatory.weather()
    assert my_weather.condition!= "unknown"
