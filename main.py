#!/usr/bin/python env

## head method ##

import ini, showFiles, shutil, os
from colorama import Fore, Style, init
init(autoreset=True)

def copy():
    source, target = ini.loadSource(), ini.loadTarget()
    
  
    root, subdirs, files = showFiles.showDir(source)
    
    for __files__ in files:
        if showFiles.isFilesExists(target,__files__) != True:
            print('copy file {color}{file}'.format(file = __files__, color = Fore.GREEN))
            shutil.copy(__files__, target)
            print('file {color}{file} is done!'.format(file = __files__, color = Fore.RED))



if __name__ == '__main__':
    copy()
