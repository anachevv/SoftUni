function numbers(n) {
    var message = "";

    while (n >= 1) {
        if (n == 0) {
            break;
        }
        message += n + "\n";
        n--;
    }

    return message.trim();
}

console.log(numbers(100));