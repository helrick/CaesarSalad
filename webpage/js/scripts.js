
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
var instructions = $('#instructions');
var userResponse = '';
var questionNum = 0;
var topic = '';
var choice = '';

recognition.continuous = true;

//capture sentence
recognition.onresult = function(event) {
	var current = event.resultIndex;
	var transcript = event.results[current][0].transcript;
	userResponse = transcript;
	textArea.val(userResponse);
	if(questionNum == 0){
		firstResponse();
	}
	if(questionNum == 1){
		secondResponse();
	}

}

function firstResponse(){
	topic = textArea.val();
	var selection = 'you selected ';
	selection += topic;
	selection += '. Do you think ';
	selection += topic;
	selection += '?';
	talk(selection);
	questionNum++;
}

function secondResponse(){
	raw_choice = textArea.val();
	raw_choice = raw_choice.toLowerCase();
	if(raw_choice == 'yes'){
		//do something with response to server
		talk('Ok, you think that ' + topic);
		questionNum++;
	}
	else if(raw_choice == 'no'){
		//server something something
		talk("Ok, you don't think that " + topic);
		questionNum++;
	}
	else if(raw_choice != topic.toLowerCase()){
		talk("I couldn't quite catch that, please answer yes or no to if you think that " + topic);
	}
}


function getFirstInput(){
	var topic = textArea.val();
	var selection = 'you selected';
	selection += topic;
	selection += '. Do you think';
	selection += topic;
	selection += '?';
	talk(selection);
	
	textArea.change(function(){
		var choice = (textArea.val()).substring(topic.length);
		textArea.val(choice);
		talk('You selected ' + choice);

	});

}



//event handlers
recognition.onstart = function() {
	instructions.text('Listening... (Press Spacebar to Stop)');
}

recognition.onspeechend = function() {
	instructions.text('Ok!');
}

recognition.onerror = function(event) {
	if(event.error == 'no-speech'){
		instructions.text("Sorry, I couldn't quite hear that");
	};
}

//if they press record, start recording
$('#start-record-btn').on('click', function(e) {
	if (userResponse.length){
		userResponse += ' ';

	}
	recognition.start();
});

//if they press space, stop recording
document.body.onkeyup = function(e){
    if(e.keyCode == 32){
        recognition.stop();
	instructions.text('Recording paused.')
	
    }
}

//Computer speech

function talk(message) {
	var speech = new SpeechSynthesisUtterance();

	speech.text = message;
	speech.volume = 1;
	speech.rate = 1.1;
	speech.pitch = 1;
	window.speechSynthesis.speak(speech);
}


function sayHello() {
	var welcome = 'hello, welcome to debate a bot. select a topic to begin:';
	talk(welcome);
	instructions.text('Click the button and say a topic from the list');
}





