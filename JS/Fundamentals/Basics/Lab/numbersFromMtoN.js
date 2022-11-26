function numbers(m, n) {
    var message = "";

    for (m; m >= n; m--) {
        message += m + "\n";
    }

    return message.trim();
}

console.log(numbers(100, 0));
