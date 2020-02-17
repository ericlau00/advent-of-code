const fs = require('fs')

fs.readFile('input', 'utf8', (err, data) => {
    if (err) throw err;
    input = data.split("\r\n");
    let paper = 0;
    input.forEach(box => {
        box = box.split("x");
        let lw = box[0] * box[1]
        let wh = box[1] * box[2]
        let hl = box[0] * box[2]
        paper += 2 * (lw + wh + hl);
        if (lw <= wh && lw <= hl) {
            paper += lw;
        } else if (wh <= lw && wh <= hl) {
            paper += wh;
        } else {
            paper += hl;
        }
    });
    console.log(paper)
})