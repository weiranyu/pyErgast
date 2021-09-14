import requests
import pandas as pd


def get_drivers(year=None, race=None):
    """
    Queries the API to obtain the list of drivers in a pandas dataframe format.
    By default, this function returns the list of all drivers who have ever driven in F1.
    If the year parameter is specified, this function returns the list of all drivers who drove in F1 in that year.
    If the year and race parameters are specified, this function returns the list of all drivers who drove in F1 for a particular race.

    Parameters
    ----------
    year: int
        An optional parameter that specifies the year to be queried.
    race: int
        An optional parameter that specifies the round of a year to be queried.

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        driverId: str
        permanentNumber: int
        code: str
        url: str
        givenName: str
        familyName: str
        dateOfBirth: str
        nationality: str

    Example
    -------
    >>> pyergast.get_drivers(2016)
               driverId permanentNumber code  ...  familyName dateOfBirth nationality
    0            alonso              14  ALO  ...      Alonso  1981-07-29     Spanish
    1            bottas              77  BOT  ...      Bottas  1989-08-28     Finnish
    2            button              22  BUT  ...      Button  1980-01-19     British
    3          ericsson               9  ERI  ...    Ericsson  1990-09-02     Swedish
    4          grosjean               8  GRO  ...    Grosjean  1986-04-17      French
    5         gutierrez              21  GUT  ...   Gutiérrez  1991-08-05     Mexican
    6          hamilton              44  HAM  ...    Hamilton  1985-01-07     British
    7          haryanto              88  HAR  ...    Haryanto  1993-01-22  Indonesian
    8        hulkenberg              27  HUL  ...  Hülkenberg  1987-08-19      German
    9             kvyat              26  KVY  ...       Kvyat  1994-04-26     Russian
    10  kevin_magnussen              20  MAG  ...   Magnussen  1992-10-05      Danish
    11            massa              19  MAS  ...       Massa  1981-04-25   Brazilian
    12             nasr              12  NAS  ...        Nasr  1992-08-21   Brazilian
    13             ocon              31  OCO  ...        Ocon  1996-09-17      French
    14    jolyon_palmer              30  PAL  ...      Palmer  1991-01-20     British
    15            perez              11  PER  ...       Pérez  1990-01-26     Mexican
    16        raikkonen               7  RAI  ...   Räikkönen  1979-10-17     Finnish
    17        ricciardo               3  RIC  ...   Ricciardo  1989-07-01  Australian
    18          rosberg               6  ROS  ...     Rosberg  1985-06-27      German
    19            sainz              55  SAI  ...       Sainz  1994-09-01     Spanish
    20        vandoorne               2  VAN  ...   Vandoorne  1992-03-26     Belgian
    21   max_verstappen              33  VER  ...  Verstappen  1997-09-30       Dutch
    22           vettel               5  VET  ...      Vettel  1987-07-03      German
    23         wehrlein              94  WEH  ...    Wehrlein  1994-10-18      German

    [24 rows x 8 columns]
    """
    if year and race:
        url = 'http://ergast.com/api/f1/{}/drivers.json?limit=1000'.format(year, race)
    elif year:
        url = 'http://ergast.com/api/f1/{}/drivers.json?limit=1000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/drivers.json?limit=1000'
    r = requests.get(url)

    assert r.status_code == 200, 'Cannot connect to Ergast API'
    drivers = r.json()
    result = pd.DataFrame(drivers["MRData"]["DriverTable"]['Drivers'])

    return result


