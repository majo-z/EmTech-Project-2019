# Adapted from: https://www.palletsprojects.com/p/flask
# Run the app: env FLASK_APP=webapp.py flask run

import flask as fl
# For decoding images
import base64

# For image manipulation
from PIL import Image, ImageOps 

app = fl.Flask(__name__)

# Request default resource
@app.route('/')
def home():
    return app.send_static_file("index.html")

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

