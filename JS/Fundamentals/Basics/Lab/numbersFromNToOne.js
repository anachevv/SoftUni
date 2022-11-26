function numbers(n) {
    var message = "";

    while (n >= 1) {
        message += n + "\n";
        n--;
    }

    return message.trim();
}

console.log(numbers(100));