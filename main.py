import os
from CommandFunctions import *
from Terminal import Terminal
from Folder import Folder
from File import File
from art import art


terminal = Terminal()
folder = Folder()
file = File()

def run():
    while True:
        folder.setPath(terminal.getPath())
        file.setPath(terminal.getPath())

        print(terminal.getPath() + '>', end='')
        string = input('')
        stringList = string.split(' ')

        if stringList[0] == 'change':
            terminal.changePath(stringList[1])

        elif stringList[0] == 'back':
            terminal.backPath()

        elif stringList[0] == 'help':
            commandsHelp('Help')

        elif stringList[0] == 'list':
            terminal.listFolders()

        elif stringList[0] == 'create':
            if len(stringList) < 3:
                print('\tInvalid syntax\n\tcreate [-folder/file] [args]')
                continue

            for name in stringList[2:]:
                if stringList[1] == '-folder':
                    folder.createFolder(name)
                elif stringList[1] == '-file':
                    file.createFile(name)

        elif stringList[0] == 'remove' or stringList[0] == 'delete':
            for name in stringList[1:]:
                folder.removeFolderFile(name)

        elif stringList[0] == 'rename':
            if len(stringList) >= 2:
                folder.renameFolder(stringList[1], stringList[2])
            else:
                print('\tInvalid syntax\n\trename [-folder] [-newName]')

        elif stringList[0] == 'exit':
            break

        elif stringList[0] == 'hash':
            if len(stringList) == 2:
                folder.hashName(stringList[1])
            else:
                print('\tInvalid syntax\n\thash [-folder]')

        elif stringList[0] == 'write':
            if len(stringList) > 2 or len(stringList) == 1:
                print('\tInvalid syntax\n\twrite [-file]')
            else:
                file.writeToFile(stringList[1])

        elif stringList[0] == 'show':
            if len(stringList) == 1:
                print('\tInvalid syntax\n\tshow [-fileName]')
            else:
                file.show(stringList[1])
        
        elif stringList[0] == 'clear':
            os.system('cls')    

        else:
            print('Command unknown')

def main():
    art.tprint("Terminal Python")

    commandsHelp('Commands')

    try:
        run()
    except KeyboardInterrupt:
        print('\nExiting...')

if __name__ == "__main__":
    main()
