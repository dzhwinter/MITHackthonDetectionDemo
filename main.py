import cv2
import numpy as np
import requests

# Backend Server IP:Port
BACKEND_URL = "http://172.19.61.250:8100" 


THRESHOLD = 0.3

# NOTE: The image size must be 28x28, if input image is not, please resize or crop to 28x28.
IMAGE_SIZE = 28

img = cv2.imread("test.jpg", 0)
assert img.shape == (IMAGE_SIZE, IMAGE_SIZE), "Please Resize to 28 x 28"
img = img.flatten()
req = {"img": img.tolist()}

# Request to restful server
req = requests.request("POST", url=BACKEND_URL, json=req)
result = np.array(req.json()['data'], dtype='float32')
print result[0].argmax(axis=0)
