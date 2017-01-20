import pytest
import hkop

def test_url_exist():
    hko = hkop.HKOP()
    assert "Error" not in hko.xml


def test_known_weather():
    hko = hkop.HKOP()
    assert hko.weather != "unknonw"
