const fs = require('fs');

const subtotal = (teaspoons, value0, value1) => {
    let sub = teaspoons * value0 + (100 - teaspoons) * value1;
    return (sub < 0) ? 0 : sub;
}

fs.readFile('test', 'utf8', (err, data) => {
    if (err) throw err;
    let ingredients = Array();
    let input = data.split("\r\n");
    input.forEach(ingredient => {
        let properties = ingredient.substring(ingredient.indexOf(':') + 2, ingredient.length)
        properties = properties.split(', ');
        let values = Array();
        properties.forEach(element => {
            values.push(element.substring(element.indexOf(" ") + 1, element.length));
        });
        ingredients.push(values);
    });
    let maxTotal = 0;
    for(let i = 0; i < ingredients.length; i++) {
        for(let j = i + 1; j < ingredients.length; j++) {
            for(let tp = 0; tp < 101; tp++) {
                let capacity = subtotal(tp, ingredients[i][0], ingredients[j][0]);
                let durability = subtotal(tp, ingredients[i][1], ingredients[j][1]);
                let flavor = subtotal(tp, ingredients[i][2], ingredients[j][2]);
                let texture = subtotal(tp, ingredients[i][3], ingredients[j][3]);
                let total = capacity * durability * flavor * texture;
                if (total > maxTotal) {
                    maxTotal = total;
                }
            }
            console.log(maxTotal);
        }
    }
})