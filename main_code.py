'''
Code developed for colour detection bot as an activity by Astra Robotics Club in RV College of Engineering
This is for a simple 2 wheeled bot to:
1) Move forward if green colour is seen
2) Stop if red colour is seen
3) Move backward if blue colour is seen
All code lines commented below are for testing and debugging purposes and may be kindly ignored.
Code is also further commented to explain a few key code lines
'''
import cv2
import numpy as np
from gpiozero import Robot
from collections import Counter as ctr

class CDbot:
    
    #contructor of class
    def __init__(self):
        
        window = np.zeros((100,100)) #initialising a black 100x100 window for using escape to quit
        self.colour = {'red':0,'green':0,'blue':0} #control dictionary for logic
        left = (4,14)  #left wheel gpio pins
        right = (17,18) #right wheel gpio pins
        self.robot = Robot(left,right) #robot initialisation class call
        self.cap = cv2.VideoCapture(0) #recording video from camera 0 (i.e. the camera on rpi)
        
        while(True):
            ret, image = self.cap.read() #read from camera
            if cv2.waitKey(1) != 27 : 
                cv2.imshow('window',window) #show the window previously made
                self.botmove(image) #main bot moving method call
            else:
                break #exit if escape key is pressed 
    
    #bot movement mechanics
    def botmove(self,image):
        self.colour_verify(image) #colour verifying logic to avoid random colour detection defect
        #self.colour = {'red':self.red_detect(image),'green':self.green_detect(image),'blue':self.blue_detect(image)}
        #print(self.colour) 
        if self.colour['red'] == 1:
            #print('stop')
            self.robot.stop() #stops robot if red is verified
        elif self.colour['green'] == 1:
            #print('forward')
            self.robot.forward() #moves robot forward if green is verified
        elif self.colour['blue'] == 1:
            #print('reverse')
            self.robot.reverse() #moves robot reverse if blue is verified
        else:
            pass #don't do anything
    
    #verification of colour
    def colour_verify(self,image):
        
        #list initialisations for logic
        red = [] 
        green = []
        blue = []
        
        #append three outputs from each detect function
        for i in range(3):
            red.append(self.red_detect(image))
            green.append(self.green_detect(image))
            blue.append(self.blue_detect(image))
            
        #reinitialising to zero to avoid the case of 2 or more being 1
        self.colour = {'red':0,'green':0,'blue':0}
        
        #if 2 or more out of 3 in each of the lists is 1, verify that as the colour
        if(ctr(red)[1]>=2):
            self.colour['red'] = 1
        else:
            self.colour['red'] = 0
            if(ctr(green)[1]>=2):
                self.colour['green'] = 1
            else:
                self.colour['green'] = 0
                if(ctr(blue)[1]>=2):
                    self.colour['blue'] = 1
                else:
                    self.colour['blue'] = 0
    
    #function for detection of red (refer to test_red.py for explanation all 3 functions together)        
    def red_detect(self,image):

        hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        
        lower_red = np.array([120,150,150])
        upper_red = np.array([200,255,255])

        blur = cv2.GaussianBlur(hsv,(15,15),0)
        mask = cv2.inRange(blur, lower_red, upper_red)
        
        res = cv2.bitwise_and(image,image, mask = mask)

        image1,contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        if(len(contours) == 1):
            return 1
        else:
            return 0
        
    #function for detection of green       
    def green_detect(self,image):

        hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        lower_green = np.array([36,100,100])
        upper_green = np.array([80,255,255])

        blur = cv2.GaussianBlur(hsv,(15,15),0)
        mask = cv2.inRange(blur, lower_green, upper_green)
        
        res = cv2.bitwise_and(image,image, mask = mask)

        image1,contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            
        if(len(contours) == 1):
            return 1
        else:
            return 0
    
    #function for detection of blue
    def blue_detect(self,image):

        hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        lower_blue = np.array([100,150,0])
        upper_blue = np.array([140,255,255])

        blur = cv2.GaussianBlur(hsv,(15,15),0)
        mask = cv2.inRange(blur, lower_blue, upper_blue)
        
        res = cv2.bitwise_and(image,image, mask = mask)

        image1,contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            
        if(len(contours) == 1):
            return 1
        else:
            return 0
    
    #destructor of class
    def __del__(self):
        print('Program terminated')
        self.cap.release()
        cv2.destroyAllWindows()     
        
if __name__ == '__main__':
    bot = CDbot() #creation of object for doing the task

    
