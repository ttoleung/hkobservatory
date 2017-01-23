import pytest
import hkop


def test_url_exist():
    hko = hkop.HKO()
    assert "Error" not in hko.xml


def test_known_weather():
    hko = hkop.HKO()
    assert hko.weather != "unknown"
