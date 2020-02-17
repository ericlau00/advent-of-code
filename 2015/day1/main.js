const fs = require('fs')

fs.readFile('input', 'utf8', (err, data) => {
    if (err) throw err;
    let floor = 0;
    for (let i = 0; i < data.length; i++) {
        if(data[i] == "(") {
            floor++;
        } else {
            floor--;
        }
    }
    console.log(floor);
})