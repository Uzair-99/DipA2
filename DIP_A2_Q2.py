#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Uzair Ahmed
#I201751 CSD
#DIP Assignment Q2

import cv2
import numpy as np

# Load the original image
image = cv2.imread("C:/Users/DELL/Downloads/data/1-3.jpg")


# Define the region of interest (ROI) coordinates and dimensions
roi_x = 310  

roi_y = 40   

roi_width = 160  

roi_height = 140  

# Extract the ROI as a template
template = image[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

# Define the lower region

lower_roi_x = 0  

lower_roi_y = 200  

lower_roi_width = image.shape[1]  

lower_roi_height = image.shape[0] - lower_roi_y  


#Code to crop the lower region of the image

lower_region = image[lower_roi_y:lower_roi_y + lower_roi_height, lower_roi_x:lower_roi_x + lower_roi_width]


# Using CV's match funtion to check if two templates match
result = cv2.matchTemplate(lower_region, template, cv2.TM_CCOEFF_NORMED)

#Amount of threshold which will show if match or not
threshold = 0.95


# Matches above the threshold assigned
match_locations = np.where(result >= threshold)

# Reverse the coordinates
match_locations = list(zip(*match_locations[::-1]))  

##IF no threshold no match then print
if not match_locations:
    print("No matches found")
#IF match found
else:
    # Draw rectangles around the matched areas on the original image
    for loc in match_locations:
        top_left = (loc[0] + lower_roi_x, loc[1] + lower_roi_y)
        
        template_height, template_width, _ = template.shape
        
        bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
        
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

        
        
    #Showing the image with a green outline outside the boxes which match
    cv2.imshow('Image with Matches', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# In[ ]:




