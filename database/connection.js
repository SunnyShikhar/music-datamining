var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'sunny',
  password: '13',
  database: 'mydb'
});

connection.connect(function(err) {
  if(err){
  console.log('Database connection error');
}else{
  console.log('You are now connected...');
}
});

module.exports = connection;