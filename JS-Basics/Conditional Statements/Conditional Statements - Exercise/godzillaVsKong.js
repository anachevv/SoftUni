function godzillaVsKong(input) {
    let budget = Number(input[0]);
    let extras = Number(input[1]);
    let clothingPrice = Number(input[2]);

    let decorationPrice = budget * 0.1;

    if (extras > 150) {
        clothingPrice *= 0.9;
    }

    let totalPrice = extras * clothingPrice + decorationPrice;

    if (totalPrice > budget) {
        let remainingMoney = totalPrice - budget;
        console.log('Not enough money!');
        console.log(`Wingard needs ${remainingMoney.toFixed(2)} leva more.`);
    } else {
        remainingMoney = budget - totalPrice;
        console.log('Action!');
        console.log(`Wingard starts filming with ${remainingMoney.toFixed(2)} leva left.`);
    }
}

godzillaVsKong(["20000","120","55.5"]);
