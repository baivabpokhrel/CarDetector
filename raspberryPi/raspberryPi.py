import requests
from fractions import Fraction
from picamera import PiCamera
from time import sleep

static_url = 'http://35.245.175.140/model_form_upload'
static_camera_identifier = 'openspot_deployed_camera_001'
static_image_file = static_camera_identifier + '.jpg'
static_image_path = '/home/pi/CarDetector/raspberryPi/'

def upload_image():
    with open(static_image_path + static_image_file, "rb") as image:
        s = requests.Session()
        # fetch the CSRF cookie
        r1 = s.get(static_url)
        if(r1.status_code == 200):
            csrf_token = r1.cookies["csrftoken"]

            # post stored.csv
            r2 = s.post(
                static_url,
                data={"csrfmiddlewaretoken": csrf_token, "description": static_camera_identifier},
                files={"image": image},
            )


print("Setting up the camera")
# Light Mode 
camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 15

# Dark Mode
# camera = PiCamera(resolution=(2592, 1944),  framerate=Fraction(1, 6))
# camera.shutter_speed = 6000000
# camera.iso = 800
# camera.exposure_mode = 'off'
sleep(2)

print("Setting up complete")

while True :
    print("Taking an image")
    camera.capture(static_image_path + static_image_file)
    print("Done taking an image")
    upload_image()
    print("Image is sent")
    sleep(30)
