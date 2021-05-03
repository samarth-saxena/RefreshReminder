# Refresh Reminder 

Website: https://sites.google.com/iiitd.ac.in/des205-t3-paradigmshifters/home

Video: https://youtu.be/f98Y7ksq3Kg

## Your digital health monitor 

Refresh Reminder helps users improve not only their physical health but in turn their work productivity by giving them a soft nudge in the form of reminding the user to take timely breaks and notifying them about possible lapses in eye blinking and facial distance. It also suggests the optimal exercises via our AR model. The application can be accessed by motion gestures thus keeping the user away from their digital devices. 

## Features

1. Screen to face distance tracker
2. Blink detection
3. Exercise suggestions
4. Sedentary Time Usage
5. Motion gesture controls

## App Screenshots

Homescreen:

![Alt text](screenshots/ss.png?raw=true "Title")

Settings page:

![Alt text](screenshots/ss2.png?raw=true "Title")

System tray icon:

![Alt text](screenshots/ss3.png?raw=true "Title")

Break reminder popup (translucent):

![Alt text](screenshots/ss4.png?raw=true "Title")

Face-screen distance popup (non-intrusive border style):

![Alt text](screenshots/ss5.png?raw=true "Title")

Blink reminder popup (non-intrusive border style):

![Alt text](screenshots/ss6.png?raw=true "Title")

## System Requirements
- OS: Windows 10 only
- Webcam (either inbuilt or external)

If compiling the source code (method #2 of installation):
- Python 3.9 or higher
	- PyQt5 toolkit
	- win10toast library
	- NumPy
- OpenCV
	- imageio
	- Haar Cascade
	- Dlib

## Installation instructions

### 1. Running the executable
1. Download the .rar from https://drive.google.com/drive/folders/185sIaasrRyNZXbI5dC9ZrfqBN2XG7ua8?usp=sharing
2. Extract it at the desired location
3. Run "source/gui.exe"

--- or ---
### 2. Cloning the repository
1. Clone the repository
2. Navigate to /src
3. Compile and run "gui.py"
