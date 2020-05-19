const fs = require('fs')

fs.readFile('input', 'utf8', (err, data) => {
    if (err) throw err;
    let count = 0;
    let map = Object();
    let coords = [0, 0];
    let direction = {
        '>': [1, 0],
        '<': [-1, 0],
        '^': [0, 1],
        'v': [0, -1]
    }

    let deliverGifts = () => {
        if (!(coords[0] in map)) {
            map[coords[0]] = new Array();
            map[coords[0]].push(coords[1]);
            count++;
        } else {
            if (!(map[coords[0]].includes(coords[1]))) {
                map[coords[0]].push(coords[1]);
                count++;
            }
        }
    }

    for (let i = 0; i < data.length; i++) {
        let d = data.substring(i, i + 1);
        deliverGifts();
        coords[0] += direction[d][0];
        coords[1] += direction[d][1];
        deliverGifts();
    }

    console.log(count);
})