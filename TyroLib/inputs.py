import pyautogui, keyboard


class Input:
    def __init__(self):
        self.Mouse = Mouse()
        self.Keyboard = Keyboard()
class Mouse:
    def __init__(self):
        pass
    
    def position(self):
        return pyautogui.position()
    
    def isDown(self, button='left'):
        return pyautogui.is_pressed(button)
    
    def goTo(self, x, y):
        pyautogui.moveTo(x, y)
        
    def click(self, x=pyautogui.position()[0], y=pyautogui.position()[1], button='left'):
        pyautogui.click(x, y, button)
        
class Keyboard:
    def __init__(self):
        pass
    
    def isKey(self, key):
        return keyboard.is_pressed(key)
    
    def currentKey(self):
        return keyboard.read_key()
    
    def hold(self, key):
        keyboard.press(key)
    
    def release(self, key):
        keyboard.release(key)
    
    def press(self, key):
        keyboard.send(key)
        
Input = Input()