from sys import platform
import os
from pathlib import Path
import tkinter.filedialog
from tkinter import messagebox

# Get working directory path from settings text file, if none exists then create a file and ask for directory path
def getWorkingDirectory(rootWindow):
	# Get base path
	home = str(Path.home())

	appDirectory = getSettingsDirectory()
	settingsFilename = os.path.join(appDirectory, 'settings.txt')

	# Check if the settings file already exists, if not then create one after asking where the user wants to pull their data from
	if os.path.exists(settingsFilename) == False:
		workingDirectory = tkinter.filedialog.askdirectory(parent=rootWindow, initialdir=home,
														   title="Please select the 'cfg7' folder.")

		if workingDirectory == '':
			exit()

		settingsFile = open(settingsFilename, 'w')
		settingsFile.write(workingDirectory)
		settingsFile.close()

	# If the settings file already exists, read the directory and return it
	else:
		settingsFile = open(settingsFilename, 'r')
		workingDirectory = settingsFile.readline()
		settingsFile.close()

	return workingDirectory


def getSettingsDirectory():
	# Get base path
	home = str(Path.home())

	# Detect if system is macOS or Windows
	if platform == "darwin":
		appDirectory = home + "/Library/Application Support/"
	else:
		appDirectory = home + "\AppData\Local\\"

	appDirectory = appDirectory + "DarkCloud2Editor"

	# Check if the app folder already exists, if not then create one
	if os.path.exists(appDirectory) == False:
		try:
			os.makedirs(appDirectory)
		except OSError as error:
			print(error)

	return appDirectory


def deleteSettingsFile():
	home = str(Path.home())

	# Detect if system is macOS or Windows
	if platform == "darwin":
		settingsFile = home + "/Library/Application Support/DarkCloud2Editor/settings.txt"
	else:

		settingsFile = home + "\AppData\Local\DarkCloud2Editor\settings.txt"

	if os.path.exists(settingsFile):
		os.remove(settingsFile)
	else:
		print("Error, File Not Found")
		print(settingsFile)