def get_constructors(year=None, race=None):
    """
    Queries the API to obtain the list of constructors in a pandas dataframe format.
    By default, this function returns the list of all constructors who have ever driven in F1.
    If the year parameter is specified, this function returns the list of all constructors who participated F1 in that year.
    If the year and race parameters are specified, this function returns the list of all constructors for a particular race.

    Parameters
    ----------
    year: int
        An optional parameter that specifies the year to be queried.
    race: int
        An optional parameter that specifies the round of a year to be queried.

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        constructorId: str
        url: str
        name: str
        nationality: str

    Example
    -------
    >>> pyergast.get_constructors(year=2003, race=10)
      constructorId                                                url      name nationality
    0           bar  http://en.wikipedia.org/wiki/British_American_...       BAR     British
    1       ferrari      http://en.wikipedia.org/wiki/Scuderia_Ferrari   Ferrari     Italian
    2        jaguar         http://en.wikipedia.org/wiki/Jaguar_Racing    Jaguar     British
    3        jordan     http://en.wikipedia.org/wiki/Jordan_Grand_Prix    Jordan       Irish
    4       mclaren               http://en.wikipedia.org/wiki/McLaren   McLaren     British
    5       minardi               http://en.wikipedia.org/wiki/Minardi   Minardi     Italian
    6       renault  http://en.wikipedia.org/wiki/Renault_in_Formul...   Renault      French
    7        sauber                http://en.wikipedia.org/wiki/Sauber    Sauber       Swiss
    8        toyota         http://en.wikipedia.org/wiki/Toyota_Racing    Toyota    Japanese
    9      williams  http://en.wikipedia.org/wiki/Williams_Grand_Pr...  Williams     British
    """
    if year and race:
        url = 'http://ergast.com/api/f1/{}/constructors.json?limit=1000'.format(year, race)
    elif year:
        url = 'http://ergast.com/api/f1/{}/constructors.json?limit=1000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/constructors.json?limit=1000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    constructors = r.json()
    result = pd.DataFrame(constructors["MRData"]["ConstructorTable"]['Constructors'])

    return result


def get_circuits(year=None, race=None):
    """
    Queries the API to obtain the list of circuits in a pandas dataframe format.
    By default, this function returns the list of all circuits ever used in F1.
    If the year parameter is specified, this function returns the list of all circuits used in F1 in that year.
    If the year and race parameters are specified, this function returns the information of the circuit that hosted the specified race in specified year.

    Parameters
    ----------
    year: int
        An optional parameter that specifies the year to be queried.
    race: int
        An optional parameter that specifies the round of a year to be queried.

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        circuitId: str
        url: str
        circuitName: str
        Latitude: int
        Longtitude: int
        Locality: str
        Country: str

    Example
    -------
    >>> pyergast.get_circuits(year=1985, race=3)
             circuitId                                                url  ...        Locality       Country
    0         adelaide  http://en.wikipedia.org/wiki/Adelaide_Street_C...  ...        Adelaide     Australia
    1     brands_hatch          http://en.wikipedia.org/wiki/Brands_Hatch  ...            Kent            UK
    2          detroit  http://en.wikipedia.org/wiki/Detroit_street_ci...  ...         Detroit           USA
    3          estoril  http://en.wikipedia.org/wiki/Aut%C3%B3dromo_do...  ...         Estoril      Portugal
    4            imola  http://en.wikipedia.org/wiki/Autodromo_Enzo_e_...  ...           Imola         Italy
    5      jacarepagua  http://en.wikipedia.org/wiki/Aut%C3%B3dromo_In...  ...  Rio de Janeiro        Brazil
    6          kyalami               http://en.wikipedia.org/wiki/Kyalami  ...         Midrand  South Africa
    7           monaco     http://en.wikipedia.org/wiki/Circuit_de_Monaco  ...     Monte-Carlo        Monaco
    8            monza  http://en.wikipedia.org/wiki/Autodromo_Naziona...  ...           Monza         Italy
    9      nurburgring      http://en.wikipedia.org/wiki/N%C3%BCrburgring  ...         Nürburg       Germany
    10  osterreichring               http://en.wikipedia.org/wiki/A1-Ring  ...       Spielburg       Austria
    11          ricard   http://en.wikipedia.org/wiki/Paul_Ricard_Circuit  ...    Le Castellet        France
    12     silverstone   http://en.wikipedia.org/wiki/Silverstone_Circuit  ...     Silverstone            UK
    13             spa  http://en.wikipedia.org/wiki/Circuit_de_Spa-Fr...  ...             Spa       Belgium
    14      villeneuve  http://en.wikipedia.org/wiki/Circuit_Gilles_Vi...  ...        Montreal        Canada
    15       zandvoort     http://en.wikipedia.org/wiki/Circuit_Zandvoort  ...       Zandvoort   Netherlands

    [16 rows x 7 columns]
    """
    if year and race:
        url = 'http://ergast.com/api/f1/{}/circuits.json?limit=1000'.format(year, race)
    elif year:
        url = 'http://ergast.com/api/f1/{}/circuits.json?limit=1000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/circuits.json?limit=1000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    circuits = r.json()
    result = pd.DataFrame(circuits["MRData"]["CircuitTable"]["Circuits"])

    # Grabbing latitude, longtitude, locality and country separately
    geo = result['Location']
    latitude, longtitude, locality, country = ([] for i in range(4))
    for track in geo:
        latitude.append(track['lat'])
        longtitude.append(track['long'])
        locality.append(track['locality'])
        country.append(track['country'])
    result['Latitude'] = latitude
    result['Longtitude'] = longtitude
    result['Locality'] = locality
    result['Country'] = country
    result = result.drop('Location', axis=1)
    return result


