import numpy as np
from core.cropSettings import (crop_x, crop_y)

#	Absolute position of the parking spots in relation to original non-cropped image
# 					  [x,y]
#                     Top Left,	Top Right,		Bottom Right,	Bottom Left
spot_1 = np.array([[2055,1355],	[2590,1370],	[2590,1870],	[2320,1870]],	np.int32)
spot_2 = np.array([[1850,950],	[2400,965],		[2590,1150],	[2590,1340],	[2040,1325]], np.int32)
spot_3 = np.array([[1510,1330],	[2010,1355],	[2260,1870],	[1535,1850]],	np.int32)
spot_4 = np.array([[1500,938],	[1810,945],		[1998,1328],	[1508,1300]],	np.int32)
spot_5 = np.array([[960,1310],	[1465,1330],	[1480,1838],	[720,1808]],	np.int32)
spot_6 = np.array([[1160,938],	[1465,945],		[1465,1300],	[970,1280]],	np.int32)
spot_7 = np.array([[440,1295],	[910,1310],		[660,1780],		[65,1740]],		np.int32)
spot_8 = np.array([[750,938],	[1120,945],		[920,1280],		[440,1270]],	np.int32)
spot_9 = np.array([[0,1275],	[400,1290],		[20,1730],		[0,1730]],		np.int32)
spot_10 = np.array([[300,938],	[710,945],		[410,1260],		[0,1245],		[0,1190]], np.int32)
spot_12 = np.array([[0,920],	[265,935],		[0,1150]], 		np.int32)
spot_13 = np.array([[1693,620],	[1900,620],		[1962,698],		[1736,698]],	np.int32)
spot_14 = np.array([[1485,620],	[1675,620],		[1710,698],		[1490,696]],	np.int32)
spot_15 = np.array([[1282,620],	[1469,620],		[1470,695],		[1250,693]],	np.int32)
spot_16 = np.array([[1080,620],	[1265,620],		[1230,692],		[1015,690]],	np.int32)
spot_17 = np.array([[860,620],	[1063,620],		[995,690],		[778,686]],		np.int32)
spot_18 = np.array([[669,610],	[839,617],		[760,682],		[550,675]],		np.int32)
spot_19 = np.array([[430,605],	[655,610],		[525,672],		[315,660]],		np.int32)
spot_20 = np.array([[220,595],	[390,600],		[285,657],		[95,655]],		np.int32)
spot_21 = np.array([[0,590],	[165,595],		[60,650],		[0,646]],		np.int32)

spot_list = [ spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10, spot_12, spot_13, spot_14, spot_15, spot_16, spot_17, spot_18, spot_19, spot_20, spot_21]

#	Adjust parking spots to cropped image
for spot in spot_list:
	for points in spot:
		points[0] = points[0]-crop_x
		points[1] = points[1]-crop_y
