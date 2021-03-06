from codecs import getreader
import csv
import yaml
from yaml import Loader
import datetime
import matplotlib.pyplot as plt
from RESTService import cryptoRestAPI

class Plotter:
    
    def __init__(self, config = 'config.yaml'):
        #yaml properties
        configFile = open(config, 'r')
        self.props = yaml.load(configFile,Loader=Loader)            

    def generateMetadata(self):
        metadata = []
        with open(self.props.get('fileName')) as file:
            reader = csv.reader(file)

            for index,line in enumerate(reader):
                if index == 10:
                    break
                metadata.append(line[3])
            
            return tuple(metadata)                

    def getYAxis(self):
        y = []

        with open(self.props.get('fileName')) as file:
            reader = csv.reader(file)

            for index,line in enumerate(reader):
                if index >= 10:
                    temp = round(float(line[3]))
                    y.append(temp)
            
            return y

    def getXAxis(self):
        x = []
        counter = 0

        with open(self.props.get('fileName')) as file:
            reader = csv.reader(file)

            for index,line in enumerate(reader):
                if index >= 10:
                    date = datetime.datetime.strptime(line[0], '%Y%m%dT%H%M').strftime('%Y-%m-%d')
                    x.append(date)
                    counter += 1
            
            return x
    
    def generateGraph(self):

        crypto = cryptoRestAPI()
        socials = crypto.getHourlySocials("24","7605")

        plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(socials.keys(),socials.values(), c='blue')

        plt.title("Social Media Activity(Reddit)", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()        
        plt.ylabel('Posts', fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()        

        
plot = Plotter()
plot.generateGraph()