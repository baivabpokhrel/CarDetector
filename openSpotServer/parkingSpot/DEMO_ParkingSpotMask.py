import cv2
import parkingSpots
from parkingSpotMask import ( get_mask_image_of_parking_spot, get_mask_array_of_parking_spot)

# 0 Flag stands for grayscale.
#	image = cv2.imread('parkingLot.jpg', 0)
# Shape of grayscale is (height, width)
# Shape of color is (height, width, [b, g, r])
# Use gray scale makes generating the 2D mask array easier
image = cv2.imread('parkingLot.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
																				 # Defult : white
image = get_mask_image_of_parking_spot(image, parkingSpots.spot_15, (0, 0, 255)) # Red
image = get_mask_image_of_parking_spot(image, parkingSpots.spot_16, (0, 0, 255)) # Red
image = get_mask_image_of_parking_spot(image, parkingSpots.spot_17, (0, 255, 0)) # Green

cv2.imwrite('maskedParkingLotOverlay.jpg', image)

																			  # Defult : 1 (shows up as dark grey on image)
image = get_mask_array_of_parking_spot(gray_image, parkingSpots.spot_15, 255) # 255 shows up as white on image 

cv2.imwrite('maskedParkingSpot.jpg', image)

