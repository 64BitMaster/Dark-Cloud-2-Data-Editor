from FileReader import FileReader


class ridepodBodyData:
	def __init__(self, itemData):
		self.itemID = int(itemData[0])
		self.partType = int(itemData[1])
		self.capacity = int(itemData[2])
		self.data4 = int(itemData[3])
		self.defense = int(itemData[4])
		self.modelName = str(itemData[5])

	def returnBodyData(self):
		return str(self.itemID) + ',' + str(self.partType) + ',' + str(self.capacity) + ',' + str(self.data4) + ',' + str(self.defense) + ',"' + str(self.modelName) + '"'


class ridepodWeaponData:
	def __init__(self, itemData):
		self.itemID = int(itemData[0])
		self.partType = int(itemData[1])
		self.capacity = int(itemData[2])
		self.data4 = int(itemData[3])
		self.hitPoints = int(itemData[4])
		self.attack = int(itemData[5])
		self.durable = int(itemData[6])
		self.flame = int(itemData[7])
		self.chill = int(itemData[8])
		self.lightning = int(itemData[9])
		self.cyclone = int(itemData[10])
		self.smash = int(itemData[11])
		self.exorcism = int(itemData[12])
		self.beast = int(itemData[13])
		self.scale = int(itemData[14])
		self.data14 = int(itemData[15])
		self.modelName = str(itemData[16])

	def returnWeaponData(self):
		return str(self.itemID) + ',' + str(self.partType) + ',' + str(self.capacity) + ',' + str(self.data4) + ',' + str(self.hitPoints) + ',' + str(self.attack) + ',' + str(self.durable) + ',' + str(self.flame) + ',' + str(self.chill) + ',' + str(self.lightning) + ',' + str(self.cyclone) + ',' + str(self.smash) + ',' + str(self.exorcism) + ',' + str(self.beast) + ',' + str(self.scale) + ',' + str(self.data14) + ',"' + str(self.modelName) + '"'


class ridepodLegData:
	def __init__(self, itemData):
		self.itemID = int(itemData[0])
		self.partType = int(itemData[1])
		self.capacity = int(itemData[2])
		self.data4 = int(itemData[3])
		self.data5 = int(itemData[4])
		self.data6 = int(itemData[5])

	def returnLegData(self):
		return str(self.itemID) + ',' + str(self.partType) + ',' + str(self.capacity) + ',' + str(self.data4) + ',' + str(self.data5) + ',' + str(self.data6)


class ridepodEnergyPackData:
	def __init__(self, itemData):
		self.itemID = int(itemData[0])
		self.partType = int(itemData[1])
		self.capacity = int(itemData[2])
		self.data4 = int(itemData[3])
		self.maxFuel = int(itemData[4])

	def returnEnergyPackData(self):
		return str(self.itemID) + ',' + str(self.partType) + ',' + str(self.capacity) + ',' + str(self.data4) + ',' + str(self.maxFuel)


def sortRidepodParts(ridepodData):
	ridepodData.sort(key=lambda x: x.partType)
	return ridepodData


class RidepodDataFileHandler(FileReader):
	def __init__(self, filepath):
		self.filepath = str(filepath)
		self.filename = '/robodat.cfg'

	def readFromFile(self):
		try:
			file = open(self.filepath + self.filename, 'rb')
			fileLines = file.readlines()
			allRidepodData = []

			for line in fileLines:
				rawData = str(line)

				if (rawData.startswith('b\'ROBOINIT') == False):
					itemData = rawData.split(',')
					itemData[0] = itemData[0].lstrip('b\'RB_PARTS ')
					itemData[len(itemData) - 1] = itemData[len(itemData) - 1].rstrip(";\\r\\n\'")

					# Check if item is a body part
					if (int(itemData[1]) == 0):
						itemData[len(itemData) - 1] = itemData[len(itemData) - 1].strip('"')
						bodyData = ridepodBodyData(itemData)
						allRidepodData.append(bodyData)

					# Check if item is a weapon part
					if (int(itemData[1]) == 1):
						itemData[len(itemData) - 1] = itemData[len(itemData) - 1].strip('"')
						weaponData = ridepodWeaponData(itemData)
						allRidepodData.append(weaponData)

					# Check if item is a leg part
					if (int(itemData[1]) == 2):
						legData = ridepodLegData(itemData)
						allRidepodData.append(legData)

					# Check if item is an energy pack part
					if(int(itemData[1]) == 3):
						energyPackData = ridepodEnergyPackData(itemData)
						allRidepodData.append(energyPackData)

			return allRidepodData

		except(FileNotFoundError):
			print("Unable to read from file, file not found.")

		except(IndexError):
			print("Error, itemData not properly split")

		except:
			print("Error, file not found")

	def writeToFile(self, ridepodData):
		try:
			file = open((self.filepath + self.filename), 'wb')
			numberOfParts = len(ridepodData)

			binarySuffix = ';\r\n'

			initialLine = 'ROBOINIT ' + str(numberOfParts) + binarySuffix
			file.write(initialLine.encode())

			for x in range(numberOfParts):
				if ridepodData[x].partType == 0:
					# Item is a body part
					nextLine = 'RB_PARTS ' + ridepodData[x].returnBodyData() + binarySuffix

				elif ridepodData[x].partType == 1:
					# Item is a weapon part
					nextLine = 'RB_PARTS ' + ridepodData[x].returnWeaponData() + binarySuffix

				elif ridepodData[x].partType == 2:
					# Item is a leg part
					nextLine = 'RB_PARTS ' + ridepodData[x].returnLegData() + binarySuffix

				else:
					# Item is an energy pack part
					nextLine = 'RB_PARTS ' + ridepodData[x].returnEnergyPackData() + binarySuffix

				file.write(nextLine.encode())


		except(FileNotFoundError):
			print("Unable to read from file, file not found.")

		except(IndexError):
			print("Error, itemInfo not properly split")

		except:
			print("Error, unable to save to file.")

