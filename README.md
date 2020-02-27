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

##### Move Mouse To X, Y coordiantes:
```
Pytomata.Mouse.move(x, y)
```
##### Press down mouse button at current mouse location:
```
Pytomata.Mouse.buttonDown(button)
```
##### Release mouse button at current mouse location:
```
Pytomata.Mouse.buttonUp(button)
```
##### Button variable value can be:
```
'left', 'middle' or 'right'
```

### Keyboard Functions:

##### Press down keyboard key button
```
Pytomata.Keyboard.buttonDown(button)
```
##### Release mouse keyboard key button:
```
Pytomata.Keyboard.buttonUp(button)
```
##### Button variable value can be:
```
'\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft'or 'optionright'
```

### Image Functions: 

#### Load an image from a pilepath and return it:
```
Pythomata.Image.load(filepath)
```
Returns the loaded images

##### Take a screenshot of an area on the screen:
```
Pythomata.Image.screenshot(x,y,w,h)
```
X, Y define top left coordinates, w, h are width and height respectively
Returns a images

##### Crop an image:
```
Pythomata.Image.crop(Image, x, y, w, h)
```
X,Y define the top left coordinates, w, h are width and height respectivley
Returns a cropped image

##### Shows and image in a window:
```
Pythomata.Image.show(Image)
```
**The window waits for a keyboard interups. Clicking x to close it will lock the script in a loop. So use the keyboard to close it.

#### Filtering:

Filtering is used to remove colors form an image.
It has two methods, in fitering removing all the colors inside a threshold
and out filtering, removing all the colors outside the filter thresold

##### Filter image and remove all pixels outside of HSV paramaters:
```
Pytomata.Image.filterOut(Image, HL, HH, SL, SH, VL, VH)
```
Where HL and HH represent hue low cutoff point and hue hight cutoff point
SL and SH represent saturation low and hight cutoff points
VL and VH represent value low and high cutoff points
All values go from 0 to 255
Returns a filtered image

##### Filter image and remove all pixels within HSV paramaters:
Pytomata.Image.filterIn(Image, HL, HH, SL, SH, VL, VH)
```
Pytomata.Image.filterIn(Image, HL, HH, SL, SH, VL, VH)
```
Where HL and HH represent hue low cutoff point and hue hight cutoff point
SL and SH represent saturation low and hight cutoff points
VL and VH represent value low and high cutoff points
All values go from 0 to 255
Returns a filtered image

#### Masking:

Masking is used to remove parts of an image using a bit mask

##### Create Alpha Bit mask:
```
Pytomata.Image.createMask(Image)
```
All values that are not 0 will be assumed as alpha 1
Returns a mask images

##### Apply Mask additive
```
Pytomata.Image.applyMaskAdd(Image, Maks)
```
Removes all values outisde of the masked area
Returns an image with the mask applied

##### Apply Mask subtractive
```
Pytomata.Image.applyMaskSub(Image, Maks)
```
Removes all values inside the mask
Returns an image with the mask applied

#### Locating:

Location functions are used to locate templets or objcet coordinates on screen.

###### Locate a tempet image inside a larger image:
```
Pytomata.Image.findTemplate(Image, Template, threshold = 0.8):
```
Templet is the image you are trying to find inside the larger Image
threshold is the threshold for being considered as a match
Returns X, Y coordinates of the matched center

###### Finde the center of an object in an image:
```
Pytomata.Image.findObject(Image):
```
Returns X, Y coordinates of the objects center
### OCR:
Process image to return a string:
```
Pytomata.OCR.imageToText(Image)
```
## Authors:

* **Necronhym (N3cr0)** - *Initial work* -


