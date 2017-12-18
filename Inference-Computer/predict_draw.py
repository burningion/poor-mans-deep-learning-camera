from darkflow.net.build import TFNet
import cv2

from io import BytesIO
import time
import requests
from PIL import Image, ImageDraw
import numpy as np


import glob

options = {"model": "cfg/tiny-yolo-voc.cfg", "load": "bin/tiny-yolo-voc.weights", "threshold": 0.15}

tfnet = TFNet(options)


counter = 0
for filename in glob.glob('birds/*.jpg'):
    curr_img = Image.open(filename).convert('RGB')
    curr_imgcv2 = cv2.cvtColor(np.array(curr_img), cv2.COLOR_RGB2BGR)

    result = tfnet.return_predict(curr_imgcv2)
    print(result)
    draw = ImageDraw.Draw(curr_img)
    for det in result:
        draw.rectangle([det['topleft']['x'], det['topleft']['y'], 
                        det['bottomright']['x'], det['bottomright']['y']],
                       outline=(255, 0, 0))
        draw.text([det['topleft']['x'], det['topleft']['y'] - 13], det['label'], fill=(255, 0, 0))
    curr_img.save('birds_labeled/%i.jpg' % counter)
    counter += 1

