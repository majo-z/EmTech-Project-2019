//Adapted from: https://medium.com/@zxlee618/drawing-on-a-html-canvas-b7566624b17f
$(document).ready(function() {
  const MAIN_MOUSE_BUTTON = 0;

  function prepareContext(canvasElement) {
    // set the size of the drawingBuffer
    let dpr = window.devicePixelRatio || 1;
    //Return the size of an element and its position relative to the viewport
    let rect = canvasElement.getBoundingClientRect();
    canvasElement.width = rect.width * dpr;
    canvasElement.height = rect.height * dpr;
    
    let context = canvasElement.getContext("2d");
    context.scale(dpr, dpr);
    
    return context;
  }

  function setLineProperties(context) {
    context.lineWidth = 4;
    context.lineJoin = "round";
    context.lineCap = "round";
    return context;
  }

  let clearButton = document.getElementById("clearButton");
  let submitButton = document.getElementById("submitButton");
  let myCanvas = document.getElementById("myCanvas");
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