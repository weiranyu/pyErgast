# pyErgast 

![](https://github.com/weiranyu/pyergast/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/weiranyu/pyergast/branch/main/graph/badge.svg)](https://codecov.io/gh/weiranyu/pyergast) [![Documentation Status](https://readthedocs.org/projects/pyergast/badge/?version=latest)](https://pyergast.readthedocs.io/en/latest/?badge=latest)

Python pandas wrapper for the [Ergast F1 API](http://ergast.com/mrd/). This package allows easy access to the Ergast API for anyone wishing to conduct analysis on Formula 1 data.

## Installation

```bash
$ pip install pyergast
```

## Dependencies

python = "^3.7"
pandas = "^1.1.5"
requests = "^2.25.0"

## Usage

### Obtaining Lists of Drivers 
```python
# Dataframe of all drivers
pyergast.get_drivers()

# All the drivers who drove in 2020
pyergast.get_drivers(2020)

# All the drivers who drove in race 2 of 1969
pyergast.get_drivers(1969, 2)
```

### Obtaining Lists of Constructors
```python
# All constructors in the 2005 season
pyergast.get_constructors(2005)

# All circuits on the 1976 calendar
pyergast.get_circuits(1976)
```

### Obtaining Race and Qualifying Results
```python
# Last race result
pyergast.get_race_result()

# Qualifying result of the 3rd race of 1996
pyergast.get_qualifying_result(1996, 3)
```

### Obtaining Season Schedules
```python
# 1954 schedule
pyergast.get_schedule(1954)
```

### Drivers and Constructor Standings
```python
# 1978 end-of-year drivers standings
pyergast.driver_standings(1978)

# Constructor standings after the 16th race of 2007
pyergast.constructor_standings(2007, 16)
```

### ID Lookup
```python
# Find the ID for Emerson Fittipaldi
pyergast.find_driverid('Emerson', 'Fittipaldi')

# ID of Honda, note no case sensitivity
pyergast.find_constructorid('HONDA')

# Circuit ID for Catalunya, done 3 ways
pyergast.find_circuitid('Catalunya')
pyergast.find_circuitid('Barcelona')
pyergast.find_circuitid('Spain')
```

### Queries
```python
# Career snapshot of Jean Alesi
pyergast.query_driver('alesi')

# Snapshot of Jordan F1 Team
pyergast.query_constructor('jordan')
```

## Documentation

The official documentation is hosted on Read the Docs: https://pyergast.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/weiranyu/pyergast/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
