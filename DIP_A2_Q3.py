#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Uzair Ahmed
#I201751 CSD
#DIP Assignment 2

import cv2
import numpy as np
import math

# Load the provided image
input_image = cv2.imread("C:/Users/DELL/Downloads/data/3-1.jpg")

#Image into grayscale
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)


#Binary Threshold
binary_threshold = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)


#Determing Contours
contours, _ = cv2.findContours(binary_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


largest_area = 0
largest_rectangle = None

#Going through the contours
for contour in contours:
    # Get the bounding box of the contour
    x, y, width, height = cv2.boundingRect(contour)

    # Calculate the area of the bounding box
    area = width * height

    # Check if the current rectangle is the largest
    if area > largest_area:
        largest_area = area
        largest_rectangle = input_image[y:y+height, x:x+width]

# Display the image with the largest rectangle outlined
x, y, width, height = cv2.boundingRect(contours[0])

#CV2 Rectange function
cv2.rectangle(input_image, (x, y), (x + width, y + height), (0, 255, 0), 2)

#CV2 IMshow Function
cv2.imshow('Largest Rectangle', largest_rectangle)

#CV2 Wait Function
cv2.waitKey(0)

#CV2 Destory All
cv2.destroyAllWindows()

# Define the lower and upper bounds of the RGB color you want to identify
lower_color_bound = np.array([235, 170, 0])  # Replace with your desired lower RGB values
upper_color_bound = np.array([245, 180, 5])  # Replace with your desired upper RGB values

# Create a mask to isolate the specific color within the defined range
color_mask = cv2.inRange(input_image, lower_color_bound, upper_color_bound)

# Find contours in the color mask
contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Calculate the areas of the detected regions
area_reading = cv2.contourArea(contours[2])

area_writing = cv2.contourArea(contours[1])

area_speaking = cv2.contourArea(contours[0])


print("Reading Area:", area_reading)

print("Writing Area:", area_writing)

print("Speaking Area:", area_speaking)

print("Rectangle Area which is Largest:", largest_area)

# Calculate ratings based on areas relative to the largest rectangle
rating_scale = 10

rating_reading = math.ceil((area_reading / largest_area) * rating_scale)

rating_writing = math.ceil((area_writing / largest_area) * rating_scale)

rating_speaking = math.ceil((area_speaking / largest_area) * rating_scale)


contour_image = input_image.copy()

cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

# Display the image with the identified color contours

cv2.imshow('Color Contours', contour_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

# Create a copy of the original image to draw ratings
image_with_ratings = input_image.copy()

# Draw the contours and ratings on the image
for i, contour in enumerate(contours):
    
    x, y, width, height = cv2.boundingRect(contour)

    # Draw the contour
    cv2.drawContours(image_with_ratings, [contour], -1, (0, 255, 0), 2)

    # Draw the rating as text near the contour
    rating_text = f"Rating: {rating_speaking}" if i == 0 else f"Rating: {rating_writing}" if i == 1 else f"Rating: {rating_reading}"
    
    cv2.putText(image_with_ratings, rating_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    
# Display the image with the identified color contours and ratings
cv2.imshow('Color Contours with Ratings', image_with_ratings)

cv2.waitKey(0)

cv2.destroyAllWindows()


# In[ ]:




