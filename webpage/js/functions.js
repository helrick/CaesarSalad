
//check if the Web Speech API is supported by the browser (Firefox and Chrome only)
try {
	var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
	var recognition = new SpeechRecognition();
}
catch(e) {
	console.error(e);
	$('.no-browser-support').show();
}

var textArea = $('#userInputArea');

var userResponse = '';


/*
recognition.continuous = true;

//capture sentence
recognition.onresult = function(event) {
	var current = event.resultIndex;
	var transcript = event.results[current][0].transcript;

	userResponse += transcript;
	userInputArea.val(userResponse);
}

//event handlers
recognition.onstart = function() {
	alert('here');
	instructions.text('Listening...');
}

recognition.onspeechend = function() {
	instructions.text('Ok!');
}

recognition.onerror = function(event) {
	if(event.error == 'no-speech'){
		instructions.text("Sorry, I couldn't quite hear that");
	};
}
*/

/*-----------------------------
      Voice Recognition 
------------------------------*/

// If false, the recording will stop after a few seconds of silence.
// When true, the silence period is longer (about 15 seconds),
// allowing us to keep recording even when the user pauses. 
recognition.continuous = true;

// This block is called every time the Speech APi captures a line. 
recognition.onresult = function(event) {

	// event is a SpeechRecognitionEvent object.
	// It holds all the lines we have captured so far. 
	// We only need the current one.
	var current = event.resultIndex;

	// Get a transcript of what was said.
	var transcript = event.results[current][0].transcript;

	// Add the current transcript to the contents of our Note.
	// There is a weird bug on mobile, where everything is repeated twice.
	// There is no official solution so far so we have to handle an edge case.
	var mobileRepeatBug = (current == 1 && transcript == event.results[0][0].transcript);

	if(!mobileRepeatBug) {
		noteContent += transcript;
		noteTextarea.val(noteContent);
	}
};

recognition.onstart = function() {
       alert("sklfj");	
	instructions.text('Voice recognition activated. Try speaking into the microphone.');
}

recognition.onspeechend = function() {
	instructions.text('You were quiet for a while so voice recognition turned itself off.');
}

recognition.onerror = function(event) {
	if(event.error == 'no-speech') {
		instructions.text('No speech was detected. Try again.');  
	};
}


$('#start-record-btn').on('click', function(e) {

	recognition.start();
});
























//Experiments below

//function for checking if the user has an available mic
/*
function hasMicInput() {
	return !!(navigator.getUserMedia || navigator.webkitGetUserMedia ||
	    navigator.mozGetUserMedia || navigator.msGetUserMedia);
}
*/


//this works to get a media input stream
/*

//test to make sure that the user has media devices
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
*/

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



