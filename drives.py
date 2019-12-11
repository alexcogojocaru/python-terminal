import win32api


def getDrives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    drivesList = list()

    for x in drives:
        drivesList.append(x[:-1] + '\\')
    
    return drivesList