def find_driverid(firstname, lastname):
    """
    Searches the list of all drivers to find ones that are the same or similar to the input.

    Parameters
    ----------
    firstname: str
        The first name of the driver
    lastname: str
        The last name of the driver

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        driverId: str
        permanentNumber: int
        code: str
        url: str
        givenName: str
        familyName: str
        dateOfBirth: str
        nationality: str

    Example
    -------
    >>> pyergast.find_driverid('peter', 'collins')
             driverId                                                url givenName  ... nationality permanentNumber code
    167       collins  http://en.wikipedia.org/wiki/Peter_Collins_(ra...     Peter  ...     British             NaN  NaN
    595        peters  http://en.wikipedia.org/wiki/Josef_Peters_(dri...     Josef  ...      German             NaN  NaN
    596      peterson       http://en.wikipedia.org/wiki/Ronnie_Peterson    Ronnie  ...     Swedish             NaN  NaN
    809  peter_walker  http://en.wikipedia.org/wiki/Peter_Walker_(dri...     Peter  ...     British             NaN  NaN

    [4 rows x 8 columns]
    """
    dfDrivers = get_drivers()
    result = dfDrivers[
        dfDrivers['driverId'].str.contains(firstname.lower()) | dfDrivers['driverId'].str.contains(lastname.lower())]
    return result


def find_constructorid(name):
    """
    Searches the list of all constructors to find ones that are the same or similar to the input.

    Parameters
    ----------
    name: str
        The name of the constructor

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        constructorId: str
        url: str
        name: str
        nationality: str

    Example
    -------
    >>> pyergast.find_constructorid('lotus')
          constructorId                                        url                       name nationality
    111    lotus_racing  http://en.wikipedia.org/wiki/Lotus_Racing                      Lotus   Malaysian
    112        lotus_f1      http://en.wikipedia.org/wiki/Lotus_F1                   Lotus F1     British
    113  lotus-borgward    http://en.wikipedia.org/wiki/Team_Lotus             Lotus-Borgward     British
    114       lotus-brm    http://en.wikipedia.org/wiki/Team_Lotus                  Lotus-BRM     British
    115    lotus-climax    http://en.wikipedia.org/wiki/Team_Lotus               Lotus-Climax     British
    116      lotus-ford    http://en.wikipedia.org/wiki/Team_Lotus                 Lotus-Ford     British
    117  lotus-maserati    http://en.wikipedia.org/wiki/Team_Lotus             Lotus-Maserati     British
    118        lotus-pw    http://en.wikipedia.org/wiki/Team_Lotus  Lotus-Pratt &amp; Whitney     British
    191      team_lotus    http://en.wikipedia.org/wiki/Team_Lotus                 Team Lotus     British
    """
    dfConstructors = get_constructors()
    result = dfConstructors[dfConstructors['constructorId'].str.contains(name.lower())]
    return result


def find_circuitid(circuit):
    """
    Searches the list of all the circuits that are similar to the input

    Parameters
    ----------
    circuit: str
        The name of the circuit. Actual circuit name, locality, or country are all accepted.

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        circuitId: str
        url: str
        circuitName: str
        Latitude: int
        Longtitude: int
        Locality: str
        Country: str

    Example
    -------
    >>> pyergast.find_circuitid('brazil')
          circuitId                                                url  ...        Locality Country
    29   interlagos  http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Jo...  ...       São Paulo  Brazil
    31  jacarepagua  http://en.wikipedia.org/wiki/Aut%C3%B3dromo_In...  ...  Rio de Janeiro  Brazil

    [2 rows x 7 columns]
    """
    dfCircuits = get_circuits()
    result = dfCircuits[dfCircuits['circuitId'].str.lower().str.contains(circuit.lower()) |
                        dfCircuits['circuitName'].str.lower().str.contains(circuit.lower()) |
                        dfCircuits['Locality'].str.lower().str.contains(circuit.lower()) |
                        dfCircuits['Country'].str.lower().str.contains(circuit.lower())]
    return result


