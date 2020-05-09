import os
import datetime


def isInteger(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def checkDataTypes(ItemData):

    if isInteger(ItemData[0]) and isInteger(ItemData[1]) and isInteger(ItemData[2]) and isInteger(ItemData[3]) and isInteger(ItemData[4]) and isInteger(ItemData[5]) and isInteger(ItemData[6]) and isInteger(ItemData[7]) and isInteger(ItemData[8]) and isInteger(ItemData[10]):
        return True
    else:
        return False


def checkIfFilesExist(itemdat, itemdatmes1):
    if os.path.exists(itemdat) and os.path.exists(itemdatmes1):
        return True
    else:
        return False

def checkBackupFolder(selectedDirectory):
    backupFolder = selectedDirectory + '/Backup'
    if os.path.exists(backupFolder) == False:
        createBackupFolder(backupFolder)


def createBackupFolder(backupFolderLocation):
    try:
        os.mkdir(backupFolderLocation)
    except:
        print('Error while creating backup folder :(')


def saveFiles(selectedDirectory, ItemNames, ItemData, backup):
    if backup == True:
        selectedDirectory = selectedDirectory + '/Backup/' + datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        saveItemDataToFile(ItemData, selectedDirectory + '_comdat.cfg')
        saveItemNamesToFile(ItemNames, selectedDirectory + '_comdatmes1.cfg')
    else:
        saveItemDataToFile(ItemData, selectedDirectory + '/comdat.cfg')
        saveItemNamesToFile(ItemNames, selectedDirectory + '/comdatmes1.cfg')


class ItemName:
    def __init__(self, prefix, itemNumber, itemName):
        self.prefix = str(prefix)
        self.itemNumber = int(itemNumber)
        self.itemName = str(itemName)

    def printItemName(self):
        print(str(self.itemNumber) + ": " + self.itemName)


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



class ItemDataFileHandler:
    def __init__(self, filename):
        self.filename = str(filename)

    def readFromFile(self):
        try:
            file = open(self.filename, 'rb')
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


def saveItemDataToFile(itemData, targetFile):
    try:
        file = open(targetFile, 'wb')
        numberOfItems = len(itemData)

        for x in range(numberOfItems):
            line = 'COM ' + str(itemData[x].itemID) + ',' + str(itemData[x].itemType) + ',' + str(
                itemData[x].data3) + ',' + str(itemData[x].data4) + ',' + str(
                itemData[x].maxStackSize) + ',' + str(itemData[x].maxItemCount) + ',' + str(
                itemData[x].data7) + ',' + str(itemData[x].spriteIndex) + ',' + str(
                itemData[x].IDAgain) + ',"' + str(itemData[x].itemModelName) + '",' + str(
                itemData[x].data11) + ';\r\n'
            file.write(line.encode())

    except:
        print("Error, unable to save item data to file.")


# Will return a list of all file names and will insert buffers when necessary.
class ItemNameFileHandler:
    def __init__(self, filename):
        self.filename = str(filename)

    def readFromFile(self):
        try:
            # Try to open file and read all lines into fileLines, then create an empty array to hold the ItemNames
            # objects
            file = open(self.filename, 'rb')
            fileLines = file.readlines()
            itemNames = []

            # For each line read, strip extra characters and divide data into item number and item name,
            # adding buffers for missing item numbers, then return the list of objects created
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


# Will save a list of ItemName objects to a target filename
def saveItemNamesToFile(itemNames, targetFile):
    try:
        file = open(targetFile, 'wb')
        numberOfItems = len(itemNames)

        for x in range(numberOfItems):
            if itemNames[x].itemName != '(null)':
                if itemNames[x].prefix == 'MES_SYS':
                    line = 'MES_SYS ' + str(itemNames[x].itemNumber) + ',"' + itemNames[x].itemName + '";\r\n'
                else:
                    line = 'MES_SYSSPE ' + str(itemNames[x].itemNumber) + ',"' + itemNames[x].itemName + '";\r\n'

                file.write(line.encode())

    except:
        print("Error, unable to save to file.")


def sortItemNames(itemNames):
    itemNames.sort(key=lambda x: x.itemNumber)
    return itemNames


def findItemName(itemID, itemNames):
    for items in itemNames:
        if (items.itemNumber == itemID) and items.prefix != 'MES_SYSSPE':
            return items.itemName

def findItem(itemID, itemData):
    for items in itemData:
        if (items.itemID == itemID):
            return items

def saveItemEdit(newItem, allItems):
    for x in range(len(allItems)):
        if allItems[x].itemID == newItem.itemID:
            allItems[x] = newItem

    return allItems

def saveItemName(newName, allNames, itemID):
    for x in range(len(allNames)):
        if allNames[x].itemNumber == itemID:
            allNames[x].itemName = newName

    return allNames
