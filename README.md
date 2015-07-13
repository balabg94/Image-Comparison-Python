# Image-Comparison-Python

This is the result of the first task for the selection process of the startup-box.

This python program let's the user compare two images once the user provides the respective image URL's in the spaces provided.
When run, the program opens a dialogue box enabling the users to interact easily. 
When clicked on the Compare button, a bit of time is taken for image fetching and comparison. Once the comparison is done, the result and the images compared are shown in a new dialogue box. Also the comparison is ranked on a scale of 0 to 100 (100 being perfect match). 

The time taken for comparison is a few seconds. The rest of the delay and the 'Not Responding' is not due to the program but due to the internet connection speed, which is crucial as the images are fetched from the internet.

In order to run the program you will need a Python IDE and few modules such as PIL, win32console, win32gui, urllib, cStringIO, izip, Tkinter, tkMessageBox.

The images are fetched then resized before comaprison, different resolution images are producing very different values.
