function areaOfFigures(input) {
    let type = input[0];
    let result = 0;
    let a = Number(input[1]);

    if (type == 'square') {
        result = a * a;
    } else if (type == 'rectangle') {
        let b = Number(input[2]);
        result = a * b;
    } else if (type == 'circle') {
        result = Math.PI * Math.pow(a, 2);
    } else if (type == 'triangle') {
        let height = Number(input[2]);
        result = a * height / 2;
    }

    console.log(result.toFixed(3));
}

areaOfFigures(['rectangle', '7', '2.5']);
