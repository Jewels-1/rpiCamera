from datetime import datetime, date
import time
import RPi.GPIO as GPIO

from picamera2.previews.qt import QGlPicamera2
from picamera2 import Picamera2, Preview


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration())

    
def button_callback(channel):
    print("Taking Picture")
    today = date.today()
    nowT =int(time.time())
    nowT = int(nowT)
    picName = "capture"+str(today.year)+ str(today.month)+str(today.day)+str(nowT)
    timestamp = datetime.now().isoformat
    picam2.capture_file("/home/pi/Pictures/capture"+picName+".jpg")


GPIO.add_event_detect(11,GPIO.RISING, callback=button_callback)

picam2.start_preview(Preview.QTGL, x=100,y=200, width=800, height=600)
picam2.start()

message = input("Press enter to quit")
GPIO.cleanup()
picam2.stop_preview()