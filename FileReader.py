import datetime
from BackupHandler import checkBackupFolder
from AppSettingsHandler import getSettingsDirectory


def isInteger(potentialInteger):
	try:
		int(potentialInteger)
		return True
	except ValueError:
		return False


class FileReader:

	def __init__(self):
		self.filename = None
		self.filepath = None

	def readFromFile(self):
		pass

	def writeToFile(self, newData):
		pass

	def backupFile(self, newData):
		currentFilepath = self.filepath
		currentFilename = self.filename
		appSettingsDirectory = getSettingsDirectory()

		checkBackupFolder(appSettingsDirectory)

		self.filepath = appSettingsDirectory + '/Backup/'
		self.filename = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + self.filename.strip('/')
		self.writeToFile(newData)

		self.filepath = currentFilepath
		self.filename = currentFilename


