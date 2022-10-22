function petShop(input) {
    let pricePerDog = 2.5;
    let pricePerCat = 4;

    let dogFoodAmount = input[0];
    let catFoodAmount = input[1];

    let totalDogFoodPrice = Number(pricePerDog * dogFoodAmount);
    let totalCatFoodPrice = Number(pricePerCat * catFoodAmount);
    let totalPrice = Number(totalDogFoodPrice + totalCatFoodPrice);

    console.log(`${totalPrice} lv.`);
}

petShop([4, 2.5])