def get_race_result(year=None, race=None):
    """
    Queries the API to return race results in a pandas dataframe format.
    By default this method returns the most recent result

    Parameters
    ----------
    year: int
        An optional parameter that specifies the year to be queried.
    race: int
        An optional parameter that specifies the round of a year to be queried.

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        number: int
        position: int
        positionText: str
        grid: int
        points: int
        driverID: str
        driver: str
        nationality: str
        constructorID: str
        constructor: str
        laps: int
        status: str
        Time: dict

    Example
    -------
    >>> pyergast.get_race_result()
       number position positionText grid  ...   constructor laps        status                                          Time
    0      33        1            1    1  ...      Red Bull   55      Finished  {'millis': '5788645', 'time': '1:36:28.645'}
    1      77        2            2    2  ...      Mercedes   55      Finished      {'millis': '5804621', 'time': '+15.976'}
    2      44        3            3    3  ...      Mercedes   55      Finished      {'millis': '5807060', 'time': '+18.415'}
    3      23        4            4    5  ...      Red Bull   55      Finished      {'millis': '5808632', 'time': '+19.987'}
    4       4        5            5    4  ...       McLaren   55      Finished    {'millis': '5849374', 'time': '+1:00.729'}
    5      55        6            6    6  ...       McLaren   55      Finished    {'millis': '5854307', 'time': '+1:05.662'}
    6       3        7            7   11  ...       Renault   55      Finished    {'millis': '5862393', 'time': '+1:13.748'}
    7      10        8            8    9  ...    AlphaTauri   55      Finished    {'millis': '5878363', 'time': '+1:29.718'}
    8      31        9            9   10  ...       Renault   55      Finished      {'millis': '5799996', 'time': '+11.351'}
    9      18       10           10    8  ...  Racing Point   55      Finished       {'millis': '5790314', 'time': '+1.669'}
    10     26       11           11    7  ...    AlphaTauri   54        +1 Lap                                           NaN
    11      7       12           12   15  ...    Alfa Romeo   54        +1 Lap                                           NaN
    12     16       13           13   12  ...       Ferrari   54        +1 Lap                                           NaN
    13      5       14           14   13  ...       Ferrari   54        +1 Lap                                           NaN
    14     63       15           15   16  ...      Williams   54        +1 Lap                                           NaN
    15     99       16           16   14  ...    Alfa Romeo   54        +1 Lap                                           NaN
    16      6       17           17   18  ...      Williams   54        +1 Lap                                           NaN
    17     20       18           18   20  ...  Haas F1 Team   54        +1 Lap                                           NaN
    18     51       19           19   17  ...  Haas F1 Team   53       +2 Laps                                           NaN
    19     11       20            R   19  ...  Racing Point    8  Transmission                                           NaN

    [20 rows x 13 columns]
    """
    if year or race:
        assert year and race, 'You must specify both a year and a race'
        url = 'http://ergast.com/api/f1/{}/{}/results.json?limit=1000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/current/last/results.json?limit=1000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    race_result = r.json()
    result_dict = race_result["MRData"]['RaceTable']['Races'][0]['Results']

    # Unpack the lists of dicts in result_dict and reformat the result
    for driver in result_dict:
        drive_dict = unpack_lists(driver)
        driver_info = drive_dict[0]
        constructor_info = drive_dict[1]
        driver['driver'] = driver_info['givenName'] + ' ' + driver_info['familyName']
        driver['driverID'] = driver_info['driverId']
        driver['nationality'] = driver_info['nationality']
        driver['constructor'] = constructor_info['name']
        driver['constructorID'] = constructor_info['constructorId']

    # Select the columns that are relevant to the race result
    cols = ['number', 'position', 'positionText', 'grid', 'points', 'driverID', 'driver',
            'nationality', 'constructorID', 'constructor', 'laps', 'status', 'Time']
    return pd.DataFrame(result_dict)[cols]


