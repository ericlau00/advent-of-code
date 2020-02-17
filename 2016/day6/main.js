const fs = require('fs');

fs.readFile('input', 'utf8', (err, data) => {
    if (err) throw err;
    data = data.split('\r\n');
    frequencies = [];
    for(let i = 0; i < data[0].length; i++) {
        frequencies[i] = new Object();
    }
    for(let i = 0; i < data.length; i++) {
        for(let j = 0; j < data[i].length; j++) {
            if(data[i][j] in frequencies[j]) {
                frequencies[j][data[i][j]]++;
            } else {
                frequencies[j][data[i][j]] = 1;
            }
        }
    }
    let word = "";
    for(let i = 0; i < frequencies.length; i++) {
        let max = 0;
        let maxLetter = "";
        for (const letter in frequencies[i]) {
            if (frequencies[i][letter] >= max) {
                max = frequencies[i][letter];
                maxLetter = letter;
            }
        }
        word = word.concat(maxLetter);
    }
    console.log(word);
});