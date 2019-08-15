import cv2
import numpy as np
import imutils

def green_detect(image):

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
        lower_green = np.array([36,100,100])
        upper_green = np.array([80,255,255])

        blur = cv2.GaussianBlur(hsv,(15,15),0)
        mask = cv2.inRange(blur, lower_green, upper_green)
        
        res = cv2.bitwise_and(image,image, mask = mask)
        kernel = np.ones((5,5),'uint8')
        dilate = cv2.dilate(mask, kernel)
        #ret,thresh=cv2.threshold(mask,0,255,0)
        image1,contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(res,contours,-1,(255,255,255),5)
        #image1,contour,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        
        #bilateral = 
        
        #cv2.imshow('gauss',blur)
        cv2.imshow('image', image)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        #cv2.imshow('dilate',dilate)
        #cv2.imshow('canvas', canvas)
        #cv2.imshow('contours',image1)
            
        if(len(contours) == 1):
            return 1
        else:
            return 0


cap = cv2.VideoCapture(0);
while(True):
            ret, image = cap.read()
            if cv2.waitKey(1) != 27:
                print(green_detect(image))
            else:
                exit()

