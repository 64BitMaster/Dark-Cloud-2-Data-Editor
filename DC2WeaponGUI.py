from WeaponDataReader import WeaponDataFileHandler, WeaponData, checkWeaponDataTypes
from ItemNameDataReader import ItemNameFileHandler
from ItemDataReader import ItemDataFileHandler, getAllWeapons
from AppSettingsHandler import getWorkingDirectory
from DataDisplay import DataDisplay
from DataHelperFunctions import getAllWeaponNames, setTextField
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from pathlib import Path

home = str(Path.home())


class DarkCloud2WeaponDisplay(DataDisplay):
	def __init__(self):
		newWindow = tkinter.Toplevel()
		newWindow.title('Dark Cloud 2 Weapon Modifier')

		Height = 600
		Width = 550

		self.workingDirectory = getWorkingDirectory(newWindow)
		self.comdatFileLocation = self.workingDirectory
		self.WeaponDataFile = WeaponDataFileHandler(self.comdatFileLocation)
		self.ItemNameFile = ItemNameFileHandler(self.comdatFileLocation)
		self.ItemDataFile = ItemDataFileHandler(self.comdatFileLocation)

		self.AllWeaponData = self.WeaponDataFile.readFromFile()
		self.AllItemData = self.ItemDataFile.readFromFile()
		self.AllItemNames = self.ItemNameFile.readFromFile()
		self.AllWeaponItemData = getAllWeapons(self.AllItemData)

		self.canvas = tkinter.Canvas(newWindow, height=Height, width=Width)
		self.canvas.pack()

		self.frame = tkinter.Frame(newWindow)
		self.frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

		self.weaponScrollbar = tkinter.Scrollbar(self.frame)
		self.weaponScrollbar.place(relx=0.47, rely=0.05, relheight=0.15)

		self.weaponListbox = tkinter.Listbox(self.frame, bg='white', yscrollcommand=self.weaponScrollbar.set)
		self.weaponListbox.place(relx=0.07, rely=0.05, relwidth=0.40, relheight=0.15)

		self.saveButton = tkinter.Button(self.frame, text="Save Changes", command=self.saveData)
		self.saveButton.place(relx=0.61, rely=0.07, relwidth=0.3, relheight=0.035)

		self.discardButton = tkinter.Button(self.frame, text="Discard Changes", command=self.discardChanges)
		self.discardButton.place(relx=0.61, rely=0.16, relwidth=0.3, relheight=0.035)

		self.data1Label = tkinter.Label(self.frame, text='data1:')
		self.data1Label.place(relx=.22, rely=.27)
		self.data1TextField = tkinter.Entry(self.frame)
		self.data1TextField.place(relx=.31, rely=.27, relwidth=.10, relheight=0.04)

		self.data2Label = tkinter.Label(self.frame, text='data2:')
		self.data2Label.place(relx=.54, rely=.27)
		self.data2TextField = tkinter.Entry(self.frame)
		self.data2TextField.place(relx=.63, rely=.27, relwidth=.10, relheight=0.04)

		self.minimumStatsLabel = tkinter.Label(self.frame, text='Minimum Stats:')
		self.minimumStatsLabel.place(relx=0.15, rely=0.35)

		row1Labelrelx = 0.0
		row1TextFieldrelx = 0.12
		row2Labelrelx = 0.25
		row2TextFieldrelx = 0.37

		self.minimumAttackLabel = tkinter.Label(self.frame, text='Attack')
		self.minimumAttackLabel.place(relx=row1Labelrelx, rely=0.4)
		self.minimumAttackTextField = tkinter.Entry(self.frame)
		self.minimumAttackTextField.place(relx=row1TextFieldrelx, rely=0.4, relwidth=0.10, relheight=0.04)

		self.minimumDurableLabel = tkinter.Label(self.frame, text='Durable')
		self.minimumDurableLabel.place(relx=row2Labelrelx, rely=0.4)
		self.minimumDurableTextField = tkinter.Entry(self.frame)
		self.minimumDurableTextField.place(relx=row2TextFieldrelx, rely=0.4, relwidth=0.10, relheight=0.04)

		self.minimumFlameLabel = tkinter.Label(self.frame, text='Flame')
		self.minimumFlameLabel.place(relx=row1Labelrelx, rely=0.45)
		self.minimumFlameTextField = tkinter.Entry(self.frame)
		self.minimumFlameTextField.place(relx=row1TextFieldrelx, rely=0.45, relwidth=0.10, relheight=0.04)

		self.minimumChillLabel = tkinter.Label(self.frame, text='Chill')
		self.minimumChillLabel.place(relx=row2Labelrelx, rely=0.45)
		self.minimumChillTextField = tkinter.Entry(self.frame)
		self.minimumChillTextField.place(relx=row2TextFieldrelx, rely=0.45, relwidth=0.10, relheight=0.04)

		self.minimumLightningLabel = tkinter.Label(self.frame, text='Lightning')
		self.minimumLightningLabel.place(relx=row1Labelrelx, rely=0.5)
		self.minimumLightningTextField = tkinter.Entry(self.frame)
		self.minimumLightningTextField.place(relx=row1TextFieldrelx, rely=0.5, relwidth=0.10, relheight=0.04)

		self.minimumCycloneLabel = tkinter.Label(self.frame, text='Cyclone')
		self.minimumCycloneLabel.place(relx=row2Labelrelx, rely=0.5)
		self.minimumCycloneTextField = tkinter.Entry(self.frame)
		self.minimumCycloneTextField.place(relx=row2TextFieldrelx, rely=0.5, relwidth=0.10, relheight=0.04)

		self.minimumSmashLabel = tkinter.Label(self.frame, text='Smash')
		self.minimumSmashLabel.place(relx=row1Labelrelx, rely=0.55)
		self.minimumSmashTextField = tkinter.Entry(self.frame)
		self.minimumSmashTextField.place(relx=row1TextFieldrelx, rely=0.55, relwidth=0.10, relheight=0.04)

		self.minimumExorcismLabel = tkinter.Label(self.frame, text='Exorcism')
		self.minimumExorcismLabel.place(relx=row2Labelrelx, rely=0.55)
		self.minimumExorcismTextField = tkinter.Entry(self.frame)
		self.minimumExorcismTextField.place(relx=row2TextFieldrelx, rely=0.55, relwidth=0.10, relheight=0.04)

		self.minimumBeastLabel = tkinter.Label(self.frame, text='Beast')
		self.minimumBeastLabel.place(relx=row1Labelrelx, rely=0.6)
		self.minimumBeastTextField = tkinter.Entry(self.frame)
		self.minimumBeastTextField.place(relx=row1TextFieldrelx, rely=0.6, relwidth=0.10, relheight=0.04)

		self.minimumScaleLabel = tkinter.Label(self.frame, text='Scale')
		self.minimumScaleLabel.place(relx=row2Labelrelx, rely=0.6)
		self.minimumScaleTextField = tkinter.Entry(self.frame)
		self.minimumScaleTextField.place(relx=row2TextFieldrelx, rely=0.6, relwidth=0.10, relheight=0.04)

		# Maxiumum Stats
		maximumStatShift = 0.53
		row3Labelrelx = row1Labelrelx + maximumStatShift
		row3TextFieldrelx = row1TextFieldrelx + maximumStatShift
		row4Labelrelx = row2Labelrelx + maximumStatShift
		row4TextFieldrelx = row2TextFieldrelx + maximumStatShift

		self.maximumStatsLabel = tkinter.Label(self.frame, text='Maximum Stats:')
		self.maximumStatsLabel.place(relx=0.68, rely=0.35)

		self.maximumAttackLabel = tkinter.Label(self.frame, text='Attack')
		self.maximumAttackLabel.place(relx=row3Labelrelx, rely=0.4)
		self.maximumAttackTextField = tkinter.Entry(self.frame)
		self.maximumAttackTextField.place(relx=row3TextFieldrelx, rely=0.4, relwidth=0.10, relheight=0.04)

		self.maximumDurableLabel = tkinter.Label(self.frame, text='Durable')
		self.maximumDurableLabel.place(relx=row4Labelrelx, rely=0.4)
		self.maximumDurableTextField = tkinter.Entry(self.frame)
		self.maximumDurableTextField.place(relx=row4TextFieldrelx, rely=0.4, relwidth=0.10, relheight=0.04)

		self.maximumFlameLabel = tkinter.Label(self.frame, text='Flame')
		self.maximumFlameLabel.place(relx=row3Labelrelx, rely=0.45)
		self.maximumFlameTextField = tkinter.Entry(self.frame)
		self.maximumFlameTextField.place(relx=row3TextFieldrelx, rely=0.45, relwidth=0.10, relheight=0.04)

		self.maximumChillLabel = tkinter.Label(self.frame, text='Chill')
		self.maximumChillLabel.place(relx=row4Labelrelx, rely=0.45)
		self.maximumChillTextField = tkinter.Entry(self.frame)
		self.maximumChillTextField.place(relx=row4TextFieldrelx, rely=0.45, relwidth=0.10, relheight=0.04)

		self.maximumLightningLabel = tkinter.Label(self.frame, text='Lightning')
		self.maximumLightningLabel.place(relx=row3Labelrelx, rely=0.5)
		self.maximumLightningTextField = tkinter.Entry(self.frame)
		self.maximumLightningTextField.place(relx=row3TextFieldrelx, rely=0.5, relwidth=0.10, relheight=0.04)

		self.maximumCycloneLabel = tkinter.Label(self.frame, text='Cyclone')
		self.maximumCycloneLabel.place(relx=row4Labelrelx, rely=0.5)
		self.maximumCycloneTextField = tkinter.Entry(self.frame)
		self.maximumCycloneTextField.place(relx=row4TextFieldrelx, rely=0.5, relwidth=0.10, relheight=0.04)

		self.maximumSmashLabel = tkinter.Label(self.frame, text='Smash')
		self.maximumSmashLabel.place(relx=row3Labelrelx, rely=0.55)
		self.maximumSmashTextField = tkinter.Entry(self.frame)
		self.maximumSmashTextField.place(relx=row3TextFieldrelx, rely=0.55, relwidth=0.10, relheight=0.04)

		self.maximumExorcismLabel = tkinter.Label(self.frame, text='Exorcism')
		self.maximumExorcismLabel.place(relx=row4Labelrelx, rely=0.55)
		self.maximumExorcismTextField = tkinter.Entry(self.frame)
		self.maximumExorcismTextField.place(relx=row4TextFieldrelx, rely=0.55, relwidth=0.10, relheight=0.04)

		self.maximumBeastLabel = tkinter.Label(self.frame, text='Beast')
		self.maximumBeastLabel.place(relx=row3Labelrelx, rely=0.60)
		self.maximumBeastTextField = tkinter.Entry(self.frame)
		self.maximumBeastTextField.place(relx=row3TextFieldrelx, rely=0.60, relwidth=0.10, relheight=0.04)

		self.maximumScaleLabel = tkinter.Label(self.frame, text='Scale')
		self.maximumScaleLabel.place(relx=row4Labelrelx, rely=0.60)
		self.maximumScaleTextField = tkinter.Entry(self.frame)
		self.maximumScaleTextField.place(relx=row4TextFieldrelx, rely=0.60, relwidth=0.10, relheight=0.04)

		# Unknown data fields, lmao

		unknownDataLabelRow1 = 0.13
		unknownDataTextFieldRow1 = 0.24
		unknownDataLabelRow2 = unknownDataLabelRow1 + 0.26
		unknownDataTextFieldRow2 = unknownDataTextFieldRow1 + 0.26
		unknownDataLabelRow3 = unknownDataLabelRow2 + 0.26
		unknownDataTextFieldRow3 = unknownDataTextFieldRow2 + 0.26

		self.data23Label = tkinter.Label(self.frame, text='data23:')
		self.data23Label.place(relx=unknownDataLabelRow1, rely=0.68)
		self.data23TextField = tkinter.Entry(self.frame)
		self.data23TextField.place(relx=unknownDataTextFieldRow1, rely=0.68, relwidth=0.10, relheight=0.04)

		self.data24Label = tkinter.Label(self.frame, text='data24:')
		self.data24Label.place(relx=unknownDataLabelRow2, rely=0.68)
		self.data24TextField = tkinter.Entry(self.frame)
		self.data24TextField.place(relx=unknownDataTextFieldRow2, rely=0.68, relwidth=0.10, relheight=0.04)

		self.data25Label = tkinter.Label(self.frame, text='data25:')
		self.data25Label.place(relx=unknownDataLabelRow3, rely=0.68)
		self.data25TextField = tkinter.Entry(self.frame)
		self.data25TextField.place(relx=unknownDataTextFieldRow3, rely=0.68, relwidth=0.10, relheight=0.04)

		self.data26Label = tkinter.Label(self.frame, text='data26:')
		self.data26Label.place(relx=unknownDataLabelRow1, rely=0.74)
		self.data26TextField = tkinter.Entry(self.frame)
		self.data26TextField.place(relx=unknownDataTextFieldRow1, rely=0.74, relwidth=0.10, relheight=0.04)

		self.data27Label = tkinter.Label(self.frame, text='data27:')
		self.data27Label.place(relx=unknownDataLabelRow2, rely=0.74)
		self.data27TextField = tkinter.Entry(self.frame)
		self.data27TextField.place(relx=unknownDataTextFieldRow2, rely=0.74, relwidth=0.10, relheight=0.04)

		self.data28Label = tkinter.Label(self.frame, text='data28:')
		self.data28Label.place(relx=unknownDataLabelRow3, rely=0.74)
		self.data28TextField = tkinter.Entry(self.frame)
		self.data28TextField.place(relx=unknownDataTextFieldRow3, rely=0.74, relwidth=0.10, relheight=0.04)

		self.data29Label = tkinter.Label(self.frame, text='data29:')
		self.data29Label.place(relx=unknownDataLabelRow2, rely=0.80)
		self.data29TextField = tkinter.Entry(self.frame)
		self.data29TextField.place(relx=unknownDataTextFieldRow2, rely=0.80, relwidth=0.10, relheight=0.04)

		# Build up data fields

		firstBuildUpLabelRow1 = 0.02
		firstBuildUpTextFieldRow1 = 0.19
		secondBuildUpLabelRow1 = firstBuildUpLabelRow1 + 0.31
		secondBuildUpTextFieldRow1 = firstBuildUpTextFieldRow1 + 0.31
		thirdBuildUpLabelRow1 = secondBuildUpLabelRow1 + 0.31
		thirdBuildUpTextFieldRow1 = secondBuildUpTextFieldRow1 + 0.31

		self.firstBuildUpLabel = tkinter.Label(self.frame, text='1st Build Up:')
		self.firstBuildUpLabel.place(relx=firstBuildUpLabelRow1, rely=0.86)
		self.firstBuildUpTextField = tkinter.Entry(self.frame)
		self.firstBuildUpTextField.place(relx=firstBuildUpTextFieldRow1, rely=0.86, relwidth=0.10, relheight=0.04)

		self.secondBuildUpLabel = tkinter.Label(self.frame, text='2nd Build Up:')
		self.secondBuildUpLabel.place(relx=secondBuildUpLabelRow1, rely=0.86)
		self.secondBuildUpTextField = tkinter.Entry(self.frame)
		self.secondBuildUpTextField.place(relx=secondBuildUpTextFieldRow1, rely=0.86, relwidth=0.10, relheight=0.04)

		self.thirdBuildUpLabel = tkinter.Label(self.frame, text='3rd Build Up:')
		self.thirdBuildUpLabel.place(relx=thirdBuildUpLabelRow1, rely=0.86)
		self.thirdBuildUpTextField = tkinter.Entry(self.frame)
		self.thirdBuildUpTextField.place(relx=thirdBuildUpTextFieldRow1, rely=0.86, relwidth=0.10, relheight=0.04)

		# Build up Monster Requirements

		firstMonsterRequirementLabelRow1 = 0.00
		firstMonsterRequirementTextFieldRow1 = 0.21
		secondMonsterRequirementLabelRow1 = firstMonsterRequirementLabelRow1 + 0.33
		secondMonsterRequirementTextFieldRow1 = firstMonsterRequirementTextFieldRow1 + 0.34
		thirdMonsterRequirementLabelRow1 = secondMonsterRequirementLabelRow1 + 0.35
		thirdMonsterRequirementTextFieldRow1 = secondMonsterRequirementTextFieldRow1 + 0.35

		self.firstMonsterRequirementLabel = tkinter.Label(self.frame, text='1st Monster Req:')
		self.firstMonsterRequirementLabel.place(relx=firstMonsterRequirementLabelRow1, rely=0.92)
		self.firstMonsterRequirementTextField = tkinter.Entry(self.frame)
		self.firstMonsterRequirementTextField.place(relx=firstMonsterRequirementTextFieldRow1, rely=0.92, relwidth=0.10,
													relheight=0.04)

		self.secondMonsterRequirementLabel = tkinter.Label(self.frame, text='2nd Monster Req:')
		self.secondMonsterRequirementLabel.place(relx=secondMonsterRequirementLabelRow1, rely=0.92)
		self.secondMonsterRequirementTextField = tkinter.Entry(self.frame)
		self.secondMonsterRequirementTextField.place(relx=secondMonsterRequirementTextFieldRow1, rely=0.92,
													 relwidth=0.10, relheight=0.04)

		self.thirdMonsterRequirementLabel = tkinter.Label(self.frame, text='3rd Monster Req:')
		self.thirdMonsterRequirementLabel.place(relx=thirdMonsterRequirementLabelRow1, rely=0.92)
		self.thirdMonsterRequirementTextField = tkinter.Entry(self.frame)
		self.thirdMonsterRequirementTextField.place(relx=thirdMonsterRequirementTextFieldRow1, rely=0.92, relwidth=0.10,
													relheight=0.04)

		self.AllWeaponNames = getAllWeaponNames(self.AllWeaponItemData, self.AllItemNames)
		self.populateListbox(self.AllWeaponData)


		self.WeaponDataFile.backupFile(self.AllWeaponData)


		self.weaponListbox.bind('<<ListboxSelect>>', lambda listbox: self.setAllFields(getNewSelection=True))

		self.weaponScrollbar.config(command=self.weaponListbox.yview)

	def getCurrentDataSelected(self):
		if str(self.weaponListbox.curselection()) != '()':
			self.currentListboxIndex = self.weaponListbox.curselection()[0]
			currentWeaponData = self.AllWeaponData[self.currentListboxIndex]
			return currentWeaponData

	def populateListbox(self, allWeapons):
		for x in range(len(allWeapons)):
			self.weaponListbox.insert(x, " " + str([self.AllWeaponItemData[x].itemID]) + ": " + str(
				self.AllWeaponNames[x]))

	def setAllFields(self, getNewSelection):
		if (getNewSelection == True):
			currentWeaponData = self.getCurrentDataSelected()
			if currentWeaponData is None:
				return

		else:
			currentWeaponData = self.AllWeaponData[self.currentListboxIndex]

		setTextField(self.data1TextField, currentWeaponData.data1)
		setTextField(self.data2TextField, currentWeaponData.data2)

		setTextField(self.minimumAttackTextField, currentWeaponData.minimumAttack)
		setTextField(self.minimumDurableTextField, currentWeaponData.minimumDurable)
		setTextField(self.minimumFlameTextField, currentWeaponData.minimumFlame)
		setTextField(self.minimumChillTextField, currentWeaponData.minimumChill)
		setTextField(self.minimumLightningTextField, currentWeaponData.minimumLightning)
		setTextField(self.minimumCycloneTextField, currentWeaponData.minimumCyclone)
		setTextField(self.minimumSmashTextField, currentWeaponData.minimumSmash)
		setTextField(self.minimumExorcismTextField, currentWeaponData.minimumExorcism)
		setTextField(self.minimumBeastTextField, currentWeaponData.minimumBeast)
		setTextField(self.minimumScaleTextField, currentWeaponData.minimumScale)

		setTextField(self.maximumAttackTextField, currentWeaponData.maximumAttack)
		setTextField(self.maximumDurableTextField, currentWeaponData.maximumDurable)
		setTextField(self.maximumFlameTextField, currentWeaponData.maximumFlame)
		setTextField(self.maximumChillTextField, currentWeaponData.maximumChill)
		setTextField(self.maximumLightningTextField, currentWeaponData.maximumLightning)
		setTextField(self.maximumCycloneTextField, currentWeaponData.maximumCyclone)
		setTextField(self.maximumSmashTextField, currentWeaponData.maximumSmash)
		setTextField(self.maximumExorcismTextField, currentWeaponData.maximumExorcism)
		setTextField(self.maximumBeastTextField, currentWeaponData.maximumBeast)
		setTextField(self.maximumScaleTextField, currentWeaponData.maximumScale)

		setTextField(self.data23TextField, currentWeaponData.data23)
		setTextField(self.data24TextField, currentWeaponData.data24)
		setTextField(self.data25TextField, currentWeaponData.data25)
		setTextField(self.data26TextField, currentWeaponData.data26)
		setTextField(self.data27TextField, currentWeaponData.data27)
		setTextField(self.data28TextField, currentWeaponData.data28)
		setTextField(self.data29TextField, currentWeaponData.data29)

		setTextField(self.firstBuildUpTextField, currentWeaponData.firstBuildUp)
		setTextField(self.secondBuildUpTextField, currentWeaponData.secondBuildUp)
		setTextField(self.thirdBuildUpTextField, currentWeaponData.thirdBuildUp)

		setTextField(self.firstMonsterRequirementTextField, currentWeaponData.firstMonsterRequirement)
		setTextField(self.secondMonsterRequirementTextField, currentWeaponData.secondMonsterRequirement)
		setTextField(self.thirdMonsterRequirementTextField, currentWeaponData.thirdMonsterRequirement)

	def getDataFromFields(self):
		changedWeaponData = [self.data1TextField.get(), self.data2TextField.get(), self.minimumAttackTextField.get(),
							 self.minimumDurableTextField.get(), self.maximumAttackTextField.get(),
							 self.maximumDurableTextField.get(), self.minimumFlameTextField.get(),
							 self.minimumChillTextField.get(), self.minimumLightningTextField.get(),
							 self.minimumCycloneTextField.get(), self.minimumSmashTextField.get(),
							 self.minimumExorcismTextField.get(), self.minimumBeastTextField.get(),
							 self.minimumScaleTextField.get(), self.maximumFlameTextField.get(),
							 self.maximumChillTextField.get(), self.maximumLightningTextField.get(),
							 self.maximumCycloneTextField.get(), self.maximumSmashTextField.get(),
							 self.maximumExorcismTextField.get(), self.maximumBeastTextField.get(),
							 self.maximumScaleTextField.get(), self.data23TextField.get(), self.data24TextField.get(),
							 self.data25TextField.get(), self.data26TextField.get(), self.data27TextField.get(),
							 self.data28TextField.get(), self.data29TextField.get(), self.firstBuildUpTextField.get(),
							 self.secondBuildUpTextField.get(), self.thirdBuildUpTextField.get(),
							 self.firstMonsterRequirementTextField.get(), self.secondMonsterRequirementTextField.get(),
							 self.thirdMonsterRequirementTextField.get()]
		return changedWeaponData

	def saveData(self):
		changedWeaponData = self.getDataFromFields()

		if checkWeaponDataTypes(changedWeaponData) == True:
			changedWeapon = WeaponData(changedWeaponData)
			self.AllWeaponData[self.currentListboxIndex] = changedWeapon

			self.WeaponDataFile.writeToFile(self.AllWeaponData)
			self.weaponListbox.delete(0, self.weaponListbox.size())
			self.populateListbox(self.AllWeaponData)
			self.weaponListbox.see(self.currentListboxIndex)

		else:
			self.discardChanges()
			tkinter.messagebox.showinfo("Error saving data", "All fields must be in an integer format")
