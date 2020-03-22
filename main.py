#!/usr/bin/python env

## head method ##

import ini, showFiles, shutil
from colorama import Fore, Style, init
init(autoreset=True)

def copy():
    source, target = ini.loadSource(), ini.loadTarget()

    if showFiles.isFull(source):
        if showFiles.isEmpty(target):
            print('start copy folders...')
            ## folder for folder ##
            for f in showFiles.showDir(source):
                print('copy folder {folder}'.format(folder = Style.BRIGHT + Fore.RED + f))
                showFiles.changeDir(source)
                #shutil.copytree(f,target,symlinks=False)
                if showFiles.ifFolderExists(f):
                    print('{folder} is copied'.format(folder = Style.BRIGHT + Fore.Red + f))
        else:
            print('target is not empty')


    else:
        print('source or target is empty')

if __name__ == '__main__':
    copy()
