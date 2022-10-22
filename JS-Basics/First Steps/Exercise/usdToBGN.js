function usdToBGN(input) {
    let usdMoney = input[0];
    let usdExchangeRate = 1.79549;
    let bgnMoney = Number(usdMoney * usdExchangeRate);

    console.log(bgnMoney);
}

usdToBGN(["12.5"]);
