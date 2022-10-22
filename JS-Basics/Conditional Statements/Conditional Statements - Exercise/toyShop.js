function toyShop(input) {
    let puzzle = 2.6;
    let doll = 3;
    let teddyBear = 4.1;
    let minion = 8.2;
    let truckToy = 2;

    let tripPrice = Number(input[0]);
    let puzzlesAmount = Number(input[1]);
    let dollsAmount = Number(input[2]);
    let teddyBearsAmount = Number(input[3]);
    let minionsAmount = Number(input[4]);
    let truckToyAmount = Number(input[5]);
    let totalAmount = puzzlesAmount + dollsAmount + teddyBearsAmount + 
    minionsAmount + truckToyAmount;

    let puzzlePrice = puzzle * puzzlesAmount;
    let dollPrice = doll * dollsAmount;
    let teddyBearPrice = teddyBear * teddyBearsAmount;
    let minionPrice = minion * minionsAmount;
    let truckPrice = truckToy * truckToyAmount;

    let totalPrice = puzzlePrice + dollPrice + teddyBearPrice + 
    minionPrice + truckPrice;
    
    if (totalAmount> 50 || totalAmount == 50) {
        totalPrice *= 0.75;
    }

    totalPrice *= 0.9;

    if (totalPrice > tripPrice || totalPrice == tripPrice) {
        let remainingMoney = totalPrice - tripPrice;
        console.log(`Yes! ${remainingMoney.toFixed(2)} lv left.`);
    } else {
        let remainingMoney = tripPrice - totalPrice;
        console.log(`Not enough money! ${remainingMoney.toFixed(2)} lv needed.`);
    }
}

toyShop(["40.8","20","25","30","50","10"]);
