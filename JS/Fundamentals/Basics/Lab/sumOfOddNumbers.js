function numbers(n) {
    var oddNumbers = [];
    var message = ""
    var oddSum = 0;

    do {
        for (let i = 0; i <= 100; i++) {
            if (n == 0) {
                break;
            }
            if (!(i % 2 == 0)) {
                oddNumbers.push(i);
                oddSum += i;
                n--;
            }
        }
    } while (oddNumbers.length < n);

    for (let i = 0; i < oddNumbers.length; i++) {
        message += oddNumbers[i] + "\n";
    }

    message += `Sum: ${oddSum}`;

    return message;
}

console.log(numbers(5));