# Object_Detection_using_yolo
Object recognition is a general term to describe a collection of related computer vision tasks that involve identifying objects in digital photographs.

Image classification involves predicting the class of one object in an image. 
Object localization refers to identifying the location of one or more objects in an image and drawing abounding box around their extent. Object detection combines these two tasks and localizes and classifies one or more objects in an image.
There are Many Object Detection Models,some of them are:

1.R-CNN Family

2.Yolo family

R-CNN is popular untill yolo is discovered.
Yolo outran every model because of its fastness.
I used yolov5 in this Object detection 

CheckPoints:

1.So Intially for basic idea on Neural Networks we did a small Image Classification on Cats and Dogs.This gave me a general idea on how convolution Network works. I tried with different convolution layers and different kernel size for getting a better accuracy. [ReadMe](https://github.com/sravanv-git/Computer_Vision_Based_Web_App/tree/main/DogvsCat_pred-main#readme)

2.For getting into object detection, I tried to learn Yolov3, Because it is widely used now a days, and also it is very fast(30 frames/sec). Learnt the basic difference b/w R-CNN and Yolo and tried to apply it on different images.

3.Making a Web application for detecting objects on live cam using Flask. Used Yolov5 which is even fatser than Yolov3.  When webcam runs,it send images to the Yolov5 algorithm and it detects a bounding box around the objects. 
