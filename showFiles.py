import ini, os

def changeDir(dirname):
    os.chdir(dirname)


def showDir(dirname):
    return os.listdir(dirname)


def isFull(dirname):
    return len(os.listdir(dirname))

def isEmpty(dirname):
    if isFull(dirname) == 0:
        return True


def ifFolderExists(dirname):
    if os.path.exists(dirname):
        return True
