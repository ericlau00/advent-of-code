const fs = require('fs');

const vowels = ['a', 'e', 'i', 'o', 'u'];
const disallowed = ['ab', 'cd', 'pq', 'xy'];

const containsThreeVowels = function (string) {
    let count = 0;
    vowels.forEach(element => {
        for (let i = 0; i < string.length; i++) {
            if (string[i] == element) {
                count++;
            }
        }
    });
    return count > 2;
};

const twoLettersInARow = function (string) {
    for (let i = 0; i < string.length - 1; i++) {
        if (string[i] == string[i + 1]) {
            return true;
        }
    }
    return false;
};

const notDisallowed = function (string) {
    for (let i = 0; i < disallowed.length; i++) {
        if (string.includes(disallowed[i])) {
            return false;
        }
    }
    return true;
}

const isNice = function (string) {
    return containsThreeVowels(string) && twoLettersInARow(string) && notDisallowed(string)
}

fs.readFile('input', 'utf8', (err, data) => {
    data = data.split("\n");
    let count = 0;
    console.log(data);
    data.forEach(element => {
        if (isNice(element)) {
            count++;
        }
    });
    console.log(count);
})