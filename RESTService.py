import requests
import yaml
from yaml import Loader

class cryptoRestAPI:

    def __init__(self, config = 'config.yaml'):
        #yaml properties
        configFile = open(config, 'r')
        props = yaml.load(configFile,Loader=Loader)
        self.api = props.get('api')
        self.headers = self.generateHeaders()
        self.endPoints = self.generateEndPoints()
        self.baseUrl = self.api["baseUrl"]
    
    def generateHeaders(self):
        headers = {}

        for h in self.api["headers"]:
            headers.update(h)
        
        return headers
    
    def generateEndPoints(self):
        endPoints = {}

        for u in self.api["urls"]:
            endPoints.update(u)
        
        return endPoints

    def getHourlyPrice(self, count, symbol):
        hourlyUrl = self.baseUrl + self.endPoints["hourlyPrice"] + "&count="+count + "&symbol="+symbol

        req = requests.get(hourlyUrl,headers=self.headers)
        print(req)
    
    

test = cryptoRestAPI()
test.getHourlyPrice("24","BTC")