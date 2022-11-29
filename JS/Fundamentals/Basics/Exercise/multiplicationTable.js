function multiply(number) {
    var message = "";

    for (let i = 1; i <= 10; i++) {
        message += `${number} X ${i} = ${number * i}\n`;
    }

    return message.trim();

}

console.log(
    multiply(
        5
    )
);