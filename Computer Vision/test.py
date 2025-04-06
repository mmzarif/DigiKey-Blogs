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

# Define HSV range for blue color (adjust if needed)
lower_blue = np.array([100, 100, 50])
upper_blue = np.array([140, 255, 255])

# Create a mask for blue regions
mask = cv2.inRange(hsv, lower_blue, upper_blue)

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