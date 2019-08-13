import cv2
import numpy as np
import imutils
from gpiozero import Robot

class CDbot:
    def __init__(self):
        
        self.colour = {'red':1,'green':2,'blue':3}
        left = (4,14)
        right = (17,27)
        self.robot = Robot(left,right)
        cap = cv2.VideoCapture(0)
        
        while(True):
            ret, image = cap.read()
        
        botmove(self,image)
    
    def botmove(self,image):
        
        if red_detect(self,image) == self.colour['red']:
            self.robot.stop()
            
        if green_detect(self,image) == self.colour['green']:
            self.robot.forward()
            
        if blue_detect(self,image) == self.colour['blue']:
            self.robot.reverse()
            
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
            return self.colour['red']
        else:
            return 0
		#cv2.imshow('contours',image1)

	def green_detect(self,image):

		image[:,:,0]=0
		image[:,:,2]=0
		#cv2.imshow('green',image)

		hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
		(w,h,c)=hsv.shape
		canvas=np.zeros((w,h),np.uint8)
		canvas=hsv[:,:,2]
		#cv2.imshow('hsvg',canvas)

		ret,thresh=cv2.threshold(canvas,248,255,0)
		image1,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		cv2.drawContours(thresh,contours,0,(255,255,255),5)
		image1,contour,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

		#cv2.imshow('contours',image1)
		peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        
        if len(approx) == 4:
            return self.colour['green']
        else 
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
            return self.colour['blue']
        else:
            return 0
	
    def __destroy__(self):
        cap.release()
        cv2.destroyAllWindows()		
		
if __name__ = '__main__':
    while(1):
        bot = CDbot()
        if cv2.waitKey(1) != 'q':
            continue
        else:
            break
    
