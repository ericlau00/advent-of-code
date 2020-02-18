const fs = require('fs');

const checkAunt = (aunt, property, value) => {
    if (property in aunt) {
        if(aunt[property] != value) {
            return false;
        }
    }
    return true;
}

fs.readFile('input', 'utf8', (err, data) => {
    if (err) throw err;
    const input = data.split('\r\n');
    let aunts = Array();
    input.forEach(aunt => {
        let temp = aunt.substring(aunt.indexOf(':') + 2);
        temp = temp.split(',');
        let obj = new Object();
        temp.forEach(element => {
            let el = element.trim().split(":");
            obj[el[0]] = Number(el[1]);
        });
        aunts.push(obj)
    });
    let impossibleAunts = Array();
    for(let i = 0; i < aunts.length; i++) {
        if (!checkAunt(aunts[i], 'children', 3)) {
            impossibleAunts.push(i);
        }
        else if (!checkAunt(aunts[i], 'cats', 7)) {
            impossibleAunts.push(i);
        }
        else if (!checkAunt(aunts[i], 'samoyeds', 2)) {
            impossibleAunts.push(i);
        }
        else if (!checkAunt(aunts[i], 'pomeranians', 3)) {
            impossibleAunts.push(i);
        }
        else if (!checkAunt(aunts[i], 'akitas', 0)) {
            impossibleAunts.push(i);
        }
        else if (!checkAunt(aunts[i], 'vizslas', 0)) {
            impossibleAunts.push(i);
        }
        else if (!checkAunt(aunts[i], 'goldfish', 5)) {
            impossibleAunts.push(i);
        }
        else if (!checkAunt(aunts[i], 'trees', 3)) {
            impossibleAunts.push(i);
        }
        else if (!checkAunt(aunts[i], 'cars', 2)) {
            impossibleAunts.push(i);
        }
        else if (!checkAunt(aunts[i], 'perfumes', 1)) {
            impossibleAunts.push(i);
        }
    }
    // for(let i = 0; i < impossibleAunts.length; i++) {
    //     if(impossibleAunts[i] != i) {
    //         console.log(i);
    //     }
    // }
})