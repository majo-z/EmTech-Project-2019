//Adapted from: https://medium.com/@zxlee618/drawing-on-a-html-canvas-b7566624b17f
$(document).ready(function() {
  const MAIN_MOUSE_BUTTON = 0;

  function prepareContext(canvasElement) {
    //Return the size of an element and its position relative to the viewport
    let rect = canvasElement.getBoundingClientRect();
    canvasElement.width = rect.width;
    canvasElement.height = rect.height;

    let context = canvasElement.getContext("2d");
    return context;
  }

  function setLineProperties(context) {
    context.lineWidth = 15;
    context.lineJoin = "round";
    context.lineCap = "round";
    context.strokeStyle = "white"; //change line color
    return context;
  }

  let clearButton = document.getElementById("clearButton");
  let submitButton = document.getElementById("submitButton");
  let myCanvas = document.getElementById("myCanvas"); 
  myCanvas.style.backgroundColor = "#003366"; //change canvas background
  let theContext = prepareContext(myCanvas);
  let shouldDraw = false;

  myCanvas.addEventListener("mousedown", start);
  myCanvas.addEventListener("mouseup", end);
  myCanvas.addEventListener("mousemove", move, false);

  clearButton.addEventListener("click", event => {
    event.preventDefault();
    clearCanvas(theContext);
  });
  function clearCanvas(context) {
    context.clearRect(0, 0, context.canvas.width, context.canvas.height);  
  }

  submitButton.addEventListener("click", event => {
    event.preventDefault();
    submitData(theContext);
  });
  function submitData(context) {
    context = myCanvas;
    //console.log(context.toDataURL());

    // Send AJAX request for image from the server
    //https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL
    var dataURL = context.toDataURL();
    $.post("/upload_image", { the_image: dataURL }, function (data) {
      // Update the text area with the image.
      $("#generatedImage").text("Generated Image: " + data.message);
    });
  }

  function start(event) {
    if (event.button === MAIN_MOUSE_BUTTON) {
      shouldDraw = true;
      setLineProperties(theContext);

      theContext.beginPath();
      
      let elementRect = event.target.getBoundingClientRect();
      theContext.moveTo(event.clientX - elementRect.left, event.clientY - elementRect.top);
    }
  }

  function end(event) {
    if (event.button === MAIN_MOUSE_BUTTON) {
      shouldDraw = false;
    }
  }

  function move(event) {
    if (shouldDraw) {
      let elementRect = event.target.getBoundingClientRect();
      theContext.lineTo(event.clientX - elementRect.left, event.clientY - elementRect.top);
      theContext.stroke();
    }
  }
});