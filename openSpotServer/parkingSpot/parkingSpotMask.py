import numpy as np
import cv2

def get_mask_image_of_parking_spot(original_image, parking_spot_polygon, color = (255, 255, 255)):
	""" 
	The function returns a image with the masked parking spot.
	This function is stackable. Can be called multiple times to layer different parking spots on the same picture.

	Parameters: 
		original_image : Original image.
		parking_spot_polygon : np.array that depicts the parking spot.
		color: Color to shade in the parking spot. Defult value -> white.

	Returns: 
		output_image: returns an overlay of parking spot on original image.
	"""
	output_image = original_image
	cv2.fillPoly(output_image, [parking_spot_polygon], color = color)
	return output_image


def get_mask_array_of_parking_spot(original_image, parking_spot_polygon, color = 1):
	""" 
	The function returns a masked parking spot.
	This function is NOT stackable. If called multiple times on the same picture, the previous parking spot's mask will be removed.   

	Parameters: 
		original_image : Original grayscale image.
						 gray = cv2.imread('car_output.jpg', 0) can be used to get grayscale 0 Flag stands for grayscale.
						 gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) can be used to get grayscale
		parking_spot_polygon : np.array that depicts the parking spot
		color: Color to shade in the parking spot(grayscale range 0-> 255). Defult value -> 1.

	Returns: 
	output_image: A 2D mask array where:
			  		if [i][j] is 1 that means that pixel is part of a parking spot
			  		if [i][j] is 0 that means that pixel is not part of a parking spot
	"""
	output_image = np.zeros(shape = original_image.shape, dtype = "uint8")
	cv2.fillPoly(output_image, [parking_spot_polygon], color = color)
	return output_image