# Adapted from:
# Ian McLoughlin's videos
# https://github.com/Verdagio/Tensorflow-keras-flask-app
# Run the app: env FLASK_APP=webapp.py flask run

import flask as fl
# For decoding images
import base64
# For saving, reading, and resizing images
import cv2
# For working with arrays
import numpy as np
# For using Keras backend
from keras import backend as K
# For working with the model
import keras as kr

app = fl.Flask(__name__)

# Request default resource
@app.route('/', methods=['GET'])
def home():
    return app.send_static_file("index.html")


# load up previously trained model
def init():
    model = kr.models.load_model("../data/models/modelCNN.h5")
    return model


# predict the number
def predictNumber(file):
    # https://stackoverflow.com/a/50377181
    K.clear_session()

    # call init
    model = init()

    prediction = model.predict(file)
    # try now to predict using our pre trained model
    # Returns the indices of the maximum values along an axis
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html
    response = np.array_str(np.argmax(prediction, axis=1))

    return response


@app.route('/uploadFile', methods=['POST'])
def uploaded():
    # Get the image from the request
    canvasImg = fl.request.values.get("the_image", "")

    # print image to cmd terminal
    print(canvasImg)

    # Decode the string to an image
    # https://stackoverflow.com/questions/16214190/how-to-convert-base64-string-to-image
    # first 22 chars have to be cut off (ex. data:image/png;base64,<actual image starts here>)
    decoded_img = base64.b64decode(canvasImg[22:])

    # save image as png
    with open("../data/img/decoded_img.png", "wb") as f:
      f.write(decoded_img)
    # read the file in greyscale mode (using 0)
    img = cv2.imread("../data/img/decoded_img.png", 0)

    # resize the image to 28 * 28
    img = cv2.resize(img, (28, 28))

    # Give a new shape to an array without changing its data
    # convert the data to float so it can be divided it by 255
    newImg = np.ndarray.flatten(np.array(img)).reshape(1, 28, 28, 1).astype('float32')

    # divide by 255 to make it 0 or 1
    newImg /= 255

    # Call predictNumber function on the image
    response = predictNumber(newImg)

    # return prediction
    return response
