# Emerging Technologies Project

My name is Marian and I am 4th year software development student at GMIT.
Objectives of this project were to:

1. Create and train a model that recognises hand-written digits using the MNIST dataset using the Keras and Jupyter Python packages. 
2. Create a web application that allows a user to draw a digit using their mouse or touchscreen device.
3. Submit the drawing for recognition to the trained model.

The project consists of:

- [Jupyter Notebook](https://jupyter.org/) that explains the technology behind collecting of datasets; building, training, evaluating, verifying and saving the neural network model.
- data/img folder that contains 10 of my own images for verifying the trained model in the jupyter notebook. The img folder is also used for storing the drawn picture for recognition.
- data/models folder used for storing the trained model.
- data/notebook containing of pictures that are used in jupyter notebook.
- index.html that includes HTML5 canvas for drawing the digits, submit and clear button, h tag that holds the prediction message, title, paragraph with instructions, references to my css and javascript scripts and Bootstrap with reference links and my own bootstrap styling.
- index.js JavaScript that works behind the html in order to create and style the canvas, create the mouse movement events, clear the canvas event, submit the button asynchronous event and errors that may occur during the application running.
- styles.css script that styles various html components, such as background color, canvas size, font size & colour, margins etc.
- [Flask](https://www.palletsprojects.com/p/flask/) web application written in Python language that uses various python packages for manipulating / interacting  with the drawn pictures and the model. Flask also contains a built-in wrapper for generating routes in the form of @app.route('/'), where @app is the name of the object containing our Flask app. The web app is responsible for decoding the string representation of image to actual image, saving it to hard drive, opening it and submitting it to the model for recognition.

# Technologies Used

- Jupyter Notebook
- Python
- Flask application framework
- HTML5
- JavaScript
- Jquery
- Bootstrap
- CSS
- GitHub
- Visual Studio Code with built in terminal
- Firefox browser

# Environment Setup

To be able to run the code in this repository, you must have a Python language installed on your device. The easiest way is to install [Anaconda Distribution](https://www.anaconda.com/), which is a open source platform that contains all necessary machine learning packages and a lot more.

After successful installation, you should be able to run conda on you terminal. Conda is an open source package management system and environment management system that quickly installs, runs and updates packages and their dependencies and it is a part of Anaconda Distribution.

The following commands will help you to check and install all necessary packages that are needed in this project and have Anaconda up to date. Note, that these commands only work on Windows.

Open the Command line or Anaconda prompt(part of Anaconda Distribution):

1. Get all the current environment details

```bash
> conda info
```

2. Get the name, version, build & channel details of all the packages installed.

```bash
> conda list
```

3. Get the Python version.

```bash
> conda list python
```

4. Get the Python environment

```bash
> which python
```

5. Update all packaages including anaconda, conda, python, anaconda-navigator

```bash
> conda update --all
```

6. To make sure you have all necessary packages installed, run the following command

```bash
> conda install keras opencv matplotlib tensorflow numpy pillow
```

# How to Download and Run the application

The repository can be found at https://github.com/majo-z/EmTech-Project-2019. To run the code in this repository, yuo should have [Git](https://git-scm.com/) installed on your machine.
The alternative way is to download the zipped version by clicking on "Clone or download" button, choose "Download ZIP" and un-zip it to your desired location. I will concentrate on cloning the project using Git.

1. Open the Git Bash and clone the repository

```bash
> git clone https://github.com/majo-z/EmTech-Project-2019
```

2. Change into the folder

```bash
> cd EmTech-Project-2019
```

3. Change into the folder

```bash
> cd WebApp
```

4. Run the webapp

```bash
> env FLASK_APP=webapp.py flask run
the webapp.py is now running on the background
```

5. Navigate to your browser and type in the address bar:

```bash
> localhost:5000
or
> 127.0.0.1:5000
```

6. To close the program

```bash
> exit the browser
>in the command line: crtl+c
```

# References:

### HTML5 / JavaScript / jQuery / Bootstrap / CSS

*https://www.sitepoint.com/a-basic-html5-template*

*https://www.developer.com/lang/understanding-the-proper-way-to-lay-out-a-page-with-html5.html*

*http://www.williammalone.com/articles/create-html5-canvas-javascript-drawing-app*

*https://getbootstrap.com/docs/4.3/getting-started/introduction*

*https://getbootstrap.com/docs/4.3/layout/grid*

*https://uxplanet.org/how-the-bootstrap-4-grid-works-a1b04703a3b7*

*https://jquery.com*

*https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL*

*https://medium.com/@zxlee618/drawing-on-a-html-canvas-b7566624b17f*

*https://api.jquery.com/jQuery.post*

*https://www.w3schools.com/css/*

### Python / Flask

*https://palletsprojects.com/p/flask*

*https://docs.python.org/3/library/base64.html*

*https://runawayhorse001.github.io/PythonTipsDS/deploy.html*

*https://github.com/Verdagio/Tensorflow-keras-flask-app*

*https://hackersandslackers.com/flask-routes*

*https://stackoverflow.com/a/16214280*

### Tensorflow

*https://www.tensorflow.org*

*https://en.wikipedia.org/wiki/TensorFlow*

*https://www.youtube.com/watch?v=2FmcHiLCwTU*

*https://www.youtube.com/watch?v=tXVNS-V39A0*

### Keras

*https://keras.io*

*https://en.wikipedia.org/wiki/Keras*

*https://keras.io/losses*

*https://keras.io/metrics*

*https://stackoverflow.com/a/50377181*

*https://www.i2tutorials.com/deep-learning-interview-questions-and-answers/what-is-the-difference-between-keras-and-tensorflow*

*https://www.infoworld.com/article/3336192/what-is-keras-the-deep-neural-network-api-explained.html*

### MNIST

*http://yann.lecun.com/exdb/mnist*

*https://en.wikipedia.org/wiki/MNIST_database*

*https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-from-scratch-for-mnist-handwritten-digit-classification*

### Numpy

*https://numpy.org/devdocs*

*https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html*

*https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html*

### Matplotlib

*https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplot.html*

*https://stackoverflow.com/questions/3584805/in-matplotlib-what-does-the-argument-mean-in-fig-add-subplot111*

### Pillow

*https://pillow.readthedocs.io/en/3.1.x/reference/Image.html*

*https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html#concept-modes*

### Machine Learning

*https://towardsdatascience.com/image-classification-in-10-minutes-with-mnist-dataset-54c35b77a38d*

*https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-from-scratch-for-mnist-handwritten-digit-classification*

*https://machinelearningmastery.com/handwritten-digit-recognition-using-convolutional-neural-networks-python-keras*

*https://www.analyticsvidhya.com/blog/2017/05/25-must-know-terms-concepts-for-beginners-in-deep-learning*

*https://medium.com/@afozbek_/how-to-train-a-model-with-mnist-dataset-d79f8123ba84*

*https://keras.io/layers/convolutional*

*https://medium.com/coinmonks/handwritten-digit-prediction-using-convolutional-neural-networks-in-tensorflow-with-keras-and-live-5ebddf46dc8*

*https://medium.com/@ashok.tankala/build-the-mnist-model-with-your-own-handwritten-digits-using-tensorflow-keras-and-python-f8ec9f871fd3*

*https://www.sitepoint.com/keras-digit-recognition-tutorial*

*https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-from-scratch-for-mnist-handwritten-digit-classification*

*https://www.geeksforgeeks.org/activation-functions-neural-networks*

*https://elitedatascience.com/overfitting-in-machine-learning*

*https://datascience.stackexchange.com/a/23157*

*https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning*

*https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python*

*https://towardsdatascience.com/machine-learning-fundamentals-via-linear-regression-41a5d11f5220*

*https://medium.com/@ashok.tankala/building-digit-prediction-web-application-using-tensorflow-with-keras-and-flask-19f8bbdaec0b*

*https://towardsdatascience.com/writing-your-first-neural-net-in-less-than-30-lines-of-code-with-keras-18e160a35502*

*https://towardsdatascience.com/understanding-neural-networks-from-neuron-to-rnn-cnn-and-deep-learning-cd88e90e0a90*

*https://adeshpande3.github.io/A-Beginner%27s-Guide-To-Understanding-Convolutional-Neural-Networks-Part-2*

# Contact: 

G0340481@gmit.ie