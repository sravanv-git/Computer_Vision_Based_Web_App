"""
Run a rest API exposing the yolov5s object detection model
"""
import argparse
import io

import torch
from PIL import Image
from flask import Flask, request,render_template,Response
import detect

app = Flask(__name__)



@app.route("/")
def index():
    # rendering webpage
    return render_template('jimmy.html')

@app.route('/video_feed')
def video_feed():
    return Response(detect.run(source="0"),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    model = torch.load("yolov5s.pt")
    app.run(host="127.0.0.1", port=args.port)  # debug=True causes Restarting with stat
