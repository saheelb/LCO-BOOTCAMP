import pyHook, pythoncom

def keyPress_EventHandler(event):
    try:
        print ('MessageName:',event.MessageName)
        print ('Message:',event.Message)
        print ('Time:',event.Time)
        print ('Window:',event.Window)
        print ('WindowName:',event.WindowName)
        print ('Ascii:', event.Ascii, chr(event.Ascii))
        print ('Key:', event.Key)
        print ('KeyID:', event.KeyID)
        print ('ScanCode:', event.ScanCode)
        print ('Extended:', event.Extended)
        print ('Injected:', event.Injected)
        print ('Alt', event.Alt)
        print ('Transition', event.Transition)
        print ('---')

        return 1
    except KeyboardInterrupt:
        return 1


hm = pyHook.HookManager()
# watch for all mouse events
hm.KeyDown = keyPress_EventHandler
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
    
