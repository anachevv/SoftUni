function displayNumbers() {
    var message = "";
    for (let i = 1; i <= 5; i++) {
        message += i + "\n";
    }
    
    return message.trim();
}

console.log(displayNumbers());