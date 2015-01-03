from os import path
import time
import cv2
import serial
import random
import settings

PORT = '/dev/ttyUSB0'
RATE = 9600
CAMERA_PORT = 1

i = 0
serial_port = serial.Serial(PORT, RATE)
print 'Initializing video stream...'
time.sleep(5)
capture = cv2.VideoCapture(CAMERA_PORT)
print 'Video parameters:',
print 'width=', capture.set(3, 1600),
print 'height=', capture.set(4, 1200)
while True:
    serial_port.flush()
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    filename = path.join(settings.IMAGES_DIR, 'pic{}.jpg'.format(i))
    print 'saving to: ', filename
    cv2.imwrite(filename, gray)
    i += 1
    serial_port.write('a')
    time.sleep(1)
    if i == 268:
        break
capture.release()
