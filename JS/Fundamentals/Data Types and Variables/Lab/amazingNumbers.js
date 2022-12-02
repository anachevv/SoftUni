function main(number) {
    let numberString = number.toString();
    var sum = 0;
    
    for (let i = 0; i < numberString.length; i++) {
        sum += Number(numberString[i]);
    }

    return `${number} Amazing? ${sum.toString().includes('9') === true ? "True" : "False"}`;

}

console.log(
    main(
        1233
    )
)