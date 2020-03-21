import ini, os

def changeDir(dirname):
    os.chdir(dirname)
    print(os.getcwd())
    print(os.listdir())



path = ini.loadSource()

changeDir(path)

