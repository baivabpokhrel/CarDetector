import requests
from picamera import PiCamera
from time import sleep

static_url = 'http://35.245.175.140/model_form_upload'
static_camera_identifier = 'openspot_deployed_camera_001'
static_image_file = static_camera_identifier + '.jpg'
static_image_path = '/home/pi/openspot/'

def upload_image():
    with open(static_image_file, "rb") as image:
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



camera = PiCamera()

#camera.rotation = 180
# camera.start_preview(alpha=200)
camera.resolution = (2592, 1944)
camera.framerate = 15

while True :
    camera.capture(static_image_path + static_image_file)
    upload_image()
    print("Image sent")
    sleep(30)
