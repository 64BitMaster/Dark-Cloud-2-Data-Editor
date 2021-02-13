from ItemDataReader import ItemDataFileHandler, saveItemEdit, ItemData, findItem, checkItemDataTypes
from ItemNameDataReader import ItemNameFileHandler, findItemName, saveItemName
from BackupHandler import checkIfFilesExist, checkBackupFolder
from AppSettingsHandler import getWorkingDirectory, getSettingsDirectory
from DataDisplay import DataDisplay
from DataHelperFunctions import setTextField
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from pathlib import Path
import tkinter.ttk


home = str(Path.home())


class DarkCloud2ItemDataDisplay(DataDisplay):
	def __init__(self):
		newWindow = tkinter.Toplevel()
		newWindow.title('Dark Cloud 2 Item Modifier')

		Height = 500
		Width = 500

		self.canvas = tkinter.Canvas(newWindow, height=Height, width=Width)
		self.canvas.pack()

		self.frame = tkinter.Frame(newWindow)
		self.frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

		self.itemScrollbar = tkinter.Scrollbar(self.frame)
		self.itemScrollbar.place(relx=0.47, rely=0.05, relheight=0.20)

		self.itemListbox = tkinter.Listbox(self.frame, bg='white', yscrollcommand=self.itemScrollbar.set)

		self.itemListbox.place(relx=0.07, rely=0.05, relwidth=0.40, relheight=0.20)

		self.saveButton = tkinter.Button(self.frame, text="Save Changes", command=self.saveData)
		self.saveButton.place(relx=0.61, rely=0.07, relwidth=0.3, relheight=0.05)

		self.discardButton = tkinter.Button(self.frame, text="Discard Changes", command=self.discardChanges)
		self.discardButton.place(relx=0.61, rely=0.16, relwidth=0.3, relheight=0.05)

		self.itemIDLabel = tkinter.Label(self.frame, text='ID:')
		self.itemIDLabel.place(relx=0.10, rely=0.30)
		self.itemIDTextField = tkinter.Entry(self.frame, state='readonly')
		self.itemIDTextField.place(relx=0.17, rely=0.30, relwidth=0.10, relheight=0.055)

		self.nameLabel = tkinter.Label(self.frame, text='Name:')
		self.nameLabel.place(relx=0.45, rely=0.30)
		self.nameTextField = tkinter.Entry(self.frame)
		self.nameTextField.place(relx=0.57, rely=0.30, relwidth=0.38, relheight=0.055)

		self.typeLabel = tkinter.Label(self.frame, text='Type:')
		self.typeLabel.place(relx=0.06, rely=0.40)
		self.typeTextField = tkinter.Entry(self.frame)
		self.typeTextField.place(relx=0.17, rely=0.40, relwidth=0.10, relheight=0.055)

		self.data3Label = tkinter.Label(self.frame, text=' ? ')
		self.data3Label.place(relx=0.505, rely=0.40)
		self.data3TextField = tkinter.Entry(self.frame)
		self.data3TextField.place(relx=0.57, rely=0.40, relwidth=0.10, relheight=0.055)

		self.hotbar = tkinter.IntVar()
		self.hotbarLabel = tkinter.Label(self.frame, text='Can be placed in the hotbar?: ')
		self.hotbarLabel.place(relx=0.055, rely=0.50)
		self.yesRadioButton = tkinter.Radiobutton(self.frame, text='Yes', variable=self.hotbar, value=1)
		self.yesRadioButton.place(relx=0.57, rely=0.50)
		self.noRadioButton = tkinter.Radiobutton(self.frame, text='No', variable=self.hotbar, value=0)
		self.noRadioButton.place(relx=0.75, rely=0.50)

		self.data7Label = tkinter.Label(self.frame, text=' ? ')
		self.data7Label.place(relx=0.101, rely=0.60)
		self.data7TextField = tkinter.Entry(self.frame)
		self.data7TextField.place(relx=0.17, rely=0.60, relwidth=0.10, relheight=0.055)

		self.spriteIDLabel = tkinter.Label(self.frame, text='SpriteID:')
		self.spriteIDLabel.place(relx=0.42, rely=0.60)
		self.spriteIDTextField = tkinter.Entry(self.frame)
		self.spriteIDTextField.place(relx=0.57, rely=0.60, relwidth=0.10, relheight=0.055)

		self.stackSizeLabel = tkinter.Label(self.frame, text='Stack:')
		self.stackSizeLabel.place(relx=0.058, rely=0.70)
		self.stackSizeTextField = tkinter.Entry(self.frame)
		self.stackSizeTextField.place(relx=0.17, rely=0.70, relwidth=0.10, relheight=0.055)

		self.totalItemsLabel = tkinter.Label(self.frame, text='Total:')
		self.totalItemsLabel.place(relx=0.466, rely=0.70)
		self.totalItemsTextField = tkinter.Entry(self.frame)
		self.totalItemsTextField.place(relx=0.57, rely=0.70, relwidth=0.10, relheight=0.055)

		self.modelLabel = tkinter.Label(self.frame, text='Model:')
		self.modelLabel.place(relx=0.058, rely=0.80)
		self.modelTextField = tkinter.Entry(self.frame)
		self.modelTextField.place(relx=0.17, rely=0.80, relwidth=0.25, relheight=0.055)

		self.data11Label = tkinter.Label(self.frame, text=' ? ')
		self.data11Label.place(relx=0.505, rely=0.80)
		self.data11TextField = tkinter.Entry(self.frame)
		self.data11TextField.place(relx=0.57, rely=0.80, relwidth=0.10, relheight=0.055)

		self.workingDirectory = getWorkingDirectory(newWindow)

		self.ItemDataFile = ItemDataFileHandler(self.workingDirectory)
		self.ItemNameFile = ItemNameFileHandler(self.workingDirectory)

		self.AllItemData = self.ItemDataFile.readFromFile()
		self.AllItemNames = self.ItemNameFile.readFromFile()

		self.populateListbox(self.AllItemData)

		self.appSettingsDirectory = getSettingsDirectory()
		checkBackupFolder(self.appSettingsDirectory)


		self.ItemDataFile.backupFile(self.AllItemData)
		self.ItemNameFile.backupFile(self.AllItemNames)


		self.itemListbox.bind('<<ListboxSelect>>', lambda listbox: self.setAllFields(listbox=True))

		self.itemScrollbar.config(command=self.itemListbox.yview)

	def getCurrentDataSelected(self):
		if str(self.itemListbox.curselection()) != '()':
			itemSelected = self.itemListbox.curselection()[0]
			currentItemData = self.AllItemData[itemSelected]
			return currentItemData

	def populateListbox(self, allItems):
		for x in range(len(allItems)):
			self.itemListbox.insert(x, "  " + str(allItems[x].itemID) + ": " + str(
				findItemName(allItems[x].itemID, self.AllItemNames)))

	def setAllFields(self, listbox):

		if (listbox == True):
			currentItemData = self.getCurrentDataSelected()
			if currentItemData is None:
				# Sometimes listbox says you've clicked it when you definitely haven't
				return
		else:
			currentItemData = self.getLastItemData()

		setTextField(self.itemIDTextField, currentItemData.itemID)
		setTextField(self.nameTextField, findItemName(currentItemData.itemID, self.AllItemNames))
		setTextField(self.typeTextField, currentItemData.itemType)
		setTextField(self.data3TextField, currentItemData.data3)

		if currentItemData.data4 == 0:
			self.noRadioButton.invoke()
		else:
			self.yesRadioButton.invoke()

		setTextField(self.data7TextField, currentItemData.data7)
		setTextField(self.spriteIDTextField, currentItemData.spriteIndex)
		setTextField(self.stackSizeTextField, currentItemData.maxStackSize)
		setTextField(self.totalItemsTextField, currentItemData.maxItemCount)
		setTextField(self.modelTextField, currentItemData.itemModelName)
		setTextField(self.data11TextField, currentItemData.data11)

	def getDataFromFields(self):
		changedItemData = [self.itemIDTextField.get(), self.typeTextField.get(), self.data3TextField.get(),
						   self.hotbar.get(), self.stackSizeTextField.get(), self.totalItemsTextField.get(),
						   self.data7TextField.get(),
						   self.spriteIDTextField.get(), self.itemIDTextField.get(), self.modelTextField.get(),
						   self.data11TextField.get()]
		return changedItemData

	def saveData(self):
		changedItemData = self.getDataFromFields()

		if checkItemDataTypes(changedItemData) == True:
			changedItem = ItemData(changedItemData)
			self.AllItemData = saveItemEdit(changedItem, self.AllItemData)
			self.AllItemNames = saveItemName(self.nameTextField.get(), self.AllItemNames, changedItem.itemID)

			self.ItemNameFile.writeToFile(self.AllItemNames)
			self.ItemDataFile.writeToFile(self.AllItemData)

			self.itemListbox.delete(0, self.itemListbox.size())
			self.populateListbox(self.AllItemData)
			self.itemListbox.see(changedItem.itemID)

		else:
			self.discardChanges()
			tkinter.messagebox.showinfo("Error saving data",
										"All fields besides the item and model names must be in an integer format")

	def getLastItemData(self):
		currentItem = int(self.itemIDTextField.get())
		currentItemData = findItem(currentItem, self.AllItemData)
		return currentItemData

