import cv2
import numpy as np
import imutils

def blue_detect(image):

        #image[:,:,0]=0
        #image[:,:,2]=0
        #cv2.imshow('green',image)

        hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        lower_blue = np.array([100,150,0])
        upper_blue = np.array([140,255,255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        (w,h)=mask.shape
        image_area = w*h

        blue_area = 0
        res = cv2.bitwise_and(image,image, mask = mask)

        cv2.imshow('image', image)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)

        _,contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
               blue_area = blue_area + cv2.contourArea(cnt)

        blue_ratio = blue_area/image_area
        print(blue_ratio)

cap = cv2.VideoCapture(0);
while(True):
            ret, image = cap.read()
            if cv2.waitKey(1) != 27:
                blue_detect(image)
            else:
                exit()


