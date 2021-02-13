from FileReader import FileReader, isInteger


class WeaponData:
	def __init__(self, newWeaponData):
		self.data1 = int(newWeaponData[0])
		self.data2 = int(newWeaponData[1])

		self.minimumAttack = int(newWeaponData[2])
		self.minimumDurable = int(newWeaponData[3])

		self.maximumAttack = int(newWeaponData[4])
		self.maximumDurable = int(newWeaponData[5])

		self.minimumFlame = int(newWeaponData[6])
		self.minimumChill = int(newWeaponData[7])
		self.minimumLightning = int(newWeaponData[8])
		self.minimumCyclone = int(newWeaponData[9])
		self.minimumSmash = int(newWeaponData[10])
		self.minimumExorcism = int(newWeaponData[11])
		self.minimumBeast = int(newWeaponData[12])
		self.minimumScale = int(newWeaponData[13])

		self.maximumFlame = int(newWeaponData[14])
		self.maximumChill = int(newWeaponData[15])
		self.maximumLightning = int(newWeaponData[16])
		self.maximumCyclone = int(newWeaponData[17])
		self.maximumSmash = int(newWeaponData[18])
		self.maximumExorcism = int(newWeaponData[19])
		self.maximumBeast = int(newWeaponData[20])
		self.maximumScale = int(newWeaponData[21])

		self.data23 = int(newWeaponData[22])
		self.data24 = int(newWeaponData[23])
		self.data25 = int(newWeaponData[24])
		self.data26 = int(newWeaponData[25])
		self.data27 = int(newWeaponData[26])
		self.data28 = int(newWeaponData[27])
		self.data29 = int(newWeaponData[28])

		self.firstBuildUp = int(newWeaponData[29])
		self.secondBuildUp = int(newWeaponData[30])
		self.thirdBuildUp = int(newWeaponData[31])

		self.firstMonsterRequirement = int(newWeaponData[32])
		self.secondMonsterRequirement = int(newWeaponData[33])
		self.thirdMonsterRequirement = int(newWeaponData[34])

	def getLine1(self):
		return str(self.data1) + ',' + str(self.data2)

	def getMinimumBasicStats(self):
		return str(self.minimumAttack) + ',' + str(self.minimumDurable)

	def getMaximumBasicStats(self):
		return str(self.maximumAttack) + ',' + str(self.maximumDurable)

	def getMinimumElementalStats(self):
		return str(self.minimumFlame) + ',' + str(self.minimumChill) + ',' + str(self.minimumLightning) + ',' + str(
			self.minimumCyclone) + ', ' + str(self.minimumSmash) + ' ,' + str(self.minimumExorcism) + ',' + str(
			self.minimumBeast) + ',' + str(self.minimumScale)

	def getMaximumElementalStats(self):
		return str(self.maximumFlame) + ',' + str(self.maximumChill) + ',' + str(self.maximumLightning) + ',' + str(
			self.maximumCyclone) + ',' + str(self.maximumSmash) + ',' + str(self.maximumExorcism) + ',' + str(
			self.maximumBeast) + ',' + str(self.maximumScale)

	def getUnknownData(self):
		return str(self.data23) + ',' + str(self.data24) + ',' + str(self.data25) + ',' + str(self.data26) + ',' + str(
			self.data27) + ',' + str(self.data28) + ',' + str(self.data29)

	def getBuildUpData(self):
		return str(self.firstBuildUp) + ',' + str(self.secondBuildUp) + ',' + str(self.thirdBuildUp) + ',' + str(
			self.firstMonsterRequirement) + ',' + str(self.secondMonsterRequirement) + ',' + str(
			self.thirdMonsterRequirement)


