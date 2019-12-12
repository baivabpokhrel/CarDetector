import os
import numpy as np
import cv2
import mrcnn.config
from mrcnn import visualize
import mrcnn.utils
from mrcnn.model import MaskRCNN
from core.models import Image
from IPython.display import Image
import sys
sys.path.insert(0,'..')

from parkingSpot.parkingSpotMask import ( get_mask_image_of_parking_spot, get_mask_array_of_parking_spot)
from parkingSpot.parkingSpots import spot_list
from core.cropSettings import (crop_x, crop_y, crop_h, crop_w)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Configuration that will be used by the Mask-RCNN library
class MaskRCNNConfig(mrcnn.config.Config):
    NAME = "coco_pre-trained_model_config"
    IMAGES_PER_GPU = 1
    GPU_COUNT = 1
    NUM_CLASSES = 1 + 80  # COCO data-set has 80 classes + one background class
    DETECTION_MIN_CONFIDENCE = 0.6
    BATCH_SIZE = 2
'''
inputs:
    mask : It is a matrix of mask for the single car in which pixles are set to true if there is mask else to false
    spot : It is a matrix for a single spot which is given a value of 1 where the spot is, and 0 where it isn't
    
output:
    true: if the mask is in the spot
    false: if the mask is not in the spot
'''
def has_car(mask,spot):
    #setting the pixel value other than 0 because while doing the comparsion we only want to count common 1's
    spot[spot==0]=2
    # countign the common 1's
    common=((spot==mask)==1).sum()
    # getting the number of 1's in the spot
    spot_n=(spot==1).sum()
    # calculting the percentage
    percent=common/spot_n
   
    spot[spot==2]=0
    if(percent>0.10):
        return True
    else:
        return False
    

# Filter a list of Mask R-CNN detection results to get only the detected cars / trucks
def get_car_boxes(boxes, class_ids):
    current_car_boxes = []

    for i, current_box in enumerate(boxes):
        # If the detected object isn't a car / truck / bus, skip it
        if class_ids[i] in [3, 8, 6]:
            current_car_boxes.append(current_box)

    return np.array(current_car_boxes)


def find_cars(image_object):

    image_path = image_object.image.path

    # Directory to save logs and trained model
    model_dir = os.path.join(os.path.join(BASE_DIR, 'carDetection'), "logs")

    # Local path to trained weights file
    coco_model_path = os.path.join(BASE_DIR, 'carDetection/mask_rcnn_coco.h5')

    # Create a Mask-RCNN model in inference mode
    model = MaskRCNN(mode="inference", model_dir=model_dir, config=MaskRCNNConfig())

    # Load pre-trained model
    model.load_weights(coco_model_path, by_name=True)

    rgb = cv2.imread(image_path)
    crop = rgb[crop_y:crop_y+crop_h, crop_x:crop_x+crop_w]
    cv2.imwrite(image_path, crop)

    # Run the image through the Mask R-CNN model to get results.
    results = model.detect([crop], verbose=0)

    # Mask R-CNN assumes we are running detection on multiple images.
    # We only passed in one image to detect, so only grab the first result.
    # The r variable will now have the results of detection:
    r = results[0]

    # Filter the results to only grab the car / truck bounding boxes
    car_boxes = get_car_boxes(r['rois'], r['class_ids'])

    # print("Cars found in photo:")
    # Draw each box on the frame
    # for box in car_boxes:
    #     print("Car: ", box)
    #     y1, x1, y2, x2 = box
    #     cv2.rectangle(crop, (x1, y1), (x2, y2), (0, 255, 0), 1)

    gray_image = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

    # Get the all the spots in the parking lot
    emptySpots=[]
    for i in spot_list:
        mask=get_mask_array_of_parking_spot(gray_image, i)
        emptySpots.append(mask)

    fullSpots=[]
    # loop over of the detected object's bounding boxes and masks
    for i in range(0, r["rois"].shape[0]):
        # extract the mask for the current detection, then
        # grab the color to visualize the mask (in BGR format)
        carMask = r["masks"][:, :, i]

        # Highlight found car
        crop = visualize.apply_mask(crop, carMask,[1,0,0], alpha=0.5)

        for index in range(len(emptySpots)):
            if has_car(carMask,emptySpots[index]):
                fullSpots.append(emptySpots.pop(index))
                break
        
    red=[0,0,1]
    green=[0,1,0]
    newImage = crop

    for i in fullSpots:
        newImage = visualize.apply_mask(newImage, i,red, alpha=0.5)

    for i in emptySpots:
        newImage = visualize.apply_mask(newImage, i,green, alpha=0.5) 

    maskedParkingLot = Image(description= image_object.description + "_masked", image = new_image)

    try:
        oldImageMasked = Image.objects.get(description = image_object.description + "_masked")
        oldImageMasked.image.delete()
        oldImageMasked.delete()
        maskedParkingLot.save()
    except Image.DoesNotExist:
        maskedParkingLot.save()

    # cv2.imwrite(image_path[:len(image_path)-4] + "_masked.jpg", new_image)
