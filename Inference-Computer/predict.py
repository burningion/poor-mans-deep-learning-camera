from darkflow.net.build import TFNet
import cv2

from io import BytesIO
import time
import requests
from PIL import Image
import numpy as np

options = {"model": "cfg/tiny-yolo-voc.cfg", "load": "bin/tiny-yolo-voc.weights", "threshold": 0.1}

tfnet = TFNet(options)

birdsSeen = 0
def handleBird():
    pass

while True:
    r = requests.get('http://192.168.1.1:5000/image.jpg') # replace with your ip address
    curr_img = Image.open(BytesIO(r.content))
    curr_img_cv2 = cv2.cvtColor(np.array(curr_img), cv2.COLOR_RGB2BGR)

    # uncomment below to try your own image
    #imgcv = cv2.imread('./sample/bird.png')
    result = tfnet.return_predict(curr_img_cv2)
    #print(result)
    for detection in result:
        if detection['label'] == 'bird':
            print("bird detected")
            birdsSeen += 1
            curr_img.save('birds/%i.jpg' % birdsSeen)
    print('running again')
    time.sleep(4)
