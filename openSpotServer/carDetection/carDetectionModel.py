import os
import numpy as np
import cv2
import mrcnn.config
import mrcnn.utils
from mrcnn.model import MaskRCNN
from IPython.display import Image


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Configuration that will be used by the Mask-RCNN library
class MaskRCNNConfig(mrcnn.config.Config):
    NAME = "coco_pre-trained_model_config"
    IMAGES_PER_GPU = 1
    GPU_COUNT = 1
    NUM_CLASSES = 1 + 80  # COCO data-set has 80 classes + one background class
    DETECTION_MIN_CONFIDENCE = 0.6
    BATCH_SIZE = 2


# Filter a list of Mask R-CNN detection results to get only the detected cars / trucks
def get_car_boxes(boxes, class_ids):
    current_car_boxes = []

    for i, current_box in enumerate(boxes):
        # If the detected object isn't a car / truck / bus, skip it
        if class_ids[i] in [3, 8, 6]:
            current_car_boxes.append(current_box)

    return np.array(current_car_boxes)


def find_cars(image_path):

    # Directory to save logs and trained model
    model_dir = os.path.join(os.path.join(BASE_DIR, 'carDetection'), "logs")

    # Local path to trained weights file
    coco_model_path = os.path.join(BASE_DIR, 'carDetection/mask_rcnn_coco.h5')

    # Create a Mask-RCNN model in inference mode
    model = MaskRCNN(mode="inference", model_dir=model_dir, config=MaskRCNNConfig())

    # Load pre-trained model
    model.load_weights(coco_model_path, by_name=True)

    parked_car_boxes = None
    rgb = cv2.imread(image_path)
    x = 0
    y = 1000
    h = 3000
    w = 3000
    crop = rgb[y:y + h, x:x + w]

    # Run the image through the Mask R-CNN model to get results.
    results = model.detect([crop], verbose=0)

    # Mask R-CNN assumes we are running detection on multiple images.
    # We only passed in one image to detect, so only grab the first result.
    r = results[0]

    # The r variable will now have the results of detection:
    # - r['rois'] are the bounding box of each detected object
    # - r['class_ids'] are the class id (type) of each detected object
    # - r['scores'] are the confidence scores for each detection
    # - r['masks'] are the object masks for each detected object (which gives you the object outline)

    # Filter the results to only grab the car / truck bounding boxes
    car_boxes = get_car_boxes(r['rois'], r['class_ids'])

    print("Cars found in photo:")

    # Draw each box on the frame
    for box in car_boxes:
        print("Car: ", box)

        y1, x1, y2, x2 = box

        # Draw the box
        cv2.rectangle(crop, (x1, y1), (x2, y2), (0, 255, 0), 1)

    cv2.imwrite(image_path, crop)
    # cv2.destroyAllWindows()
    # Image('car_output.jpg')
    # return 'car_output.jpg'