class WeaponDataFileHandler(FileReader):
	def __init__(self, filepath):
		self.filepath = str(filepath)
		self.filename = '/wepdat.cfg'

	def readFromFile(self):
		try:
			file = open((self.filepath + self.filename), 'rb')
			allWeaponData = []

			firstLine = str(file.readline())

			firstLine = firstLine.strip('b\'WEPNUM ')
			firstLine = firstLine.rstrip(";\\r\\n\'")
			totalWeapons = int(firstLine)

			for i in range(totalWeapons):
				currentWeaponData = []

				dataLine1 = str(file.readline())
				dataLine1 = dataLine1.strip('b\'WEP ')
				dataLine1 = dataLine1.rstrip(";\\r\\n\'")
				unknownData1 = dataLine1.split(',')
				currentWeaponData.append(unknownData1[0])
				currentWeaponData.append(unknownData1[1])

				dataLine2 = str(file.readline())
				dataLine2 = dataLine2.strip('b\'WEP_ST ')
				dataLine2 = dataLine2.rstrip(";\\r\\n\'")
				weaponMinimumBasicStats = dataLine2.split(',')
				currentWeaponData.append(weaponMinimumBasicStats[0])
				currentWeaponData.append(weaponMinimumBasicStats[1])

				dataLine3 = str(file.readline())
				dataLine3 = dataLine3.strip('b\'WEP_ST_L ')
				dataLine3 = dataLine3.rstrip(";\\r\\n\'")
				weaponMaximumBasicStats = dataLine3.split(',')
				currentWeaponData.append(weaponMaximumBasicStats[0])
				currentWeaponData.append(weaponMaximumBasicStats[1])

				dataLine4 = str(file.readline())
				dataLine4 = dataLine4.replace('b\'WEP_ST2 ', '')
				dataLine4 = dataLine4.rstrip(";\\r\\n\'")
				weaponMinimumElementalStats = dataLine4.split(',')
				currentWeaponData.append(weaponMinimumElementalStats[0])
				currentWeaponData.append(weaponMinimumElementalStats[1])
				currentWeaponData.append(weaponMinimumElementalStats[2])
				currentWeaponData.append(weaponMinimumElementalStats[3])
				currentWeaponData.append(weaponMinimumElementalStats[4].strip(' '))
				currentWeaponData.append(weaponMinimumElementalStats[5])
				currentWeaponData.append(weaponMinimumElementalStats[6])
				currentWeaponData.append(weaponMinimumElementalStats[7])

				dataLine5 = str(file.readline())
				dataLine5 = dataLine5[12:]
				dataLine5 = dataLine5.rstrip(";\\r\\n\'")

				weaponMaximumElementalStats = dataLine5.split(',')
				currentWeaponData.append(weaponMaximumElementalStats[0])
				currentWeaponData.append(weaponMaximumElementalStats[1])
				currentWeaponData.append(weaponMaximumElementalStats[2])
				currentWeaponData.append(weaponMaximumElementalStats[3])
				currentWeaponData.append(weaponMaximumElementalStats[4])
				currentWeaponData.append(weaponMaximumElementalStats[5])
				currentWeaponData.append(weaponMaximumElementalStats[6])
				currentWeaponData.append(weaponMaximumElementalStats[7])

				dataLine6 = str(file.readline())
				dataLine6 = dataLine6.strip('b\'WEP_SPE ')
				dataLine6 = dataLine6.rstrip(";\\r\\n\'")
				weaponUnknownData = dataLine6.split(',')
				currentWeaponData.append(weaponUnknownData[0])
				currentWeaponData.append(weaponUnknownData[1])
				currentWeaponData.append(weaponUnknownData[2])
				currentWeaponData.append(weaponUnknownData[3])
				currentWeaponData.append(weaponUnknownData[4])
				currentWeaponData.append(weaponUnknownData[5])
				currentWeaponData.append(weaponUnknownData[6])

				dataLine7 = str(file.readline())
				dataLine7 = dataLine7.strip('b\'WEP_BUILD ')
				dataLine7 = dataLine7.rstrip(";\\r\\n\'")
				weaponBuildUpData = dataLine7.split(',')
				currentWeaponData.append(weaponBuildUpData[0])
				currentWeaponData.append(weaponBuildUpData[1])
				currentWeaponData.append(weaponBuildUpData[2])
				currentWeaponData.append(weaponBuildUpData[3])
				currentWeaponData.append(weaponBuildUpData[4])
				currentWeaponData.append(weaponBuildUpData[5])

				allWeaponData.append(WeaponData(currentWeaponData))

			return allWeaponData

		except(FileNotFoundError):
			print("Unable to read from file, file not found.")

		except(IndexError):
			print("Error, itemData not properly split")

		except:
			print("Error, file not found")

	def writeToFile(self, newWeaponData):

		try:
			file = open((self.filepath + self.filename), 'wb')
			numberOfWeapons = len(newWeaponData)
			# print(numberOfWeapons)

			binarySuffix = ';\r\n'

			initialLine = 'WEPNUM ' + str(numberOfWeapons) + binarySuffix
			file.write(initialLine.encode())

			for x in range(len(newWeaponData)):
				firstLine = 'WEP ' + newWeaponData[x].getLine1() + binarySuffix
				file.write(firstLine.encode())

				minimumBasicStats = 'WEP_ST ' + newWeaponData[x].getMinimumBasicStats() + binarySuffix
				file.write(minimumBasicStats.encode())

				maximumBasicStats = 'WEP_ST_L ' + newWeaponData[x].getMaximumBasicStats() + binarySuffix
				file.write(maximumBasicStats.encode())

				minimumElementalStats = 'WEP_ST2 ' + newWeaponData[x].getMinimumElementalStats() + binarySuffix
				file.write(minimumElementalStats.encode())

				maximumElementalStats = 'WEP_ST2_L ' + newWeaponData[x].getMaximumElementalStats() + binarySuffix
				file.write(maximumElementalStats.encode())

				unknownStats = 'WEP_SPE ' + newWeaponData[x].getUnknownData() + binarySuffix
				file.write(unknownStats.encode())

				buildUpData = 'WEP_BUILD ' + newWeaponData[x].getBuildUpData() + binarySuffix
				file.write(buildUpData.encode())

		except(FileNotFoundError):
			print("Unable to read from file, file not found.")

		except(IndexError):
			print("Error, itemInfo not properly split")

		except:
			print("Error, unable to save to file.")


def checkWeaponDataTypes(AllWeaponData):
	for x in range(len(AllWeaponData)):
		if isInteger(AllWeaponData[x]) == False:
			return False
	return True
