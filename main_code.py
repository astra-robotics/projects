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
        self.colour = {'red':0,'green':0,'blue':0,-1:0} #control dictionary for logic
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
        self.colour = {'red':0, 'blue':0, 'green':0,-1:0}
        self.colour[self.colour_detect(image)]=1
        
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

    #colour detection code
    def colour_detect(image):

        hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

        lower_blue = np.array([100,100,100])
        upper_blue = np.array([140,255,255])

        lower_red = np.array([140,100,100])
        upper_red = np.array([180,255,255])

        lower_green = np.array([60,100,100])
        upper_green = np.array([100,255,255])

        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        red_mask = cv2.inRange(hsv, lower_red, upper_red)
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        
        (w,h,c)=hsv.shape
        image_area = w*h

        blue_area = 0
        red_area = 0
        green_area = 0
        res = cv2.bitwise_and(image,image, mask = green_mask)
        cv2.imshow('res',res)

        _,contours_blue,_ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        _,contours_red,_ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        _,contours_green,_ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt_b in contours_blue:
               blue_area = blue_area + cv2.contourArea(cnt_b)

        for cnt_r  in contours_red:
               red_area = red_area + cv2.contourArea(cnt_r)

        for cnt_g in contours_green:       
               green_area = green_area + cv2.contourArea(cnt_g)
        
        blue_ratio = blue_area/image_area
        red_ratio = red_area/image_area
        green_ratio = green_area/image_area

        colour_ratios = [blue_ratio, red_ratio, green_ratio]
        if(max(colour_ratios)>0.2):
            if(max(colour_ratios) == colour_ratios[0]):
                return 'blue'
            elif(max(colour_ratios) == colour_ratios[1]):
                return 'red'
            else:
                return 'green'
        else:
            return -1
        
    #destructor of class
    def __del__(self):
        print('Program terminated')
        self.cap.release()
        cv2.destroyAllWindows()     
        
if __name__ == '__main__':
    bot = CDbot() #creation of object for doing the task

    
