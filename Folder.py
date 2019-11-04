import hashlib
import os


class Folder:
    def __init__(self, path=None):
        if path is None:
            self.__path = "C:/"
        else:
            self.__path = path

    def createFolder(self, folderName):
        try:
            os.mkdir(os.path.join(self.__path, folderName))
        except FileExistsError:
            print(folderName + ' already exists')

    def hashName(self, folderName):
        hashVar = hashlib.sha256()

        if folderName in os.listdir(self.__path):
            hashVar.update(folderName.encode())

            src = os.path.join(self.__path, folderName)
            dst = os.path.join(self.__path, hashVar.hexdigest())
            os.rename(src, dst)

    def setPath(self, parentPath):
        self.__path = parentPath

    def getPath(self):
        return self.__path

    def renameFolder(self, srcFolder, rnmFolder):
        try:
            src = os.path.join(self.__path, srcFolder)
            dst = os.path.join(self.__path, rnmFolder)
            os.rename(src, dst)
        except FileNotFoundError:
            print(srcFolder + ' does not exist')

    def removeFolderFile(self, name):
        if name[0] == '*':
            # fileName, fileExtension = os.path.splitext(os.path.join(self.__path, name))

            for file in os.listdir(self.__path):
                fileName, fileExtension = os.path.splitext(os.path.join(self.__path, file))

                if fileExtension == name[1:]:
                    os.remove(os.path.join(self.__path, file))
            return

        if os.path.isfile(os.path.join(self.__path, name)):
            try:
                os.remove(os.path.join(self.__path, name))
            except FileNotFoundError:
                print(name + ' does not exist')

        else:
            try:
                os.rmdir(os.path.join(self.__path, name))
            except FileNotFoundError:
                print(name + ' does not exist')
