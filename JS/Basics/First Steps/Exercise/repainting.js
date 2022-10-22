function repainting(input) {
    let nylon = 1.5;
    let paint = 14.5;
    let thinner = 5;
    let bagPrice = 0.4;

    let nylonQuantity = Number(input[0]);
    let paintQuantity = Number(input[1]);
    let thinnerQuantity = Number(input[2]);
    let hours = Number(input[3]);

    let nylonPrice = (nylonQuantity + 2) * nylon;
    let paitnPrice = (paintQuantity + 0.1 * paintQuantity) * paint;
    let thinnerPrice = thinnerQuantity * thinner;

    let price = nylonPrice + paitnPrice + thinnerPrice + bagPrice;
    let workersSum = (price * 0.3) * hours;

    let totalPrice = price + workersSum;

    console.log(totalPrice);
}

repainting(["10", "11", "4", "8"]);
