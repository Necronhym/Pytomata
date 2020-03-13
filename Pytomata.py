import pyautogui
import numpy
import cv2
import pytesseract
import time
class Pytomata:
    #Mouse Commands:
    class Mouse:
        def move(x, y):
            #Input Checking:
            if x > pyautogui.size()[0]:
                x = pyautogui.size()[0]
            if y > pyautogui.size()[1]:
                y = pyautogui.size()[1]
            if x < 0:
                x = 0
            if y < 0:
                y = 0
            #Move mouse
            pyautogui.moveTo(x, y)
        #Press mouse button:
        def buttonDown(b):
            if b in ['left', 'middle', 'right']:
                pyautogui.mouseDown(button=b)
        #Releace mouse button:
        def buttonUp(b):
            if b in ['left', 'middle', 'right']:
                pyautogui.mouseUp(button=b)
    #Keyboard Commands:
    class Keyboard:
        def buttonDown(button):
            if button in ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7','8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~','accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace','browserback', 'browserfavorites', 'browserforward', 'browserhome','browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear','convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete','divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10','f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20','f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9','final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja','kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail','launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack','nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6','num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn','pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn','prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator','shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab','up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen','command', 'option', 'optionleft', 'optionright']:
                pyautogui.keyDown(button)
        def buttonUp(button):
            if button in ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7','8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~','accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace','browserback', 'browserfavorites', 'browserforward', 'browserhome','browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear','convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete','divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10','f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20','f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9','final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja','kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail','launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack','nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6','num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn','pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn','prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator','shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab','up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen','command', 'option', 'optionleft', 'optionright']:
                pyautogui.keyUp(button)
    #Image Commands:
    #DONE
    class Image:
        def screenshot(x=0, y=0, w=pyautogui.size()[0], h=pyautogui.size()[1]):
            #Input checking:
            if x<0:
                x=0
            if y<0:
                y=0
            if x>pyautogui.size()[0]:
                x = pyautogui.size()[0]
            if y>pyautogui.size()[1]:
                y = pyautogui.size()[1]
            if (x+w) > pyautogui.size()[0]:
                w = pyautogui.size()[0]-(x)
            if (y+h) > pyautogui.size()[1]:
                h = pyautogui.size()[1]-(y)
            return cv2.cvtColor(numpy.array(pyautogui.screenshot(region=(x, y, w, h))), cv2.COLOR_RGB2BGR)
        def load(fileLocation):
            return cv2.imread(fileLocation)
        # !Waits for keypress clicking X wont do it;
        def show(image, name="Image"):
            cv2.imshow(name, image)
            cv2.waitKey(0)
            cv2.destroyWindow(name)
        #Crops image has input checking
        def crop(image, x=0,y=0,w=0,h=0):
            if x<0:
                x=0
            if y<0:
                y=0
            if w==0:
                w=image.shape[1]
            if h==0:
                h=image.shape[0]
            if x>image.shape[1]:
                x=image.shape[1]
            if y>image.shape[0]:
                y=image.shape[0]
            if (x+w)>image.shape[1] > image.shape[1]:
                w = image.shape[1] - x
            if (y+h)>image.shape[0] > image.shape[0]:
                g = image.shape[0] - y
            return image[y:y+h, x:x+w]
        def filterOut(image, HL=0, HH=255, SL=0, SH=255, VL=0, VH=255):
            return cv2.bitwise_and(image, image,mask= cv2.inRange( cv2.cvtColor(image, cv2.COLOR_BGR2HSV), numpy.array([HL, SL, VL]), numpy.array([HH, SH, VH])))
        def filterIn(image, HL=0, HH=255, SL=0, SH=255, VL=0, VH=255):
            return cv2.bitwise_and(image, image,mask= cv2.bitwise_not(cv2.inRange( cv2.cvtColor(image, cv2.COLOR_BGR2HSV), numpy.array([HL, SL, VL]), numpy.array([HH, SH, VH]))))
        def createMask(Image):
            return cv2.threshold(Image[:,:,:], 0, 255, cv2.THRESH_BINARY)[1]
        def applyMaskAdd(Image, Templet):
            return cv2.subtract(Image.astype(float),cv2.bitwise_not(Templet), dtype = cv2.CV_8UC1)
        def applyMaskSub(Image, Templet):
            return cv2.subtract(Image.astype(float), Templet, dtype = cv2.CV_8UC1)
        def findTemplate(Image, Template, Threshold = 0.8):
            Image= cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
            Template= cv2.cvtColor(Template, cv2.COLOR_BGR2GRAY)
            tw,th= Template.shape[::1]
            res = cv2.matchTemplate(Image, Template, cv2.TM_CCOEFF_NORMED)
            loc = numpy.where( res >= Threshold )
            return loc[1][-1]+(tw/2),loc[0][-1]+(th/2)
        def findObject(Img):
            try:
                        x, y= cv2.boundingRect(cv2.findContours(cv2.cvtColor(Pytomata.Image.createMask(Img), cv2.COLOR_BGR2GRAY), 1, 2)[0][0])[0]+(cv2.boundingRect(cv2.findContours(cv2.cvtColor(Pytomata.Image.createMask(Img), cv2.COLOR_BGR2GRAY), 1, 2)[0][0])[2]/2), cv2.boundingRect(cv2.findContours(cv2.cvtColor(Pytomata.Image.createMask(Img), cv2.COLOR_BGR2GRAY), 1, 2)[0][0])[1]+(cv2.boundingRect(cv2.findContours(cv2.cvtColor(Pytomata.Image.createMask(Img), cv2.COLOR_BGR2GRAY), 1, 2)[0][0])[3]/2)
            except:
                        x,y = 0, 0
            return x, y
    #Oprical Character Recognition
    #Done
    class OCR:
        def imageToText(Image):
            return pytesseract.image_to_string(Image)

