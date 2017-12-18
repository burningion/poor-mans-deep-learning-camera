#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response

from camera_opencv import Camera

app = Flask(__name__)

def gen2(camera):
    """Returns a single image frame"""
    frame = camera.get_frame()
    yield frame

@app.route('/image.jpg')
def image():
    """Returns a single current image for the webcam"""
    return Response(gen2(Camera()), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
