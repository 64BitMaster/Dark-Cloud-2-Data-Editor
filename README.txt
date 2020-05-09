Created by Marc Sustaita, but none of this would be possible without the fantastic videos by Gallum on YouTube!

######################################################################


Hi, thanks for checking this little tool out! To run this, it SHOULD just as easy as unzipping your respective OS and opening the executable inside.

It'll ask you to select the folder you have the 'comdat.cfg' and 'comdatmes1.cfg' files located, and once you select them it'll create a Backup folder in that directory to put copies of each file every time you save, just incase you need to revert back.

There's more than likely a few bugs still in here as this is definitely still a work in progress! If you see any weird quirks or flat-out wrong behavior, just let me know and I'll take a look at it!


If you have suggestions on future features, or comments on how the code is laid out or the GUI is assembled, please let me know! This was my first time working on a GUI, so I'd like to improve in the future!

Also, if you'd like to build this app yourself, all you need to do is run 'DC2ItemEditor.py' in a Python environment with the other two files 'DC2ItemGUI.py' and 'ItemDataReader.py' in the same folder and it should compile normally!



######################################################################

Version 1.2: 

- Fixed a bug that caused the backup files to fail to save on Windows (forgot to check which characters were illegal in Windows file names, whoops)

- Added better handlers for open files, now it will let you know if it can't find the files at the given directory and prompt you to try again

- Program now checks to make sure text fields are only integers for the respective fields that require that

######################################################################


TO-DO:

- I think when the app loads, if you try interacting with the editing menu before you select an item, it throws an error, but still continues running, so I need to eventually catch it

- I'd like to change the way the Save and Discard Changes buttons work so that you can only interact with them after you've made changes to be saved or discarded

- Maybe allow you to select the sprite sheet, and display the sprite of the item alongside the rest of the variables?

- Add more information on what the variables do, perhaps with tooltips when the user hovers over each field?

- Implement a '+' button to add a new item to the game! This would allow you to add items back in (at least to the debug menu), ESPECIALLY if they still have their name in the game, such as the Macho Sword!

- Add all weapon stats, ridepod part stats, and more!
	
