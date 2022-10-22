function shopping(input) {
    let budget = Number(input[0]);
    let cardsAmount = Number(input[1]);
    let processorsAmount = Number(input[2]);
    let memoryAmount = Number(input[3]);

    let graphicCard = 250 * cardsAmount;
    let processor = 0.35 * graphicCard;
    let memory = 0.1 * graphicCard;

    let remainingMoney = 0;

    let totalPrice = graphicCard + processor * processorsAmount + memory * memoryAmount;

    if (cardsAmount > processorsAmount) {
        totalPrice *= 0.85;
    }

    if (budget > totalPrice || budget == totalPrice) {
        remainingMoney = budget - totalPrice;
        console.log(`You have ${remainingMoney.toFixed(2)} leva left!`);
    } else {
        remainingMoney = totalPrice - budget;
        console.log(`Not enough money! You need ${remainingMoney.toFixed(2)} leva more!`);
    }
}

shopping(["920.45","3","1","1"]);
