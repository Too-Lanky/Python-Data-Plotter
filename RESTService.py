import requests
import yaml
from yaml import Loader
import json
from datetime import datetime

class cryptoRestAPI:    

    def __init__(self):
        #yaml properties
        configFile = open('config.yaml', 'r')
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

    def getHourlySocials(self, count, id):
        socialUrl = self.baseUrl + self.endPoints["hourlySocials"] + "?limit="+count + "&coinId="+id
        socialMediaPosts = {}

        try:
            req = requests.get(socialUrl,headers=self.headers)
            resp = json.loads(req.text)            
            for hour in resp["Data"]:
                dt = datetime.fromtimestamp(hour["time"])
                t = dt.strftime('%b %d %Y %H:%M')
                socialMediaPosts[t] =  hour["reddit_comments_per_hour"]
            return socialMediaPosts    
        except:
            pass