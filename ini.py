## load ini file ##

import configparser

parser = configparser.ConfigParser()

parser.read('settings.ini')

def loadSource():
    return parser['SOURCE']['path']

def loadTarget():
    return parser['TARGET']['path']

source, target = loadSource(), loadTarget()
print(source)
print(target)


