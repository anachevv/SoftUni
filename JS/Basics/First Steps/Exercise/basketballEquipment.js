function basketballEquipment(input) {
    let annualTax = Number(input[0]);
    let basketsPrice = annualTax * 0.6;
    let outfitPrice = basketsPrice * 0.8;
    let ballPrice = 1 / 4 * outfitPrice;
    let accessoriesPrice = 1 / 5 * ballPrice;

    let totalPrice = annualTax + basketsPrice + outfitPrice + ballPrice + accessoriesPrice;

    console.log(totalPrice);
}

basketballEquipment(['365']);
