from ItemNameDataReader import findItemName


def getAllWeaponNames(allWeaponItemData, allItemNames):
	WeaponNames = []
	for x in range(len(allWeaponItemData)):
		WeaponNames.append(findItemName(allWeaponItemData[x].itemID, allItemNames))
	return WeaponNames


def getAllRidepodPartNames(allRidepodPartItemData, allItemNames):
	RidepodPartNames = []
	for x in range(len(allRidepodPartItemData)):
		RidepodPartNames.append(findItemName(allRidepodPartItemData[x].itemID, allItemNames))
	return RidepodPartNames


def setTextField(textFieldWidget, text):
	currentReadState = textFieldWidget['state']

	textFieldWidget.config(state='normal')
	textFieldWidget.delete(0, 'end')
	textFieldWidget.insert(0, str(text))

	if currentReadState == 'readonly':
		textFieldWidget.config(state='readonly')