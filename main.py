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
            showFiles.changeDir(root)
            print('{red}--> {green}{path}'.format(path = os.getcwd(), green = Fore.GREEN, red = Fore.RED))
            print('copy file >> {color}{file}'.format(file = __files__, color = Fore.GREEN))
            shutil.move(__files__, os.path.join(target))
            print('file {color}{file} is done!'.format(file = __files__, color = Fore.RED))

    for __dir__ in subdirs:
        if showFiles.ifFolderExists(target, __dir__) !=True:
            showFiles.changeDir(root)
            print('{red}--> {green}{path}'.format(path = os.getcwd(), green = Fore.GREEN, red = Fore.RED))
            print('copy folder >> {color}{folder}'.format(folder = __dir__, color = Fore.GREEN))
            shutil.move(__dir__, os.path.join(target))
            print('folder {color}{folder} is done!'.format(folder = __dir__, color = Fore.RED))


if __name__ == '__main__':
    copy()
