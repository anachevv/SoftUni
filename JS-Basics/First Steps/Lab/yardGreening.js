function yardGreening(input) {
    let pricePerKm = 7.61;
    let area = input[0];
    let price = Number(pricePerKm * area);
    let priceDiscount = 0.18 * price;
    let totalPrice = price - priceDiscount;

    console.log(`The final price is: ${totalPrice} lv.`);
    console.log(`The discount is: ${priceDiscount} lv.`);
}

yardGreening([150])
