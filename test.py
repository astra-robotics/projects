import cv2
import numpy as np
import imutils

def blue_detect(image):

        #image[:,:,0]=0
        #image[:,:,2]=0
        #cv2.imshow('green',image)

        hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        '''
        (w,h,c)=hsv.shape
        canvas=np.zeros((w,h),np.uint8)
        canvas=hsv[:,:,2]
        #cv2.imshow('hsvg',canvas)
        '''
        lower_blue = np.array([80,50,50])
        upper_blue = np.array([255,100,100])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        res = cv2.bitwise_and(image,image, mask = mask)
        kernel = np.ones((5,5),'uint8')
        dilate = cv2.dilate(mask, kernel)
        #ret,thresh=cv2.threshold(mask,0,255,0)
        image1,contours,hierarchy=cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image,contours,0,(255,255,255),5)
        #image1,contour,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        #blur = cv2.GaussianBlur(image,(11,11),0)
        
        #bilateral = 
        
        #cv2.imshow('gauss',blur)
        cv2.imshow('image', image)
        #cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        cv2.imshow('dilate',dilate)
        #cv2.imshow('canvas', canvas)
        #cv2.imshow('contours',image1)
        #peri = cv2.arcLength(contour, True)
        #approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
        
        if(len(contours) == 1):
            return 1
        else:
            return 0


cap = cv2.VideoCapture(0);
while(True):
            ret, image = cap.read()
            if cv2.waitKey(1) != 27:
                print(blue_detect(image))
            else:
                exit()

