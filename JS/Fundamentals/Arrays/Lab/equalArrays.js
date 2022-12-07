function equalArrays(first, second) {
    let sum = 0;

    for (let i = 0; i < first.length; i++) {
        if (parseInt(first[i]) != parseInt(second[i])) {
            return `Arrays are not identical. Found difference at ${i} index`;
        } else {
            sum += parseInt(first[i]);
        }
    }

    return `Arrays are identical. Sum: ${sum}`;
}

console.log(
    equalArrays(
        ['1','2','3','4','5'], ['1','2','4','4','5']
    )
)