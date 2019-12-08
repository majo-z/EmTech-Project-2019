//Adapted from: https://medium.com/@zxlee618/drawing-on-a-html-canvas-b7566624b17f
$(document).ready(function () {
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

  let myCanvas = document.getElementById("myCanvas");
  myCanvas.style.backgroundColor = "#003366"; //change canvas background
  let theContext = prepareContext(myCanvas);
  let shouldDraw = false;

  myCanvas.addEventListener("mousedown", start);
  myCanvas.addEventListener("mouseup", end);
  myCanvas.addEventListener("mousemove", move, false);

  $("#clearButton").on('click', function (e) {
    e.preventDefault();
    theContext.clearRect(0, 0, theContext.canvas.width, theContext.canvas.height);
    // https://api.jquery.com/empty, https://stackoverflow.com/a/25096037
    $('#predictedNumber').hide().empty();
  });

  $("#submitButton").on('click', function (e) {
    // Prevent the form actually submitting.
    e.preventDefault();
    // Initialise canvas
    canvas = myCanvas;

    // Send AJAX request for image from the server
    // https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL
    var img = canvas.toDataURL();
    // console.log(img);

    // https://stackoverflow.com/a/25096037
    $('#predictedNumber').show();

    //https://api.jquery.com/jQuery.post/
    $.post("/uploadFile", { the_image: img })
      .done(function (data) {
        // Update the text h1 tag with the image.
        $("#predictedNumber").text("Prediction: " + data);
      })
      .fail(function (err) {
        $("#predictedNumber").text("Something went wrong... " + err);
      });
  }); //submitButton

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