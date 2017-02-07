#!/usr/bin/python

import numpy as np 
import cv2 
import cv2.cv as cv
im_width = 320
im_height = 240


cap = cv2.VideoCapture(0)
cap.set(cv.CV_CAP_PROP_FRAME_WIDTH,im_width)
cap.set(cv.CV_CAP_PROP_FRAME_HEIGHT,im_height)

cv.NamedWindow("Video", 0)

detector = cv2.CascadeClassifier('./sideview_cascade_classifier.xml')

while(True):

    
    ret,frame = cap.read()
    if(ret == False):
        print "Error reading from camera"
        break
    
    frame = cv2.resize(frame,(im_width,im_height))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    r  =  []
    x  =  []

    objects = detector.detectMultiScale(image = gray, rejectLevels = r, levelWeights = x,scaleFactor=1.01, minNeighbors=4)

    for (x,y,w,h) in objects: 

               cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)

    cv2.imshow('Video',frame)
    
    k = cv2.waitKey(3)
        
    if(k & 0xFF == ord('q')):
        cv.DestroyWindow("video") 
        break

cap.release()
cv2.destroyAllWindows()
