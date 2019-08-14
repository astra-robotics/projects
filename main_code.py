import cv2
import numpy as np
import imutils
from gpiozero import Robot

class CDbot:
    def __init__(self):
        
        self.colour = [0,0,0]
        left = (4,14)
        right = (17,27)
        self.robot = Robot(left,right)
        cap = cv2.VideoCapture(0)
        
        while(True):
            ret, image = cap.read()
            if cv2.waitKey(1) != 27 :
                botmove(self,image)
            else:
                exit()
                
    def botmove(self,image):
        self.colour = [self.red_detect(self,image),self.green_detect(self,image),self.blue_detect(self,image)]
        if self.colour[0] == 1:
            self.robot.stop()
        else if self.colour[1] == 1:
            self.robot.forward()
        else if self.colour[2] == 1:
            self.robot.reverse()
        else:
            pass
        
    def red_detect(self,image):
        
        image[:,:,0]=0
        image[:,:,1]=0
        #cv2.imshow('red',image)
        
        hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        (w,h,c)=hsv.shape
        canvas=np.zeros((w,h),np.uint8)
        canvas=hsv[:,:,2]
        #cv2.imshow('hsvr',canvas)

        ret,thresh=cv2.threshold(canvas,253,254,0)

        image1,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(thresh,contours,0,(255,255,255),10)
        image1,contour,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        
        if len(approx) == 4:
            return 1
        else:
            return 0
        #cv2.imshow('contours',image1)

    def green_detect(self,image):

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
        lower_green = np.array([50,180,50])
        upper_green = np.array([70,255,150])
        
        mask = cv2.inRange(hsv, lower_green, upper_green)
        
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
        #cv2.imshow('res',res)
        #cv2.imshow('dilate',dilate)
        #cv2.imshow('canvas', canvas)
        #cv2.imshow('contours',image1)
        #peri = cv2.arcLength(contour, True)
        #approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
        
        if(len(contours) == 1):
            return 1
        else:
            return 0
                
    def blue_detect(self,image):

        image[:,:,1]=0
        image[:,:,2]=0
        #cv2.imshow('blue',image)

        hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        (w,h,c)=hsv.shape
        canvas=np.zeros((w,h),np.uint8)
        canvas=hsv[:,:,2]
        #cv2.imshow('hsvb',canvas)

        #gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ret,thresh=cv2.threshold(canvas,251,255,0)
        image1,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(thresh,contours,0,(255,255,255),5)
        image1,contour,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.imshow('contours',image)

        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        
        if len(approx) == 4:
            return 1
        else:
            return 0
    
    def __destroy__(self):
        cap.release()
        cv2.destroyAllWindows()     
        
if __name__ = '__main__':
    while(1):
        bot = CDbot()

    
