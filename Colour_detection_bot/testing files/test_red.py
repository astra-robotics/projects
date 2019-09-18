import cv2
import numpy as np
import time

def red_detect(image):

        #image[:,:,0]=0
        #image[:,:,2]=0
        #cv2.imshow('red',image)

        hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV) #convert RGB image to HSV for easier detection of colour

        lower_red = np.array([120,150,150]) #lower limit of red colour in HSV (change for green and blue; view test_green and test_blue for those values)
        upper_red = np.array([200,255,255]) #upper limit of red colour in HSV (change for green and blue; view test_green and test_blue for those values)

        blur = cv2.GaussianBlur(hsv,(15,15),0) #blur image for noise reduction (kinda needs to be optimised)
        mask = cv2.inRange(blur, lower_red, upper_red) #mask for only red colour
        
        res = cv2.bitwise_and(image,image, mask = mask) #show resultant image with red
        #kernel = np.ones((5,5),'uint8') 
        #dilate = cv2.dilate(mask, kernel)
        #ret,thresh=cv2.threshold(mask,0,255,0)
        contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #find contours possible on the masked image
        #cv2.drawContours(res,contours,-1,(255,255,255),5)
        #image1,contour,hierarchy=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        
        #bilateral = 
        
        #cv2.imshow('gauss',blur)
        cv2.imshow('image', image)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        #cv2.imshow('dilate',dilate)
        #cv2.imshow('canvas', canvas)
        #cv2.imshow('contours',image1)
            
        if(len(contours) == 1): #if only 1 contour found, red colour object seen
            return 1
        else:
            return 0


cap = cv2.VideoCapture(0);
while(True):
            ret, image = cap.read()
            if cv2.waitKey(1) != 27:
                #start_time = time.time()
                print(red_detect(image))
                #print("\n"+str(time.time()-start_time))
            else:
                exit()

