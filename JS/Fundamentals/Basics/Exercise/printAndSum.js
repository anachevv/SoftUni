function printAndSum(start, end) {
    var sumOfNumbers = 0;
    var result = "";

    for (let i = start; i <= end; i++) {
        sumOfNumbers += i;
        result += i + ' ';
    }

    result = result + `\nSum: ${sumOfNumbers}`

    return result.trim();
}

console.log(printAndSum(0, 26));
