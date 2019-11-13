import cv2
from parkingSpots import *
from parkingSpotMask import get_mask_of_parking_spot

# 0 Flag stands for grayscale.
# Shape of grayscale is (height, width)
# Shape of color is (height, width, [r, g, b])
# Use gray scale makes generating the 2D mask array easier
image = cv2.imread('parkingLot.jpg', 0)

image = get_mask_of_parking_spot(image, spot_16, True)
image = get_mask_of_parking_spot(image, spot_17, True)
image = get_mask_of_parking_spot(image, spot_15, True)

cv2.imwrite('maskedParkingLot.jpg', image)