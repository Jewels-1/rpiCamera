from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QWidget

import RPi.GPIO as GPIO

from picamera2.previews.qt import QGlPicamera2
from picamera2 import Picamera2

GPIO.setwarnings(FALSE)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration())

def on_button_clicked():
    button.setEnabled(False)
    cfg = picam2.create_still_configuration()
    picam2.switch_mode_and_capture_file(cfg, "test1.jpg", signal_function=qpicamera2.signal_done)
    
def capture_done(job):
    result = picam2.wait(job)
    button.setEnabled(True)
    
def button_callback(channel):
    print("Taking Picture")
    
GPIO.add_event_detect(10,GPIO.RISING, callback=button_callback)

app =  QApplication([])
qpicamera2 = QGlPicamera2(picam2, width=800, height=600, keep_ar=False)
button = QPushButton("Click To capture JPEG")
window = QWidget()
qpicamera2.done_signal.connect(capture_done)
button.clicked.connect(on_button_clicked)
    
layout_v = QVBoxLayout()
layout_v.addWidget(qpicamera2)
layout_v.addWidget(button)
window.setWindowTitle("QT Picamera2 App")
window.resize(640, 480)
window.setLayout(layout_v)
    
picam2.start()
window.show()
app.exec()
    