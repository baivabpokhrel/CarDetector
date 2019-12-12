import numpy as np
from core.cropSettings import (crop_x, crop_y)

#	Absolute position of the parking spots in relation to original non-cropped image
# 					  [x,y]
#                     Top Left, Top Right,  Bottom Right, Bottom Left
spot_13 = np.array([[1693,620], [1900,620], [1962,698],   [1736,698]], np.int32)
spot_14 = np.array([[1485,620], [1675,620], [1710,698],   [1490,696]], np.int32)
spot_15 = np.array([[1282,620], [1469,620], [1470,695],   [1250,693]], np.int32)
spot_16 = np.array([[1080,620], [1265,620], [1230,692],   [1015,690]], np.int32)
spot_17 = np.array([[860,620], 	[1063,620], [995,690],	  [778,686]], np.int32)
spot_18 = np.array([[669,610], 	[839,617], 	[760,682],	  [550,675]], np.int32)
spot_19 = np.array([[430,605], 	[655,610], 	[525,672],	  [315,660]], np.int32)
spot_20 = np.array([[220,595], 	[390,600], 	[285,657],	  [95,655]], np.int32)
spot_21 = np.array([[0,590], 	[165,595], 	[60,650],	  [0,646]], np.int32)

spot_list = [ spot_13, spot_14, spot_15, spot_16, spot_17, spot_18, spot_19, spot_20, spot_21]

#	Adjust parking spots to cropped image
for spot in spot_list:
	for points in spot:
		points[0] = points[0]-crop_x
		points[1] = points[1]-crop_y
