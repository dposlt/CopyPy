import ini, os

def changeDir(dirname):
    os.chdir(dirname)


def showDir(dirname):
    for root, subdirs, files in os.walk(dirname):
        return root,subdirs,files


def isFull(dirname):
    return len(os.listdir(dirname))

def isEmpty(dirname):
    if isFull(dirname) == 0:
        return True


def ifFolderExists(dirname):
    if os.path.exists(dirname):
        return True

def isFilesExists(dirname,filename):
    if os.path.exists(dirname + filename):
        return True
