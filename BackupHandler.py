import os


def checkIfFilesExist(filepath):
	if os.path.exists(filepath):
		return True
	else:
		return False


def checkBackupFolder(workingDirectory):
	backupFolder = workingDirectory + '/Backup'
	if os.path.exists(backupFolder) == False:
		createBackupFolder(backupFolder)


def createBackupFolder(backupFolderLocation):
	try:
		os.mkdir(backupFolderLocation)
	except (OSError):
		print('An error occured while attempting to create the backup folder, try checking permissions and try again')
	except:
		print('An unknown error occured')