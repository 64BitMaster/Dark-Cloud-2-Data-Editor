from FileReader import FileReader, isInteger


class ItemData:
	def __init__(self, itemData):
		self.itemID = int(itemData[0])
		self.itemType = int(itemData[1])
		self.data3 = int(itemData[2])
		self.data4 = int(itemData[3])
		self.maxStackSize = int(itemData[4])
		self.maxItemCount = int(itemData[5])
		self.data7 = int(itemData[6])
		self.spriteIndex = int(itemData[7])
		self.IDAgain = int(itemData[8])
		self.itemModelName = str(itemData[9])
		self.data11 = int(itemData[10])

	def printItemData(self):
		print(str(self.itemID) + ", " + str(self.itemType) + ", " + str(self.data3) + ", " + str(
			self.data4) + ", [" + str(self.maxItemCount) + ", " + str(self.maxStackSize) + "], " + str(
			self.data7) + ", " + str(self.spriteIndex) + ", " + str(self.itemModelName) + ", " + str(self.data11))


class ItemDataFileHandler(FileReader):
	def __init__(self, filepath):
		self.filepath = str(filepath)
		self.filename = '/comdat.cfg'

	def readFromFile(self):
		try:
			file = open((self.filepath + self.filename), 'rb')
			fileLines = file.readlines()
			allItemData = []

			for line in fileLines:
				dataString = str(line)

				itemData = dataString.split(',')
				itemData[0] = itemData[0].lstrip('b\'COM ')
				itemData[9] = itemData[9].strip('"')
				itemData[10] = itemData[10].rstrip(";\\r\\n\'")

				allItemData.append(ItemData(itemData))

			return allItemData

		except(FileNotFoundError):
			print("Unable to read from file, file not found.")

		except(IndexError):
			print("Error, itemData not properly split")

		except:
			print("Error, file not found")

	def writeToFile(self, itemData):
		try:
			file = open((self.filepath + self.filename), 'wb')
			numberOfItems = len(itemData)

			for x in range(numberOfItems):
				line = 'COM ' + str(itemData[x].itemID) + ',' + str(itemData[x].itemType) + ',' + str(
					itemData[x].data3) + ',' + str(itemData[x].data4) + ',' + str(
					itemData[x].maxStackSize) + ',' + str(itemData[x].maxItemCount) + ',' + str(
					itemData[x].data7) + ',' + str(itemData[x].spriteIndex) + ',' + str(
					itemData[x].IDAgain) + ',"' + str(itemData[x].itemModelName) + '",' + str(
					itemData[x].data11) + ';\r\n'
				file.write(line.encode())
		except IOError:
			print('IO Error')

		except Exception as e:
			print(e)


# Locates full item data based on a given itemID
def findItem(itemID, itemData):
	for items in itemData:
		if (items.itemID == itemID):
			return items


# Saves changed item data based on current itemID
def saveItemEdit(newItem, allItems):
	for x in range(len(allItems)):
		if allItems[x].itemID == newItem.itemID:
			allItems[x] = newItem

	return allItems


# Finds all items that are the four types of weapons (used for correctly matching weapon names when reading weapon data)
def getAllWeapons(itemData):
	AllWeapons = []
	for x in range(len(itemData)):
		if itemData[x].itemType == 1 or itemData[x].itemType == 2 or itemData[x].itemType == 3 or itemData[x].itemType == 4:
			AllWeapons.append(itemData[x])
	return AllWeapons


# Check data entered for data type to make sure only numbers are entered
def checkItemDataTypes(ItemData):
	for x in range(11):
		if x != 9:
			if isInteger(ItemData[x]) == False:
				return False
	return True