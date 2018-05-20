# Poor Man's Deep Learning Camera

Build a thin client deep learning camera in Python with the Raspberry Pi, Flask, and YOLO

![Deep Learning Camera](https://github.com/burningion/poor-mans-deep-learning-camera/raw/master/images/deep-learning-camera.jpg)

## Installation

You'll need a few different libraries installed on the Raspberry Pi. Most notably, OpenCV 3 with Python bindings, along with Flask. 

The Raspberry Pi runs the `Camera-Server` code, and sends back images from a webserver.

On another computer, you'll run the inference script, and it will detect whether or not there are birds in your webcam's image.

For this to run, you'll need to download and install the Darkflow weights, along with the YOLO model of your choice. Once that's installed, you should then be able to start doing inferences.

If you're looking for a pretrained model, I used the `tiny-yolo-voc` weights at the [Darkflow repo](https://github.com/thtrieu/darkflow/).

thtrieu even linked to a Google Drive copy of his models [here](https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU).

## Architecture

![Deep Learning Camera Architecture](https://github.com/burningion/poor-mans-deep-learning-camera/raw/master/images/deeplens.png)

Hopefully this image makes sense. We run a cheap edge computer that just sends images out of the current webcam frame, and the other computer script does the inference on that deep learning camera.

## Blog Post

The blog post accompanying this repo is at [Make Art with Python](https://www.makeartwithpython.com/blog/poor-mans-deep-learning-camera/). 

## Detected Bird Image

Of course, here's a bird that was detected and saved using this script:

![Bird detected using deep learning camera](https://github.com/burningion/poor-mans-deep-learning-camera/raw/master/images/out.jpg)

