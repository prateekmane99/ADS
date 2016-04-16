var express = require('express');
var http = require('http');
var PythonShell = require('python-shell');
var ut = require('date-utils');


var app = express();



app.use( express.static(__dirname));

app.get('/', function(req, res) {

	return res.sendFile(__dirname + '/god3.html');
});




app.get('/query1' , function(req, res) {

	var row_1 = req.param('d');	
	var header = req.param('h');	
	console.log(row_1);

	console.log(row_1.split(','));

	var options = {
  		//mode: 'text',
  		args: [row_1.split(','), header.split(',')]
	};

	PythonShell.run('abc.py', options, function (err, results) {
  	if (err) throw err;
  	// results is an array consisting of messages collected during execution
  	
  	output = JSON.parse(results);
  	var scoredLabels = output.Results.output1.value.Values[0][0];
  	var scoreProb = output.Results.output1.value.Values[0][1];

  	console.log('DERYL RODRIGUES %j', output);
  	res.send(row_1+','+scoredLabels+','+scoreProb);
  	
	});


});


http.createServer(app).listen(4030, function() {
	console.log("LOADED SERVER");
});