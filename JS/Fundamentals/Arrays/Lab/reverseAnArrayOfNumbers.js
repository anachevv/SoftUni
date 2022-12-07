function main(n, numbers) {
    var newArray = [];
    
    for (let i = 0; i < numbers.length; i++) {
        if (i === n) {
            break;
        }
        newArray.push(numbers[i]);
    }

    newArray = newArray.reverse();

    return newArray.join(" ");
}

console.log(
    main(
        3, [10, 20, 30, 40, 50]
    )
)