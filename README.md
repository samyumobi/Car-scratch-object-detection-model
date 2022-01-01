# Car-scratch-object-detection-model
Train an object detection model to detect and localize scratches in the images.

1. Train an object detection model on provided data:
https://drive.google.com/drive/folders/1Z_uj0F_tvvFg0PSk4UV0kEe7AkErn0xX?usp=sha
ring
    a) Given a dataset of car scratches, you need to train an object detection model to
    detect and localize scratches in the images.
    b) The train and the val sets are already annotated. Dataset split: 3.4k train images,
    390 val images, and 80 test images.
    c) Basic augmentation such as Gauss noise has been added to the train set already
    to increase the train set size.
    d) The aforementioned link contains two zip files: One whose annotations are in coco
    format and the other one which will have annotations in the Pascal VOC format.
    e) You are free to choose open-source implementations /TensorFlow/Keras/PyTorch
    framework to train your model.
    f) Make sure you have a basic understanding of the model architecture you use.
    g) Make a note of your model performance using different metrics.
2. API : 
    Build a simple API using Flask/FastAPI to deploy the model for running inference:
    API should take images as input and return the predictions as JSON responses i.e.
    for every image in the test set, you should return a JSON output wherein in the key
    can the class of the object that your model found and the value could be the
    coordinates of the object.
