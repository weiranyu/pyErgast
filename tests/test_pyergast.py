from pyergast import __version__
from pyergast import pyergast
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_get_drivers():
    expected = 850
    actual = pyergast.get_drivers()['driverId'].count()
    assert expected == actual, 'Should be true (850 drivers in total)'

def test_get_constructors():
    expected = 211
    actual = pyergast.get_constructors()['constructorId'].count()
    assert expected == actual, 'Should be true (11 constructors in total)'

def test_get_circuits():
    expected = 77
    actual = pyergast.get_circuits()['circuitId'].count()
    assert expected == actual, 'Should be true (76 circuits in total)'

def test_find_driverid():
    expected = 1
    actual = pyergast.find_driverid('Kimi', 'Raikkonen').shape[0]
    assert expected == actual, 'There should 1 be result'

def test_find_constructorid():
    expected = 1
    actual = pyergast.find_constructorid('HAAS').shape[0]
    assert expected == actual, 'There should 1 be result'

def test_find_circuitid():
    expected = (4, 7)
    actual = pyergast.find_circuitid('Portugal').shape
    assert expected == actual, 'Should have 4 rows and 7 columns'

def test_get_race_result():
    expected = '44'
    actual = pyergast.get_race_result(2014, 4)['number'][0]
    assert expected == actual, 'Number 44 should have won'

def test_get_qualifying_result():
    expected = '44'
    actual = pyergast.get_qualifying_result(2014, 4)['number'][0]
    assert expected == actual, 'Number 44 should have qualified first'

def test_qualifying_assert():
    with pytest.raises(AssertionError):
        pyergast.get_qualifying_result(1950, 1)

def test_get_schedule():
    expected = 17
    actual = pyergast.get_schedule().shape[0]
    assert expected == actual, 'There were 17 races in 2020'

def test_driver_standings():
    expected = 81
    actual = pyergast.driver_standings(1950).shape[0]
    assert expected == actual, 'There were 81 drivers in 1950'

def test_constructor_standings():
    expected = 17
    actual = pyergast.constructor_standings(1985).shape[0]
    assert expected == actual, 'There were 17 constructors in 1950'

def test_query_driver():
    expected = (1, 10)
    actual = pyergast.query_driver('aitken').shape
    assert expected == actual, 'Should be (1, 10)'

def test_query_constructor():
    expected = (63, 9)
    actual = pyergast.query_constructor('ferrari').shape
    assert expected == actual, 'Should be (63, 9)'

