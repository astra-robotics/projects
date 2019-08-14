import cv2
import numpy as np

cap = cv2.VideoCapture(0);
while(True):
            ret, image = cap.read()
            if cv2.waitKey(1) != 27 :
                cv2.imshow('image',image)
            else:
                exit()
