# Adapted from: https://www.palletsprojects.com/p/flask
# Run the app: env FLASK_APP=webapp.py flask run

import flask as fl
# For decoding images
import base64
# For image manipulation
from PIL import Image, ImageOps 
# For saving, reading, and resizing images
import cv2
# For working with arrays
import numpy as np
# For using Keras backend
from keras import backend as K
# For working with the model
import tensorflow as tf
import keras as kr

app = fl.Flask(__name__)

# Request default resource
@app.route('/', methods=['GET'])
def home():
    return app.send_static_file("index.html")

# load up previously trained model
def init():
    model = kr.models.load_model("../data/models/modelCNN.h5")
    graph = tf.get_default_graph()
    return model, graph

def imageParser(data):
    # Get the image fromthe request
    canvasImg = fl.request.values.get("the_image", "")
    # Decode the string to an image
    # https://stackoverflow.com/questions/16214190/how-to-convert-base64-string-to-image
    decoded_img = base64.b64decode(canvasImg[22:]) # first 22 chars have to be cut off
    # save image as png
    with open("../data/img/decoded_img.png", "wb") as f:
      f.write(decoded_img)

@app.route('/uploadFile', methods = ['POST'])
def uploaded():

    # reads the buffered incoming data from the client into one bytestring
    # https://tedboy.github.io/flask/generated/generated/flask.Request.get_data.html
    imageParser(fl.request.get_data())
    img = cv2.imread("../data/img/decoded_img.png", 0)    # read the file in greyscale
    img = cv2.resize(img,(28,28))                          # resize the image to 28 * 28

    # Gives a new shape to an array without changing its data
    # convert the data to float so we can divide it by 255
    newImg = np.ndarray.flatten(np.array(img)).reshape(1, 784).astype('float32')

    # divide by 255 to make it 0 or 1
    newImg /= 255

    return {"message": "Hello"} # send the image back to client side

