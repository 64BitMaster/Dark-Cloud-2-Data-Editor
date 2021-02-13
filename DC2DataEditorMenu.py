import tkinter
import DC2ItemGUI
import DC2WeaponGUI
import DC2RidepodGUI
from AppSettingsHandler import getWorkingDirectory, deleteSettingsFile
from DataHelperFunctions import setTextField
from sys import platform
import os
from pathlib import Path
from BackupHandler import checkBackupFolder
import subprocess


class MenuDisplay:
	def __init__(self, master):
		self.master = master
		master.title('Dark Cloud 2 Data Modifier')
		Height = 350
		Width = 600

		self.canvas = tkinter.Canvas(master, height=Height, width=Width)
		self.canvas.pack()

		self.frame = tkinter.Frame(master)
		self.frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

		self.itemDataButton = tkinter.Button(self.frame, text = 'Edit Item Properties', command = self.openItemDataEditor)
		self.itemDataButton.place(relx = 0.1, rely = 0.2, relwidth = 0.3, relheight = 0.1)

		self.weaponDataButton = tkinter.Button(self.frame, text = 'Edit Weapon Stats', command = self.openWeaponDataEditor)
		self.weaponDataButton.place(relx = 0.6, rely = 0.2, relwidth = 0.3, relheight = 0.1)

		self.ridepodDataButton = tkinter.Button(self.frame, text='Edit Ridepod Stats', command = self.openRidepodDataEditor)
		self.ridepodDataButton.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.1)

		self.deleteSettings = tkinter.Button(self.frame, text='Delete Saved Path', command=self.deleteSettingsAndRefresh)
		self.deleteSettings.place(relx=0.6, rely=0.5, relwidth=0.3, relheight=0.1)

		self.currentLocationLabel = tkinter.Label(self.frame, text = 'Current Location:')
		self.currentLocationLabel.place(relx = 0.05, rely = 0.7, relwidth = 0.3, relheight = 0.1)

		self.currentLocationTextField = tkinter.Entry(self.frame, state ='readonly')
		self.currentLocationTextField.place(relx = 0.33, rely = 0.7, relwidth = 0.6, relheight = 0.1)

		self.openBackupFolderButton = tkinter.Button(self.frame, text = 'Open Backup Folder', command = self.openBackupFolder)
		self.openBackupFolderButton.place(relx = 0.34, rely = 0.85, relwidth = 0.3, relheight = 0.1)

		setTextField(self.currentLocationTextField, getWorkingDirectory(master))


	def openItemDataEditor(self):
		DC2ItemGUI.DarkCloud2ItemDataDisplay()

	def openWeaponDataEditor(self):
		DC2WeaponGUI.DarkCloud2WeaponDisplay()

	def openRidepodDataEditor(self):
		DC2RidepodGUI.DarkCloud2RidepodDisplay()

	def deleteSettingsAndRefresh(self):
		deleteSettingsFile()
		setTextField(self.currentLocationTextField, getWorkingDirectory(self.master))

	def openBackupFolder(self):
		home = str(Path.home())

		# macOS
		if platform == "darwin":
			appDataLocation = home + "/Library/Application Support/DarkCloud2Editor"
			checkBackupFolder(appDataLocation)
			appDataLocation = appDataLocation + '/Backup'
			appDataLocation = os.path.normpath(appDataLocation)
			subprocess.Popen(["open", appDataLocation])

		# Windows
		else:
			appDataLocation = home + "\AppData\Local\DarkCloud2Editor"
			checkBackupFolder(appDataLocation)
			appDataLocation = appDataLocation + '\Backup'
			appDataLocation = os.path.normpath(appDataLocation)
			#subprocess.run([os.path.join(os.getenv('WINDIR'), 'explorer.exe'), appDataLocation])
			os.startfile(appDataLocation)



