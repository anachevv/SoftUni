function depositCalculator(input) {
    let depositSum = Number(input[0]);
    let deadLine = Number(input[1]);
    let annualInterestRate = Number(input[2]) / 100;

    let totalSum = Number(depositSum + deadLine * 
        ((depositSum * annualInterestRate) / 12));
    
    console.log(totalSum);
}

depositCalculator(["2350", "6", "7"]);
