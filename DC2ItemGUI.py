from ItemDataReader import ItemDataFileHandler, ItemNameFileHandler,  \
	findItemName, saveItemEdit, ItemData, saveItemName, findItem, checkBackupFolder, saveFiles
import tkinter
import tkinter.filedialog
from pathlib import Path

home = str(Path.home())


class DarkCloud2ItemDataDisplay:
	def __init__(self, master):
		self.master = master
		master.title('Dark Cloud 2 Item Modifier')

		Height = 500
		Width = 500

		self.canvas = tkinter.Canvas(master, height=Height, width=Width)
		self.canvas.pack()

		self.frame = tkinter.Frame(master)
		self.frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

		self.itemScrollbar = tkinter.Scrollbar(self.frame)
		self.itemScrollbar.place(relx=0.47, rely=0.05, relheight=0.20)

		self.itemListbox = tkinter.Listbox(self.frame, bg='white', yscrollcommand=self.itemScrollbar.set)

		self.itemListbox.place(relx=0.07, rely=0.05, relwidth=0.40, relheight=0.20)

		self.saveButton = tkinter.Button(self.frame, text="Save Changes", command=self.addChangedData)
		self.saveButton.place(relx=0.61, rely=0.07, relwidth=0.3, relheight=0.07)

		self.discardButton = tkinter.Button(self.frame, text="Discard Changes", command=self.discardChanges)
		self.discardButton.place(relx=0.61, rely=0.16, relwidth=0.3, relheight=0.07)

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

		self.workingDirectory = tkinter.filedialog.askdirectory(parent=master, initialdir=home,
		                                                        title='Please select the folder that contains the comdat.cfg and comdatmes1.cfg files.')

		self.comdatFileLocation = self.workingDirectory + '/comdat.cfg'
		self.comdatmes1FileLocation = self.workingDirectory + '/comdatmes1.cfg'


		#print(self.comdatFileLocation)
		self.AllItemData = ItemDataFileHandler(self.comdatFileLocation).readFromFile()
		self.AllItemNames = ItemNameFileHandler(self.comdatmes1FileLocation).readFromFile()

		self.populateListbox(self.AllItemData)

		checkBackupFolder(self.workingDirectory)

		saveFiles(self.workingDirectory, self.AllItemNames, self.AllItemData, backup=True)

		self.itemListbox.bind('<<ListboxSelect>>', self.setAllFields)

		self.itemScrollbar.config(command=self.itemListbox.yview)

	def setAllFields(self, event):
		itemSelected = self.itemListbox.curselection()[0]
		currentItemData = self.AllItemData[itemSelected]
		self.itemIDTextField.config(state='normal')
		self.itemIDTextField.delete(0, 'end')
		self.itemIDTextField.insert(0, str(currentItemData.itemID))
		self.itemIDTextField.config(state='readonly')
		self.nameTextField.delete(0, 'end')
		self.nameTextField.insert(0, str(findItemName(currentItemData.itemID, self.AllItemNames)))
		self.typeTextField.delete(0, 'end')
		self.typeTextField.insert(0, str(currentItemData.itemType))
		self.data3TextField.delete(0, 'end')
		self.data3TextField.insert(0, str(currentItemData.data3))

		if currentItemData.data4 == 0:
			self.noRadioButton.invoke()
		else:
			self.yesRadioButton.invoke()

		self.data7TextField.delete(0, 'end')
		self.data7TextField.insert(0, str(currentItemData.data7))
		self.spriteIDTextField.delete(0, 'end')
		self.spriteIDTextField.insert(0, str(currentItemData.spriteIndex))
		self.stackSizeTextField.delete(0, 'end')
		self.stackSizeTextField.insert(0, str(currentItemData.maxStackSize))
		self.totalItemsTextField.delete(0, 'end')
		self.totalItemsTextField.insert(0, str(currentItemData.maxItemCount))
		self.modelTextField.delete(0, 'end')
		self.modelTextField.insert(0, str(currentItemData.itemModelName))
		self.data11TextField.delete(0, 'end')
		self.data11TextField.insert(0, str(currentItemData.data11))

	def getAllData(self):
		changedItemData = [self.itemIDTextField.get(), self.typeTextField.get(), self.data3TextField.get(),
		                   self.hotbar.get(), self.stackSizeTextField.get(), self.totalItemsTextField.get(), self.data7TextField.get(),
		                   self.spriteIDTextField.get(), self.itemIDTextField.get(), self.modelTextField.get(),
		                   self.data11TextField.get()]
		newItem = ItemData(changedItemData)
		return newItem

	def populateListbox(self, allItems):
		for x in range(len(allItems)):
			self.itemListbox.insert(x, "  " + str(allItems[x].itemID) + ": " + str(
				findItemName(allItems[x].itemID, self.AllItemNames)))

	def addChangedData(self):
		changedItem = self.getAllData()
		saveItemEdit(changedItem, self.AllItemData)
		saveItemName(self.nameTextField.get(), self.AllItemNames, changedItem.itemID)
		saveFiles(self.workingDirectory, self.AllItemNames, self.AllItemData, backup=False)
		self.itemListbox.delete(0, self.itemListbox.size())
		self.populateListbox(self.AllItemData)
		self.itemListbox.see(changedItem.itemID)

	def discardChanges(self):
		currentItem = int(self.itemIDTextField.get())
		currentItemData = findItem(currentItem, self.AllItemData)
		self.itemIDTextField.config(state='normal')
		self.itemIDTextField.delete(0, 'end')
		self.itemIDTextField.insert(0, str(currentItemData.itemID))
		self.itemIDTextField.config(state='readonly')
		self.nameTextField.delete(0, 'end')
		self.nameTextField.insert(0, str(findItemName(currentItemData.itemID, self.AllItemNames)))
		self.typeTextField.delete(0, 'end')
		self.typeTextField.insert(0, str(currentItemData.itemType))
		self.data3TextField.delete(0, 'end')
		self.data3TextField.insert(0, str(currentItemData.data3))

		if currentItemData.data4 == 0:
			self.noRadioButton.invoke()
		else:
			self.yesRadioButton.invoke()

		self.data7TextField.delete(0, 'end')
		self.data7TextField.insert(0, str(currentItemData.data7))
		self.spriteIDTextField.delete(0, 'end')
		self.spriteIDTextField.insert(0, str(currentItemData.spriteIndex))
		self.stackSizeTextField.delete(0, 'end')
		self.stackSizeTextField.insert(0, str(currentItemData.maxStackSize))
		self.totalItemsTextField.delete(0, 'end')
		self.totalItemsTextField.insert(0, str(currentItemData.maxItemCount))
		self.modelTextField.delete(0, 'end')
		self.modelTextField.insert(0, str(currentItemData.itemModelName))
		self.data11TextField.delete(0, 'end')
		self.data11TextField.insert(0, str(currentItemData.data11))
