# Adapted from: https://www.palletsprojects.com/p/flask
# Run the app: env FLASK_APP=webapp.py flask run

import flask as fl
# For decoding images
import base64
# For image manipulation
from PIL import Image, ImageOps 
# For regular expressions
import re
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

#load up our previously trained model
def init():
    model = kr.models.load_model("./data/models/modelCNN.h5")
    graph = tf.get_default_graph()

    return model, graph

# Add a route for generating image
@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
  # Get the image fromthe request
  myImage = fl.request.values.get("the_image", "")
  
  # Print image to the console
  print(myImage)

  # Decode the string to an image
  # https://stackoverflow.com/questions/16214190/how-to-convert-base64-string-to-image
  decoded_img = base64.b64decode(myImage[22:]) # first 22 chars have to be cut off
  
  # Save the image
  with open("decoded_img.png", "wb") as f:
    
    f.write(decoded_img)
  
  # https://note.nkmk.me/en/python-pillow-invert
  decoded_img = Image.open("decoded_img.png").convert('L')
  decoded_img_invert = ImageOps.invert(decoded_img)
  decoded_img_invert.save('decoded_img_invert.png')

  # Generate and respond with the image
  return {"message": myImage} # send the image back to client side

