#!/usr/bin/env python
# coding: utf-8

# In[6]:


pip install opencv-python


# In[12]:


#Uzair Ahmed
#I201751 CS D
#DIP Assignment 2

##Importing Libraries 
import cv2  ##Importing OpenCV
import numpy as np   ##Importing Numpy
import math  ##Importing Math Library

# Code to read and load Images
image_path = "C:/Users/DELL/Downloads/data/2-1.jpg"
gray_image = cv2.imread(image_path, 0)
color_image = cv2.imread(image_path)


# Apply Gaussian Blur to blur the image

kernel_size = 5
##Function of Gaussian Blur
blurred_image = cv2.GaussianBlur(color_image, (kernel_size, kernel_size), 0)




threshold_low = 50

threshold_high = 150

##Applying the Canny Edge Detection function between the low threshold and high threshold
edges = cv2.Canny(blurred_image, threshold_low, threshold_high)



##Defining Parameters
##For Hough Transformation


distance_res = 2  

ang_resolution = np.pi / 80 

#Threshold
min_ = 15 

min_pixels = 68  

max_pixels = 5  


#Blank Image
line_image = np.copy(color_image) * 0  

#Running Hough Transformation using the parameters assigned above
lines = cv2.HoughLinesP(edges, distance_res, ang_resolution, min_, np.array([]), min_pixels, max_pixels)




#Finding Angles to find the time in the clock image 

angles = []

for line in lines:
    for X1, Y1, X2, Y2 in line:
        cv2.line(line_image, (X1, Y1), (X2, Y2), (255, 0, 0), 5)
        
        angle = np.arctan2(Y2 - Y1, X2 - X1)  # Calculate the angle of the line
        
        angles.append(angle)

        
# Angle between lines
#Abs
angle_between_lines = np.degrees(abs(angles[0] - angles[1]))

print("The Angle determined between the lines is : ", angle_between_lines)

##Finding X and Y center
X_center,Y_center =  gray_image.shape[1] // 2, gray_image.shape[0] // 2
#Y_center = gray_image.shape[1] // 2, gray_image.shape[0] // 2

hand_length = min(X_center, Y_center)

##Converting into radians
angle_between_lines_rad = math.radians(angle_between_lines)

#X Minute Hand
minute_hand_x = int(X_center + hand_length * math.cos(angle_between_lines_rad))

#Y Minute Hand
minute_hand_y = int(Y_center - hand_length * math.sin(angle_between_lines_rad))

#X Hour Hand
X_hour_hand = X_center
#Y Hour Hand
Y_hour_hand = Y_center

hour_angle = math.degrees(math.atan2(Y_hour_hand - Y_center, X_hour_hand - X_center))

##IF Hour hand angle is less than 0 we would add 360 degress
if hour_angle < 0:
    hour_angle += 360

#Converting into hours
hours = int((hour_angle / 360) * 12)

#Converting into minutes
minutes = int((angle_between_lines / 360) * 60)

#PRinting time
print(f"Time Determined is : {hours:02d}:{minutes:02d}")

cv2.imshow('line_image', line_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




