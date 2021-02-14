from RidepodDataReader import RidepodDataFileHandler, ridepodBodyData, ridepodWeaponData, ridepodLegData, \
	ridepodEnergyPackData
from ItemNameDataReader import ItemNameFileHandler
from ItemDataReader import ItemDataFileHandler, getAllWeapons
from AppSettingsHandler import getWorkingDirectory
from DataDisplay import DataDisplay
from DataHelperFunctions import getAllRidepodPartNames, setTextField
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from pathlib import Path

home = str(Path.home())


class DarkCloud2RidepodDisplay(DataDisplay):
	def __init__(self):
		newWindow = tkinter.Toplevel()
		newWindow.title('Dark Cloud 2 Ridepod Part Modifier')

		Height = 600
		Width = 550

		self.workingDirectory = getWorkingDirectory(newWindow)
		# self.robotdatFileLocation = self.workingDirectory
		self.RidepodDataFile = RidepodDataFileHandler(self.workingDirectory)
		self.ItemNameFile = ItemNameFileHandler(self.workingDirectory)
		self.AllRidepodData = self.RidepodDataFile.readFromFile()
		self.AllItemNames = self.ItemNameFile.readFromFile()

		self.AllRidepodItemNames = getAllRidepodPartNames(self.AllRidepodData, self.AllItemNames)

		self.canvas = tkinter.Canvas(newWindow, height=Height, width=Width)
		self.canvas.pack()

		self.mainFrame = tkinter.Frame(newWindow, borderwidth=1)
		self.mainFrame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.45)

		self.ridepodPartScrollbar = tkinter.Scrollbar(self.mainFrame)
		self.ridepodPartScrollbar.place(relx=0.47, rely=0.05, relheight=0.5)

		self.ridepodPartListbox = tkinter.Listbox(self.mainFrame, bg='white',
												  yscrollcommand=self.ridepodPartScrollbar.set)
		self.ridepodPartListbox.place(relx=0.07, rely=0.05, relwidth=0.40, relheight=0.5)

		self.saveButton = tkinter.Button(self.mainFrame, text="Save Changes", command=self.saveData)
		self.saveButton.place(relx=0.61, rely=0.12, relwidth=0.3, relheight=0.09)

		self.discardButton = tkinter.Button(self.mainFrame, text="Discard Changes", command=self.discardChanges)
		self.discardButton.place(relx=0.61, rely=0.35, relwidth=0.3, relheight=0.09)

		self.ridepodPartItemIDLabel = tkinter.Label(self.mainFrame, text='itemID: ')
		self.ridepodPartItemIDLabel.place(relx=0.12, rely=0.68)
		self.ridepodPartItemIDTextField = tkinter.Entry(self.mainFrame)
		self.ridepodPartItemIDTextField.place(relx=0.23, rely=0.67, relwidth=0.12)
		self.ridepodPartTypeLabel = tkinter.Label(self.mainFrame, text='Part Type: ')
		self.ridepodPartTypeLabel.place(relx=0.5, rely=0.68)
		self.ridepodPartTypeTextField = tkinter.Entry(self.mainFrame)
		self.ridepodPartTypeTextField.place(relx=0.65, rely=0.67, relwidth=0.12)

		self.ridepodPartCapacityLabel = tkinter.Label(self.mainFrame, text='Capacity: ')
		self.ridepodPartCapacityLabel.place(relx=0.09, rely=0.88)
		self.ridepodPartCapacityTextField = tkinter.Entry(self.mainFrame)
		self.ridepodPartCapacityTextField.place(relx=0.23, rely=0.87, relwidth=0.12)

		self.ridepodPartdata4Label = tkinter.Label(self.mainFrame, text='data4: ')
		self.ridepodPartdata4Label.place(relx=0.55, rely=0.88)
		self.ridepodPartdata4TextField = tkinter.Entry(self.mainFrame)
		self.ridepodPartdata4TextField.place(relx=0.65, rely=0.87, relwidth=0.12)

		self.populateListbox(self.AllRidepodData)

		self.ridepodPartListbox.bind('<<ListboxSelect>>', lambda listbox: self.setAllFields(getNewSelection=True))

		self.ridepodPartScrollbar.config(command=self.ridepodPartListbox.yview)

		# Requires defense and model name
		self.ridepodBodyFrame = tkinter.Frame(newWindow)

		self.ridepodPartdefenseLabel = tkinter.Label(self.ridepodBodyFrame, text='Defense: ')
		self.ridepodPartdefenseLabel.place(relx=0.10, rely=0.035)
		self.ridepodPartdefenseTextField = tkinter.Entry(self.ridepodBodyFrame)
		self.ridepodPartdefenseTextField.place(relx=0.23, rely=0.035, relwidth=0.12)

		self.ridepodPartBodyModelNameLabel = tkinter.Label(self.ridepodBodyFrame, text='Model Name: ')
		self.ridepodPartBodyModelNameLabel.place(relx=0.47, rely=0.035)
		self.ridepodPartBodyModelNameTextField = tkinter.Entry(self.ridepodBodyFrame)
		self.ridepodPartBodyModelNameTextField.place(relx=0.65, rely=0.035, relwidth=0.12)

		#self.ridepodBodyFrame.place_forget()


		# Requires full weapon stats, including hit points, data 14, and model name
		self.ridepodWeaponFrame = tkinter.Frame(newWindow)


		row1Labelrelx = 0.10
		row1TextFieldrelx = 0.23
		row2Labelrelx = 0.47
		row2TextFieldrelx = 0.65

		self.hitPointsLabel = tkinter.Label(self.ridepodWeaponFrame, text='Hit Points')
		self.hitPointsLabel.place(relx=row1Labelrelx+0.22, rely=0.01)
		self.hitPointsTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.hitPointsTextField.place(relx=row1TextFieldrelx+0.22, rely=0.0, relwidth=0.12)

		self.AttackLabel = tkinter.Label(self.ridepodWeaponFrame, text='Attack')
		self.AttackLabel.place(relx=row1Labelrelx, rely=0.16)
		self.AttackTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.AttackTextField.place(relx=row1TextFieldrelx, rely=0.15, relwidth=0.12)

		self.DurableLabel = tkinter.Label(self.ridepodWeaponFrame, text='Durable')
		self.DurableLabel.place(relx=row2Labelrelx, rely=0.16)
		self.DurableTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.DurableTextField.place(relx=row2TextFieldrelx, rely=0.15, relwidth=0.12)

		self.FlameLabel = tkinter.Label(self.ridepodWeaponFrame, text='Flame')
		self.FlameLabel.place(relx=row1Labelrelx, rely=0.28)
		self.FlameTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.FlameTextField.place(relx=row1TextFieldrelx, rely=0.27, relwidth=0.12)

		self.ChillLabel = tkinter.Label(self.ridepodWeaponFrame, text='Chill')
		self.ChillLabel.place(relx=row2Labelrelx, rely=0.28)
		self.ChillTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.ChillTextField.place(relx=row2TextFieldrelx, rely=0.27, relwidth=0.12)

		self.LightningLabel = tkinter.Label(self.ridepodWeaponFrame, text='Lightning')
		self.LightningLabel.place(relx=row1Labelrelx, rely=0.40)
		self.LightningTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.LightningTextField.place(relx=row1TextFieldrelx, rely=0.39, relwidth=0.12)

		self.CycloneLabel = tkinter.Label(self.ridepodWeaponFrame, text='Cyclone')
		self.CycloneLabel.place(relx=row2Labelrelx, rely=0.40)
		self.CycloneTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.CycloneTextField.place(relx=row2TextFieldrelx, rely=0.39, relwidth=0.12)

		self.SmashLabel = tkinter.Label(self.ridepodWeaponFrame, text='Smash')
		self.SmashLabel.place(relx=row1Labelrelx, rely=0.52)
		self.SmashTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.SmashTextField.place(relx=row1TextFieldrelx, rely=0.51, relwidth=0.12)

		self.ExorcismLabel = tkinter.Label(self.ridepodWeaponFrame, text='Exorcism')
		self.ExorcismLabel.place(relx=row2Labelrelx, rely=0.52)
		self.ExorcismTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.ExorcismTextField.place(relx=row2TextFieldrelx, rely=0.51, relwidth=0.12)

		self.BeastLabel = tkinter.Label(self.ridepodWeaponFrame, text='Beast')
		self.BeastLabel.place(relx=row1Labelrelx, rely=0.64)
		self.BeastTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.BeastTextField.place(relx=row1TextFieldrelx, rely=0.63, relwidth=0.12)

		self.ScaleLabel = tkinter.Label(self.ridepodWeaponFrame, text='Scale')
		self.ScaleLabel.place(relx=row2Labelrelx, rely=0.64)
		self.ScaleTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.ScaleTextField.place(relx=row2TextFieldrelx, rely=0.63, relwidth=0.12)

		self.data14label = tkinter.Label(self.ridepodWeaponFrame, text='data14')
		self.data14label.place(relx=row1Labelrelx, rely=0.76)
		self.data14TextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.data14TextField.place(relx=row1TextFieldrelx, rely=0.74, relwidth=0.12)

		self.weaponModelNameLabel = tkinter.Label(self.ridepodWeaponFrame, text='Model Name')
		self.weaponModelNameLabel.place(relx=row2Labelrelx, rely=0.76)
		self.weaponModelNameTextField = tkinter.Entry(self.ridepodWeaponFrame)
		self.weaponModelNameTextField.place(relx=row2TextFieldrelx, rely=0.75, relwidth=0.12)


		self.ridepodLegFrame = tkinter.Frame(newWindow)


		self.ridepodPartdata5Label = tkinter.Label(self.ridepodLegFrame, text='data5: ')
		self.ridepodPartdata5Label.place(relx=0.125, rely=0.036)
		self.ridepodPartdata5TextField = tkinter.Entry(self.ridepodLegFrame)
		self.ridepodPartdata5TextField.place(relx=0.23, rely=0.035, relwidth=0.12)

		self.ridepodPartdata6Label = tkinter.Label(self.ridepodLegFrame, text='data6: ')
		self.ridepodPartdata6Label.place(relx=0.55, rely=0.036)
		self.ridepodPartdata6TextField = tkinter.Entry(self.ridepodLegFrame)
		self.ridepodPartdata6TextField.place(relx=0.65, rely=0.035, relwidth=0.12)



		self.ridepodEnergyPackFrame = tkinter.Frame(newWindow)


		self.ridepodPartmaxFuelLabel = tkinter.Label(self.ridepodEnergyPackFrame, text='Max Fuel: ')
		self.ridepodPartmaxFuelLabel.place(relx=0.09, rely=0.036)
		self.ridepodPartmaxFuelTextField = tkinter.Entry(self.ridepodEnergyPackFrame)
		self.ridepodPartmaxFuelTextField.place(relx=0.23, rely=0.035, relwidth=0.12)

		self.RidepodDataFile.backupFile(self.AllRidepodData)


	def getCurrentDataSelected(self):
		if str(self.ridepodPartListbox.curselection()) != '()':
			self.currentListboxIndex = self.ridepodPartListbox.curselection()[0]
			currentRidepodPartData = self.AllRidepodData[self.currentListboxIndex]
			return currentRidepodPartData

	def populateListbox(self, allRidepodData):
		for x in range(len(allRidepodData)):
			self.ridepodPartListbox.insert(x, " " + str([self.AllRidepodData[x].itemID]) + ": " + str(
				self.AllRidepodItemNames[x]))

	def getRidepodPartType(self, currentRidepodPartData):
		# Determine if part is a Body, Arm, Leg, or Energy Pack Part
		if isinstance(currentRidepodPartData, ridepodBodyData):
			# Update text fields with GUI for Body Editing
			return ('body')

		elif isinstance(currentRidepodPartData, ridepodWeaponData):
			# Update text fields with GUI for Weapon Editing
			return ('weapon')

		elif isinstance(currentRidepodPartData, ridepodLegData):
			# Update text fields with GUI for ridepodLegData
			return ('leg')

		else:
			# Should be ridepodEnergyPackData, update GUI for it
			# IF IT'S NOT, kill self.

			return ('energypack')



	def setAllFields(self, getNewSelection):
		if (getNewSelection == True):
			currentRidepodPart = self.getCurrentDataSelected()
			if currentRidepodPart is None:
				return


		else:
			currentRidepodPart = self.AllRidepodData[self.currentListboxIndex]

		newRidepodPartType = self.getRidepodPartType(currentRidepodPart)


		self.ridepodBodyFrame.place_forget()
		self.ridepodWeaponFrame.place_forget()
		self.ridepodLegFrame.place_forget()
		self.ridepodEnergyPackFrame.place_forget()

		setTextField(self.ridepodPartItemIDTextField, currentRidepodPart.itemID)
		setTextField(self.ridepodPartTypeTextField, currentRidepodPart.partType)
		setTextField(self.ridepodPartCapacityTextField, currentRidepodPart.capacity)
		setTextField(self.ridepodPartdata4TextField, currentRidepodPart.data4)

		if (newRidepodPartType == 'body'):
			setTextField(self.ridepodPartdefenseTextField, currentRidepodPart.defense)
			setTextField(self.ridepodPartBodyModelNameTextField, currentRidepodPart.modelName)
			self.ridepodBodyFrame.place(relx=0.025, rely=0.5, relwidth=0.95, relheight=0.40)


		elif (newRidepodPartType == 'weapon'):

			setTextField(self.hitPointsTextField, currentRidepodPart.hitPoints)
			setTextField(self.DurableTextField, currentRidepodPart.durable)
			setTextField(self.AttackTextField, currentRidepodPart.attack)
			setTextField(self.FlameTextField, currentRidepodPart.flame)
			setTextField(self.ChillTextField, currentRidepodPart.chill)
			setTextField(self.LightningTextField, currentRidepodPart.lightning)
			setTextField(self.CycloneTextField, currentRidepodPart.cyclone)
			setTextField(self.SmashTextField, currentRidepodPart.smash)
			setTextField(self.ExorcismTextField, currentRidepodPart.exorcism)
			setTextField(self.BeastTextField, currentRidepodPart.beast)
			setTextField(self.ScaleTextField, currentRidepodPart.scale)
			setTextField(self.data14TextField, currentRidepodPart.data14)
			setTextField(self.weaponModelNameTextField, currentRidepodPart.modelName)
			self.ridepodWeaponFrame.place(relx=0.025, rely=0.5, relwidth=0.95, relheight=0.40)



		elif (newRidepodPartType == 'leg'):
			setTextField(self.ridepodPartdata5TextField, currentRidepodPart.data5)
			setTextField(self.ridepodPartdata6TextField, currentRidepodPart.data6)
			self.ridepodLegFrame.place(relx=0.025, rely=0.5, relwidth=0.95, relheight=0.40)


		elif (newRidepodPartType == 'energypack'):
			setTextField(self.ridepodPartmaxFuelTextField, currentRidepodPart.maxFuel)
			self.ridepodEnergyPackFrame.place(relx=0.025, rely=0.5, relwidth=0.95, relheight=0.40)


	def getDataFromFields(self):
		currentRidepodPartType = self.getRidepodPartType(self.AllRidepodData[self.currentListboxIndex])

		mainChangedPartData = [self.ridepodPartItemIDTextField.get(), self.ridepodPartTypeTextField.get(), self.ridepodPartCapacityTextField.get(), self.ridepodPartdata4TextField.get()]

		if currentRidepodPartType == 'body':
			changedBodyData = [self.ridepodPartdefenseTextField.get(), self.ridepodPartBodyModelNameTextField.get()]
			fullChangedPartData = ridepodBodyData(mainChangedPartData + changedBodyData)

		elif currentRidepodPartType == 'weapon':
			changedWeaponData = [self.hitPointsTextField.get(), self.AttackTextField.get(), self.DurableTextField.get(), self.FlameTextField.get(), self.ChillTextField.get(), self.LightningTextField.get(), self.CycloneTextField.get(), self.SmashTextField.get(), self. ExorcismTextField.get(), self.BeastTextField.get(), self.ScaleTextField.get(), self.data14TextField.get(), self.weaponModelNameTextField.get()]
			fullChangedPartData = ridepodWeaponData(mainChangedPartData + changedWeaponData)
			#print("Attack: " + str(fullChangedPartData.attack))
			#print("Durable: " + str(fullChangedPartData.durable))

		elif currentRidepodPartType == 'leg':
			changedLegData = [self.ridepodPartdata5TextField.get(), self.ridepodPartdata6TextField.get()]
			fullChangedPartData = ridepodLegData(mainChangedPartData + changedLegData)

		else:
			changedEnergyPackData = [self.ridepodPartmaxFuelTextField.get()]
			fullChangedPartData = ridepodEnergyPackData(mainChangedPartData + changedEnergyPackData)

		return fullChangedPartData


	def saveData(self):
		changedData = self.getDataFromFields()

		self.AllRidepodData[self.currentListboxIndex] = changedData
		self.RidepodDataFile.writeToFile(self.AllRidepodData)

		self.ridepodPartListbox.delete(0,self.ridepodPartListbox.size())
		self.populateListbox(self.AllRidepodData)
		self.ridepodPartListbox.see(self.currentListboxIndex)