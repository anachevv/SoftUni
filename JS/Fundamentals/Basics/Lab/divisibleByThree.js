function numbers() {
    var message = "";

    for (let i = 1; i <= 100; i++) {
        if (i % 3 == 0) {
            message += i + "\n";
        }
    }
    
    return message.trim();
}

console.log(numbers());
