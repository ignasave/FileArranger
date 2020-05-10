import time
from io import open 
#from watchdog.observers import Observer
#from watchdog.events import PatternMatchingEventHandler
import os 
import glob

actualDir = os.getcwd()
data = {}
excluded_files = ['BIN', 'sys']
files_list = glob.glob('*')

def getData():
    archive = open(actualDir + '/config.txt')
    for line in archive.readlines():
        data.update({line.split('  ')[0] : line.split('  ')[1].replace('\n', '')})


def createDirs():
    for dir in data:
        try:
            os.makedirs(data[dir])
        except FileExistsError:
            continue


def arrange():
    for file in files_list:
        fextension = file.split(sep='.')
        if fextension not in excluded_files:
            for dir in data:           
                    try:
                        if (fextension[1] == dir and fextension[0] != 'Organizador' and fextension[0] != 'config'):  
                            os.rename(file, data[dir] + '/' + file)
                    except (OSError, IndexError):
                        continue


getData()
createDirs()
arrange()


