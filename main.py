import requests
from bs4 import BeautifulSoup

def getResponse(URL):
    return requests.get(URL)

def getResults(response, game, class_name="kit-") -> list:
    return [values.getText() for values in BeautifulSoup(response.content).find_all('div', {"class":"{}{}".format(class_name, game)})]

def urlMount(game, number=None):
    partial_url = "https://confiraloterias.com.br/{}/?concurso={}"
    if number is None:
        return lambda n: partial_url.format(game, n)
    else:
        return partial_url.format(game, str(number))

class DataGame(object):
    def __init__(self, name, begin, end):
        self.name, self.begin, self.end = name, begin, end

def readLotofacil(begin=1800, end=1900):
    return DataGame('lotofacil', begin, end)

def readMegasena(begin=2220, end=2223):
    return DataGame('megasena', begin, end)

def readGame(data_game):
    game_name = data_game.name
    url     = urlMount(game_name)
    return [getResults(getResponse(url(number)), game_name) for number in range(data_game.begin, data_game.end)] 

print(readGame(readMegasena()))
