import gzip
import os
import requests
import numpy as np
import cv2

IMAGE_SIZE = 28

# extract image from dataset
def extract_sample(filename):
  with gzip.open(filename) as g:
    # skip the checksum header
    g.read(16)
    buf = g.read(IMAGE_SIZE * IMAGE_SIZE) 
    data = np.frombuffer(buf, dtype=np.uint8)
    data = data.reshape(IMAGE_SIZE, IMAGE_SIZE, 1)
    return data

# download dataset from mnist website
os.system("wget http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz")
image = extract_sample("./t10k-images-idx3-ubyte.gz")
cv2.imwrite("test.jpg", image)
