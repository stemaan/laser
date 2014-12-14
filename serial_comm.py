import time
import cv2
import serial
import random

PORT = '/dev/ttyUSB0'
RATE = 9600
CAMERA_PORT = 1

i = 0
serial_port = serial.Serial(PORT, RATE)
print 'initializing...'
time.sleep(5)
capture = cv2.VideoCapture(CAMERA_PORT)
print 'w', capture.set(3, 1600)
print 'h', capture.set(4, 1200)
while True:
    serial_port.flush()
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    print 'saving to file: pic{}.jpg'.format(i)
    cv2.imwrite('/home/steman/Dev/inz/images/raw/pic{}.jpg'.format(i), gray)
    i += 1
    serial_port.write('a')
    time.sleep(1)
#    a = serial_port.read()
#    if a:
##        print 'received: ', a
#        print 'step', i
    if i == 209:
        break
capture.release()