def get_qualifying_result(year=None, race=None):
    """
    Queries the API to return qualifying results in a pandas dataframe format.
    By default this method returns the most recent result

    Parameters
    ----------
    year: int
        An optional parameter that specifies the year to be queried.
    race: int
        An optional parameter that specifies the round of a year to be queried.

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        number: int
        position: int
        driverID: str
        driver: str
        nationality: str
        constructorID: str
        constructor: str
        Q1: str
        Q2: str
        Q3: str

    Example
    -------
    >>> pyergast.get_qualifying_result()
       number position           driverID              driver  ...   constructor        Q1        Q2        Q3
    0      33        1     max_verstappen      Max Verstappen  ...      Red Bull  1:35.993  1:35.641  1:35.246
    1      77        2             bottas     Valtteri Bottas  ...      Mercedes  1:35.699  1:35.527  1:35.271
    2      44        3           hamilton      Lewis Hamilton  ...      Mercedes  1:35.528  1:35.466  1:35.332
    3       4        4             norris        Lando Norris  ...       McLaren  1:36.016  1:35.849  1:35.497
    4      23        5              albon     Alexander Albon  ...      Red Bull  1:36.106  1:35.654  1:35.571
    5      55        6              sainz        Carlos Sainz  ...       McLaren  1:36.517  1:36.192  1:35.815
    6      26        7              kvyat        Daniil Kvyat  ...    AlphaTauri  1:36.459  1:36.214  1:35.963
    7      18        8             stroll        Lance Stroll  ...  Racing Point  1:36.502  1:36.143  1:36.046
    8      16        9            leclerc     Charles Leclerc  ...       Ferrari  1:35.881  1:35.932  1:36.065
    9      10       10              gasly        Pierre Gasly  ...    AlphaTauri  1:36.545  1:36.282  1:36.242
    10     31       11               ocon        Esteban Ocon  ...       Renault  1:36.783  1:36.359       NaN
    11      3       12          ricciardo    Daniel Ricciardo  ...       Renault  1:36.704  1:36.406       NaN
    12      5       13             vettel    Sebastian Vettel  ...       Ferrari  1:36.655  1:36.631       NaN
    13     99       14         giovinazzi  Antonio Giovinazzi  ...    Alfa Romeo  1:37.075  1:38.248       NaN
    14     11       15              perez        Sergio Pérez  ...  Racing Point  1:36.034       NaN       NaN
    15      7       16          raikkonen      Kimi Räikkönen  ...    Alfa Romeo  1:37.555       NaN       NaN
    16     20       17    kevin_magnussen     Kevin Magnussen  ...  Haas F1 Team  1:37.863       NaN       NaN
    17     63       18            russell      George Russell  ...      Williams  1:38.045       NaN       NaN
    18     51       19  pietro_fittipaldi   Pietro Fittipaldi  ...  Haas F1 Team  1:38.173       NaN       NaN
    19      6       20             latifi     Nicholas Latifi  ...      Williams  1:38.443       NaN       NaN

    [20 rows x 10 columns]
    """
    if year and race:
        assert year >= 1996, 'Qualifying data only available starting from 1996'
        url = 'http://ergast.com/api/f1/{}/{}/qualifying.json?limit=1000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/current/last/qualifying.json?limit=1000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    race_result = r.json()
    result_dict = race_result["MRData"]['RaceTable']['Races'][0]['QualifyingResults']

    # Unpack the lists of dicts in result_dict and reformat the result
    for driver in result_dict:
        drive_dict = unpack_lists(driver)
        driver_info = drive_dict[0]
        constructor_info = drive_dict[1]
        driver['driver'] = driver_info['givenName'] + ' ' + driver_info['familyName']
        driver['driverID'] = driver_info['driverId']
        driver['nationality'] = driver_info['nationality']
        driver['constructor'] = constructor_info['name']
        driver['constructorID'] = constructor_info['constructorId']

    # Specify the columns to be returned, taking into account changing qualifying formats
    cols = ['number', 'position', 'driverID', 'driver', 'nationality', 'constructorID', 'constructor', 'Q1']
    if 'Q2' in result_dict[0].keys():
        cols.append('Q2')
    if 'Q3' in result_dict[0].keys():
        cols.append('Q3')
    return pd.DataFrame(result_dict)[cols]


