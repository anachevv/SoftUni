function round(number, precision) {

    if (precision > 15) {
        precision = 15;
    }
    
    return parseFloat(number.toFixed(precision));
}

console.log(round(3.1415926535897932384626433832795,2));
