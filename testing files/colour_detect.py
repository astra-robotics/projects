import cv2
import numpy as np
import imutils

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

cap = cv2.VideoCapture(0);
while(True):
            ret, image = cap.read()
            if cv2.waitKey(1) != 27:
                print(colour_detect(image))
            else:
                exit()
