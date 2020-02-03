from PIL import ImageGrab

ss = ImageGrab.grab(bbox=None)
ss.save("screen.jpg")

