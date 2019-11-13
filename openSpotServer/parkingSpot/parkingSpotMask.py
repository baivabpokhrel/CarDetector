import numpy as np
import cv2

def get_mask_of_parking_spot(original_image, parking_spot_polygon, overlay=False):
	""" 
	The function returns a masked parking spot.

	Parameters: 
	original_image : Original grayscale image.
						gray = cv2.imread('car_output.jpg', 0) can be used to get grayscale 0 Flag stands for grayscale.
						gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) can be used to get grayscale
	parking_spot_polygon : np.array that depicts the parking spot
	overlay : True returns an overlay on original image
			  False returns a mask array,
			  	if [i][j] is 1 that means that pixel is part of a parking spot
			  	if [i][j] is 0 that means that pixel is not part of a parking spot

	Returns: 
	output_image: returns an overlay of parking spot on original image or 
				  a mask array where:
			  		if [i][j] is 1 that means that pixel is part of a parking spot
			  		if [i][j] is 0 that means that pixel is not part of a parking spot
	"""
	output_image = np.zeros(shape = original_image.shape, dtype = "uint8")
	if overlay:
		output_image = original_image

	cv2.fillPoly(output_image, [parking_spot_polygon], color = (1))
	return output_image