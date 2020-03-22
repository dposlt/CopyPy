#!/usr/bin/python env

## head method ##

import ini, showFiles, shutil, os
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
                print('create folder {folder} to target'.format(folder = f))
                os.mkdir(target+f)
                newtarget = target+f

                shutil.copytree(f,newtarget)
                if showFiles.ifFolderExists(f):
                    print('{green}{folder}{reset} is copied'.format(folder = f, green = Fore.GREEN, reset = Style.RESET_ALL))
        else:
            print('target is not empty')
            print(showFiles.showDir(target))


    else:
        print('source or target is empty')

if __name__ == '__main__':
    copy()