def get_schedule(year=None):
    """
    Queries the API to return the schedule of a specified season. Defaults to most recent season.

    Parameters
    ----------
    year: int
        An optional parameter that specifies the year to be queried.

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        season: int
        round: int
        url: str
        raceName: str
        date: str
        circuitId: str
        circuitName: str
        locality: str
        country: str

    Example
    -------
    >>> pyergast.get_schedule(1957)
      season round  ...      locality    country
    0   1957     1  ...  Buenos Aires  Argentina
    1   1957     2  ...   Monte-Carlo     Monaco
    2   1957     3  ...  Indianapolis        USA
    3   1957     4  ...         Rouen     France
    4   1957     5  ...     Liverpool         UK
    5   1957     6  ...       Nürburg    Germany
    6   1957     7  ...       Pescara      Italy
    7   1957     8  ...         Monza      Italy

    [8 rows x 9 columns]
    """
    if year:
        url = 'http://ergast.com/api/f1/{}.json?limit=1000'.format(year)
    else:
        url = 'http://ergast.com/api/f1/current.json?limit=1000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    schedule = r.json()['MRData']['RaceTable']['Races']

    # Unpack the lists of dicts in result_dict and reformat the result
    for race in schedule:
        circuit = unpack_lists(race)[0]
        race['circuitID'] = circuit['circuitId']
        race['circuitName'] = circuit['circuitName']
        race['locality'] = circuit['Location']['locality']
        race['country'] = circuit['Location']['country']
        del race['Circuit']

    return pd.DataFrame(schedule)


def driver_standings(year=None, race=None):
    """
    Fetch the driver standings after a specific race in a specific year. Defaults to latest standings

    Parameters
    ----------
    year: int
        An optional parameter that specifies the year to be queried.
    race: int
        An optional parameter that specifies the round of a year to be queried.

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        position: int
        positionText: str
        points: int
        wins: int
        driverID: str
        driver: str
        nationality: str
        constructorID: str
        constructor: str

    Example
    -------
    >>> pyergast.driver_standings(1974)
       position positionText points wins            driverID              driver    nationality constructorID constructor
    0         1            1     55    3  emerson_fittipaldi  Emerson Fittipaldi      Brazilian       mclaren     McLaren
    1         2            2     52    1           regazzoni      Clay Regazzoni          Swiss       ferrari     Ferrari
    2         3            3     45    2           scheckter      Jody Scheckter  South African       tyrrell     Tyrrell
    3         4            4     38    2               lauda          Niki Lauda       Austrian       ferrari     Ferrari
    4         5            5     35    3            peterson     Ronnie Peterson        Swedish    team_lotus  Team Lotus
    ..      ...          ...    ...  ...                 ...                 ...            ...           ...         ...
    57       58           58      0    0              purley        David Purley        British         token       Token
    58       59           59      0    0             facetti       Carlo Facetti        Italian       brabham     Brabham
    59       60           60      0    0            lombardi      Lella Lombardi        Italian       brabham     Brabham
    60       61           61      0    0             perkins       Larry Perkins     Australian          amon        Amon
    61       62           62      0    0           nicholson      John Nicholson  New Zealander        lyncar      Lyncar

    [62 rows x 9 columns]
    """
    if year and race:
        url = 'http://ergast.com/api/f1/{}/{}/driverStandings.json?limit=1000'.format(year, race)
    elif year:
        url = 'http://ergast.com/api/f1/{}/driverStandings.json?limit=1000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/current/driverStandings.json?limit=1000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    driverStandings = r.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

    for driver in driverStandings:
        driver['driverID'] = driver['Driver']['driverId']
        driver['driver'] = driver['Driver']['givenName'] + ' ' + driver['Driver']['familyName']
        driver['nationality'] = driver['Driver']['nationality']
        driver['constructorID'] = driver['Constructors'][0]['constructorId']
        driver['constructor'] = driver['Constructors'][0]['name']
        del driver['Driver']
        del driver['Constructors']

    return pd.DataFrame(driverStandings)


