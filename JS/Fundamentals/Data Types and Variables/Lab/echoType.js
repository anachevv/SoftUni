function main(data) {
    var message = `${typeof data}\n`;

    if (typeof data === "string" || typeof data === "number") {
        message += data;
    } else {
        message += "Parameter is not suitable for printing";
    }

    return message;

}

console.log(
    main(
        null
    )
)