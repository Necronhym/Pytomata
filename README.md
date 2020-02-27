# Pytomata

Pythomata is a cross-platform scripting autoamtion platfrom.
It uses for scripting OpenCV for image processing, object detection and filtering, tesseract-ocr for optical character recogrnition, and pyautogui for keyboard and mouse command simulation

## Getting Started:

Simply download the repository, unzip it and use the pythomata.py file

Using git:
```
git clone https://github.com/Necronhym/Pytomata.git
```

### Prerequisites:

Pythomata requiers:

Python3 v3.7.3
pytesseract v0.1.3
OpenCV v4.1.2.30
PyAutoGUI v0.9.48

You can use the following command to check the versions installed on your machine with freeze:

```
pip freeze
```
If some of the version do not meet requierments you can use the following commands to install the dependancies:

On Windows:
```
pip install opencv-python

pip install tesseract

pip install pyautogui 
```

On GNU/Linux and macOS
```
pip3 install opencv-python

pip3 install tesseract

pip3 install pyautogui 
```

## Usage:

Pytomata hosts a diverse tool set of functions designed for responsive automation.
All of these functions are housed in a simple to use python class devided in to sub classes.
Currently supported functions, and examples on how to use them include:

### Mouse Functions: 

Move Mouse To X, Y coordiantes:
```
Pytomata.Mouse.move(x, y)
```
Press down mouse button at current mouse location:
```
Pytomata.Mouse.buttonDown(button)
```
Release mouse button at current mouse location:
```
Pytomata.Mouse.buttonUp(button)
```
Button variable must be:
```
'left', 'middle' or 'right'
```

### Keyboard Functions:
Press down keyboard key button
```
Pytomata.Keyboard.buttonDown(button)
```
Release mouse keyboard key button:
```
Pytomata.Keyboard.buttonUp(button)
```
Button variable values must be:
```
'\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7','8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~','accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace','browserback', 'browserfavorites', 'browserforward', 'browserhome','browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear','convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete','divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10','f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20','f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9','final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja','kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail','launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack','nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6','num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn','pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn','prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator','shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab','up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen','command', 'option', 'optionleft' or 'optionright'
```

### Image Functions:

### OCR:
Process image to return a string:
```
Pytomata.OCR(Image)
```
## Authors:

* **Necronhym (N3cr0)** - *Initial work* -


