from FileReader import FileReader

class ItemName:
	def __init__(self, prefix, itemNumber, itemName):
		self.prefix = str(prefix)
		self.itemNumber = int(itemNumber)
		self.itemName = str(itemName)

	def printItemName(self):
		print(str(self.itemNumber) + ": " + self.itemName)


class ItemNameFileHandler(FileReader):
	def __init__(self, filepath):
		self.filepath = str(filepath)
		self.filename = '/comdatmes1.cfg'

	def readFromFile(self):
		try:
			# Try to open file and read all lines into fileLines, then create an empty array to hold the ItemNames
			# objects
			file = open(self.filepath + self.filename, 'rb')
			fileLines = file.readlines()
			itemNames = []

			# For each line read, strip extra characters and divide data into item number and item name,
			for line in fileLines:
				rawInfo = str(line).rstrip(';\\r\\n\'')
				itemInfo = rawInfo.split(",")
				itemInfo[1] = str(itemInfo[1])[1:-1]
				itemInfo[1] = itemInfo[1].replace('\\', '')

				# If item is in the special category, remove the different text and adjust the prefix
				if itemInfo[0].startswith('b\'MES_SYSSPE '):
					itemInfo[0] = itemInfo[0].strip('b\'MES_SYSSPE ')
					itemNames.append(ItemName('MES_SYSSPE', int(itemInfo[0]), str(itemInfo[1])))
				else:
					itemInfo[0] = itemInfo[0].strip('b\'MES_SYS ')
					itemNames.append(ItemName('MES_SYS', int(itemInfo[0]), str(itemInfo[1])))

			return itemNames

		except(FileNotFoundError):
			print("Unable to read from file, file not found.")

		except(IndexError):
			print("Error, itemInfo not properly split")

		except:
			print("Unknown error.")

	def writeToFile(self, itemNames):
		try:
			file = open((self.filepath + self.filename), 'wb')
			numberOfItems = len(itemNames)

			for x in range(numberOfItems):
				if itemNames[x].itemName != '(null)':
					if itemNames[x].prefix == 'MES_SYS':
						line = 'MES_SYS ' + str(itemNames[x].itemNumber) + ',"' + itemNames[x].itemName + '";\r\n'
					else:
						line = 'MES_SYSSPE ' + str(itemNames[x].itemNumber) + ',"' + itemNames[x].itemName + '";\r\n'

					file.write(line.encode())
		except IOError:
			print('IO Error')

		except Exception as e:
			print(e)


def saveItemName(newName, allNames, itemID):
	for x in range(len(allNames)):
		if allNames[x].itemNumber == itemID:
			allNames[x].itemName = newName
	return allNames


def findItemName(itemID, itemNames):
	for items in itemNames:
		if (items.itemNumber == itemID) and items.prefix != 'MES_SYSSPE':
			return items.itemName


def sortItemNames(itemNames):
	itemNames.sort(key=lambda x: x.itemNumber)
	return itemNames
