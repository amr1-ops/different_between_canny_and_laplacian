# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 14:24:31 2023

@author: aamr6
"""

import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while True:
    success, frame = camera.read()
    
    # cv.namedWindow('normal', cv.WINDOW_NORMAL)
    # cv.resizeWindow('normal', 500,480)
    # cv.imshow('normal',frame)
    
    
    laplacian = cv.Laplacian(frame,cv.CV_64F)
    #convert from 64bit for [0:255] to visualize
    laplacian = np.uint8(laplacian)
    cv.imshow('Laplacian',laplacian)
    
    edges = cv.Canny(frame,100,100)
    cv.imshow('Canny',edges)
    
    
    if cv.waitKey(1) == ord('x'):
        break

camera.release()
cv.destroyAllWindows()