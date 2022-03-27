from codecs import getreader
import csv
import yaml
from yaml import Loader

class Plotter:
    
    def __init__(self, config = 'DataPlotter/config.yaml'):
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

    def generateAxes(self):
        rowColumn = {}
        with open(self.props.get('fileName')) as file:
            reader = csv.reader(file)

            for index,line in enumerate(reader):
                if index >= 10:
                    rowColumn[line[0]] = line[3]
            
            return rowColumn

test = Plotter()
print(test.generateMetadata())
print(test.generateAxes())