def constructor_standings(year=None, race=None):
    """
    Fetch the constructor standings after a specific race in a specific year. Defaults to latest standings

    Parameters
    ----------
    year: int
        An optional parameter that specifies the year to be queried.
    race: int
        An optional parameter that specifies the round of a year to be queried.

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        position: int
        positionText: str
        points: int
        wins: int
        constructorID: str
        constructor: str
        nationality: str

    Example
    -------
    >>> pyergast.constructor_standings(1965)
       position positionText points wins    constructorID             name    nationality
    0         1            1     54    6     lotus-climax     Lotus-Climax        British
    1         2            2     45    3              brm              BRM        British
    2         3            3     27    0   brabham-climax   Brabham-Climax        British
    3         4            4     26    0          ferrari          Ferrari        Italian
    4         5            5     14    0    cooper-climax    Cooper-Climax        British
    5         6            6     11    1            honda            Honda       Japanese
    6         7            7      5    0      brabham-brm      Brabham-BRM        British
    7         8            8      2    0        lotus-brm        Lotus-BRM        British
    8         9            9      0    0     brabham-ford     Brabham-Ford        British
    9        10           10      0    0             alfa       Alfa Romeo        Italian
    10       11           11      0    0   lds-alfa_romeo   LDS-Alfa Romeo  South African
    11       12           12      0    0      cooper-ford      Cooper-Ford        British
    12       13           13      0    0       lds-climax       LDS-Climax  South African
    13       14           14      0    0       lotus-ford       Lotus-Ford        British
    14       15           15      0    0               re               RE      Rhodesian
    15       16           16      0    0  cooper-maserati  Cooper-Maserati        British
    """
    if year and race:
        assert year >= 1958, 'Constructor standings only available starting 1958'
        url = 'http://ergast.com/api/f1/{}/{}/constructorStandings.json?limit=1000'.format(year, race)
    elif year:
        assert year >= 1958, 'Constructor standings only available starting 1958'
        url = 'http://ergast.com/api/f1/{}/constructorStandings.json?limit=1000'.format(year, race)
    else:
        url = 'http://ergast.com/api/f1/current/constructorStandings.json?limit=1000'

    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    constructorStandings = r.json()['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']

    for constructor in constructorStandings:
        constructor['constructorID'] = constructor['Constructor']['constructorId']
        constructor['name'] = constructor['Constructor']['name']
        constructor['nationality'] = constructor['Constructor']['nationality']
        del constructor['Constructor']

    return pd.DataFrame(constructorStandings)


def query_driver(driverid):
    """
    Fetches the driver's historical driver standings position

    Parameters
    ----------
    driverid: str
        A string representing the driver id of the driver. Use `find_driverid` method to obtain constructorid

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        season: int
        round: int
        position: int
        positionText: str
        points: int
        wins: int
        driver: str
        nationality: str
        constructorID: str
        constructor: str

    Example
    -------
    >>> pyergast.query_driver('raikkonen')
       season round position positionText points wins          driver nationality constructorID constructor
    0    2001    17       10           10      9    0  Kimi Räikkönen     Finnish        sauber      Sauber
    1    2002    17        6            6     24    0  Kimi Räikkönen     Finnish       mclaren     McLaren
    2    2003    16        2            2     91    1  Kimi Räikkönen     Finnish       mclaren     McLaren
    3    2004    18        7            7     45    1  Kimi Räikkönen     Finnish       mclaren     McLaren
    4    2005    19        2            2    112    7  Kimi Räikkönen     Finnish       mclaren     McLaren
    5    2006    18        5            5     65    0  Kimi Räikkönen     Finnish       mclaren     McLaren
    6    2007    17        1            1    110    6  Kimi Räikkönen     Finnish       ferrari     Ferrari
    7    2008    18        3            3     75    2  Kimi Räikkönen     Finnish       ferrari     Ferrari
    8    2009    17        6            6     48    1  Kimi Räikkönen     Finnish       ferrari     Ferrari
    9    2012    20        3            3    207    1  Kimi Räikkönen     Finnish      lotus_f1    Lotus F1
    10   2013    19        5            5    183    1  Kimi Räikkönen     Finnish      lotus_f1    Lotus F1
    11   2014    19       12           12     55    0  Kimi Räikkönen     Finnish       ferrari     Ferrari
    12   2015    19        4            4    150    0  Kimi Räikkönen     Finnish       ferrari     Ferrari
    13   2016    21        6            6    186    0  Kimi Räikkönen     Finnish       ferrari     Ferrari
    14   2017    20        4            4    205    0  Kimi Räikkönen     Finnish       ferrari     Ferrari
    15   2018    21        3            3    251    1  Kimi Räikkönen     Finnish       ferrari     Ferrari
    16   2019    21       12           12     43    0  Kimi Räikkönen     Finnish          alfa  Alfa Romeo
    17   2020    17       16           16      4    0  Kimi Räikkönen     Finnish          alfa  Alfa Romeo
    """
    url = 'http://ergast.com/api/f1/drivers/{}/driverStandings.json?limit=1000'.format(driverid)
    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    seasons = r.json()['MRData']['StandingsTable']['StandingsLists']

    # Extracting data from json
    for season in seasons:
        for key, value in season['DriverStandings'][0].items():
            season[key] = value
        season['driver'] = season['Driver']['givenName'] + ' ' + season['Driver']['familyName']
        season['nationality'] = season['Driver']['nationality']
        season['constructorID'] = season['Constructors'][0]['constructorId']
        season['constructor'] = season['Constructors'][0]['name']
        del season['DriverStandings']
        del season['Driver']
        del season['Constructors']

    return pd.DataFrame(seasons)


