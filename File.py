import os
from drives import *


def getFileName(filePath):
    i = -1
    string = ''

    while filePath[i] != '\\':
        string = string + filePath[i]

        if abs(i) == len(filePath):
            break
        else:
            i = i - 1

    return string[::-1]


class File:
    def __init__(self, path=None):
        if path is None:
            self.__path = getDrives()[0]
        else:
            self.__path = path

    def setPath(self, path):
        self.__path = path

    def createFile(self, fileName):
        file = open(os.path.join(self.__path, fileName), "w")

    def removeFile(self, folder):
        try:
            os.remove(os.path.join(self.__path, folder))
        except FileNotFoundError:
            print(folder + ' does not exist')

    def writeToFile(self, fileName):
        path = os.path.join(self.__path, fileName)
        filePath, fileExtension = os.path.splitext(path)

        if fileExtension != '':
            print('Enter text:')
            string = input('')

            path = os.path.join(self.__path, getFileName(filePath) + fileExtension)
            f = open(path, "w")
            f.write(string)

    def show(self, fileName):
        file = open(os.path.join(self.__path, fileName), "r")

        i = 1
        print()

        for x in file:
            print(i, '.\t', x, end='')
            i = i + 1

        print('\n\n')
