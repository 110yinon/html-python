var fs = require('fs');

fs.writeFile('myFile.txt', 'Hello content!', function (err) {
  if (err) throw err;
  console.log('Saved!');
});