def query_constructor(constructorid):
    """
    Fetches the consturctor's historical constructor standings position

    Parameters
    ----------
    constructorid: str
        A string representing the constructor id of the constructor. Use `find_constructorid` function to obtain constructorid

    Returns
    -------
    pandas.DataFrame

    Index:
        RangeIndex

    Columns:
        season: int
        round: int
        position: int
        positionText: str
        points: int
        wins: int
        constructorID: str
        constructor: str
        nationality: str

    Example
    -------
    >>> pyergast.query_constructor('alfa')
       season round position positionText points wins constructorID constructor nationality
    0    1963    10       16           16      0    0          alfa  Alfa Romeo     Italian
    1    1965    10       10           10      0    0          alfa  Alfa Romeo     Italian
    2    1979    15       16           16      0    0          alfa  Alfa Romeo     Italian
    3    1980    14       11           11      4    0          alfa  Alfa Romeo     Italian
    4    1981    15        9            9     10    0          alfa  Alfa Romeo     Italian
    5    1982    16        9            9      7    0          alfa  Alfa Romeo     Italian
    6    1983    15        6            6     18    0          alfa  Alfa Romeo     Italian
    7    1984    16        8            8     11    0          alfa  Alfa Romeo     Italian
    8    1985    16       12           12      0    0          alfa  Alfa Romeo     Italian
    9    2019    21        8            8     57    0          alfa  Alfa Romeo     Italian
    10   2020    17        8            8      8    0          alfa  Alfa Romeo     Italian
    """
    url = 'http://ergast.com/api/f1/constructors/{}/constructorStandings.json?limit=1000'.format(constructorid)
    r = requests.get(url)
    assert r.status_code == 200, 'Cannot connect to Ergast API. Check your inputs.'
    seasons = r.json()['MRData']['StandingsTable']['StandingsLists']

    # Extracting data from json
    for season in seasons:
        for key, value in season['ConstructorStandings'][0].items():
            season[key] = value
        season['constructorID'] = season['Constructor']['constructorId']
        season['constructor'] = season['Constructor']['name']
        season['nationality'] = season['Constructor']['nationality']
        del season['Constructor']
        del season['ConstructorStandings']

    return pd.DataFrame(seasons)


def unpack_lists(driver):
    """
    Helper function that unpacks dictionaries in a dataframe and packs them into a new list of dicts

    Parameters
    ----------
    df_input: dict
        A dictionary of dictionaries

    Returns
    -------
    list

    Examples
    --------
    >>> pyErgast.unpack_lists({'a': {'a1': 1}, 'b': 1})
    [{'a1': 1}]
    """
    result = []
    for key in driver.keys():
        if isinstance(driver[key], dict):
            result.append(driver[key])
    return result