import cv2
import numpy as np

#load image of ruler
image = cv2.imread("digikeyruler.jpg") 

(height, width) = image.shape[:2] #.shape returns (height, width, channels)

#fit the pop up window on my display
window_width = int(width * 0.5) 
window_height = int(height * 0.5)
cv2.namedWindow("Ruler", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Ruler", window_width, window_height)

cv2.imshow("Ruler", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define HSV thresholds for red (dual range)
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([180, 255, 255])

# Create two masks and combine them
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

# display mask
window_width = int(width * 0.5) 
window_height = int(height * 0.5)
cv2.namedWindow("Mask", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Mask", window_width, window_height)
cv2.imshow("Mask", mask)
cv2.waitKey(0)

# Morphological operation to clean up small gaps
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
clean_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#display clean mask
window_width = int(width * 0.5)
window_height = int(height * 0.5)
cv2.namedWindow("Clean Mask", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Clean Mask", window_width, window_height)
cv2.imshow("Clean Mask", clean_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

#draw contours on the image
contours, _ = cv2.findContours(clean_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
window_width = int(width * 0.5)
window_height = int(height * 0.5)
cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Contours", window_width, window_height)
cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()