from art import art


def commandsHelp():
    art.tprint("Help", font="small")
    print('\n\t\tcreate [name] - creates a new folder on current path')
    print('\n\t\trename [folder] [newFolder] - renames [folder] (if it exists) with [newFolder]')
    print('\n\t\tchange [folder/path] - changes to a [folder] or a specfied [path]')
    print('\n\t\tback - moves back a folder')
    print('\n\t\tlist - lists all the folders')
    print('\n\t\tremove/delete [folder] - deletes an existing folder/file')
    print('\n\t\thash [folder/file] - hashes a folder/file\'s name')
    print('\n\t\texit - exits the terminal')
