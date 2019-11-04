import os


def isPath(path):
    if '\\' in path:
        return True
    return False


class Terminal:
    def __init__(self, basePath=None):
        if basePath is None:
            self.__path = "C:\\"
        else:
            self.__path = basePath

    def getPath(self):
        return self.__path

    def setPath(self, path):
        self.__path = path

    def changeFolder(self, folderName):
        try:
            self.__path = os.path.join(self.__path, folderName)
        except FileNotFoundError:
            print('The folder does not exist')

    def listFolders(self):
        files = os.listdir(self.__path)
        for x in files:
            print('\t' + x)

    def printCurrentPath(self):
        print('Current path: ' + self.__path)

    def changePath(self, pathName):
        if isPath(pathName):
            self.__path = os.path.join(self.__path, pathName)
            return

        files = os.listdir(self.__path)
        check = False

        for file in files:
            if file == pathName:
                self.__path = os.path.join(self.__path, pathName)
                check = True
                break

        if check is False:
            print(pathName + ' does not exist')

    def backPath(self):
        if self.__path == "C:\\" or self.__path == "D:\\":
            return

        i = -1
        while self.__path[i] != '\\':
            if abs(i) == len(self.__path):
                break
            else:
                i = i - 1
        self.__path = self.__path[:(i + 1)]
