from math import sin, cos, radians
from os import path, listdir
import cv2
import cv2.cv as cv
import numpy as np
import settings

STEPPER_MOTOR_ANGLE = radians(1.8)
LASER_ANGLE = radians(30)
b = lambda i, w: (i + 1 - w/2) / 5.0
to_milimeter = lambda row: row / 5.0

def find_brightest(img, step):
    height, width = img.shape
    pixels = []
    for row in xrange(height):
        brightest = 0
        x_brigtest = y_brightest = 0  
        for col in xrange(width):
            if brightest < img[row, col]:
                brightest = img[row, col]
                x_brigtest = col
                y_brightest = row
        l = b(x_brigtest, width) 
        r = l / sin(LASER_ANGLE)
        x = r * cos(STEPPER_MOTOR_ANGLE*step)
        y = r * sin(STEPPER_MOTOR_ANGLE*step)
        z = to_milimeter(row)
        pixels.append((x, y, z))
    return pixels

with open(path.join(settings.CORDS_DIR, 'cords.asc'), 'w') as data:
    for step, img in enumerate(listdir(settings.IMAGES_DIR), 1):
        file_name = path.join(settings.IMAGES_DIR, img)
        image = cv2.imread(file_name, cv.CV_LOAD_IMAGE_GRAYSCALE)
        result = find_brightest(image, step)
        cords = ['{} {} {}\n'.format(threes[0], threes[1], threes[2]) for threes in result]
        data.writelines(cords)
