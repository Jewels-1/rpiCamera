from datetime import datetime, date
import time
import RPi.GPIO as GPIO

from picamera2.previews.qt import QGlPicamera2
from picamera2 import Picamera2, Preview

#class Picamera2.PiRenderer(parent,layer=0,alpha=255,fullscreen=True,window=None,crop=None,rotation=0,vflip=False,hflip=False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

picam2 = Picamera2()
configPreview  = picam2.create_preview_configuration()
configStill = picam2.create_still_configuration()
picam2.configure(configPreview)

    
def button_callback(channel):
    print("Taking Picture")
    timestamp = time.strftime("%Y%m%d%H%M%S")
    picName = "capture"+timestamp
    picam2.switch_mode(configStill)
    picam2.capture_file("/home/pi/Pictures/capture"+picName+".jpg")
    picam2.switch_mode(configPreview)
#    picam2.configure(configPreview)


GPIO.add_event_detect(11,GPIO.RISING, callback=button_callback)

picam2.start_preview(Preview.QTGL, x=0,y=65, width=640, height=415)
picam2.start()

message = input("Press enter to quit")
GPIO.cleanup()
picam2.stop_preview()