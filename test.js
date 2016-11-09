var db = require('./database/connection.js');

db.query('select * from survey', function(err, result) {
	console.log(result);
});