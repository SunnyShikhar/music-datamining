var app = require('express')();
var bodyParser = require('body-parser');
var db = require('./database/connection.js');

app.post("/insert", function(req, res) {
	var post = {
		id: req.body.username,
        gender: req.body.password,
        age: req.body.age,
        avgMusic: req.body.avgMusic,
        favSong: req.body.favSong,
        enjoyLife: req.body.enjoyLife
	};

	db.query('INSERT INTO survey SET ?', post, function(error) {
		if(error) {
			console.log(error.message);
		} else {
			console.log('success');
		}
	});
});