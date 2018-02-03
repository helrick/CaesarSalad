//function for checking if the user has an available mic
/*
function hasMicInput() {
	return !!(navigator.getUserMedia || navigator.webkitGetUserMedia ||
            navigator.mozGetUserMedia || navigator.msGetUserMedia);
}
*/

function getUserMedia(options, successCallback, failureCallback) {
  var api = navigator.getUserMedia || navigator.webkitGetUserMedia ||
    navigator.mozGetUserMedia || navigator.msGetUserMedia;
  if (api) {
    return api.bind(navigator)(options, successCallback, failureCallback);
  }
}

function getStream (type) {
  if (!navigator.getUserMedia && !navigator.webkitGetUserMedia &&
    !navigator.mozGetUserMedia && !navigator.msGetUserMedia) {
    alert('User Media API not supported.');
    return;
  }

  var constraints = {};
  constraints[type] = true;
  getUserMedia(constraints, function (stream) {
    var mediaControl = document.querySelector(type);
    
    if ('srcObject' in mediaControl) {
      mediaControl.srcObject = stream;
      mediaControl.src = (window.URL || window.webkitURL).createObjectURL(stream);
    } else if (navigator.mozGetUserMedia) {
      mediaControl.mozSrcObject = stream;
    }
  }, function (err) {
    alert('Error: ' + err);
  });
}


/*

if (hasMicInput()) {
  //alert('getUserMedia() works!')
} else {
  alert('getUserMedia() is not supported in your browser, switch to a device with a microphone to use Debatebot!');
}


MediaStreamTrack.getSources(function(sourceInfos) {
	var audioSource = null;
	for(var i = 0; i !=sourceInfos.length; ++i) {

		var source
*/
		
