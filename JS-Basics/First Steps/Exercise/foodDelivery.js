function foodDelivery(input) {
    let chickenMenu = 10.35;
    let fishMenu = 12.4;
    let vegetarianMenu = 8.15;

    let chickenMenusAmount = Number(input[0]);
    let fishMenusAmount = Number(input[1]);
    let vegetarianMenusAmount = Number(input[2]);

    let chickenPrice = chickenMenu * chickenMenusAmount;
    let fishPrice = fishMenu * fishMenusAmount;
    let vegetarianPrice = vegetarianMenu * vegetarianMenusAmount;

    let price = chickenPrice + fishPrice + vegetarianPrice;
    let dessertPrice = 0.2 * price;

    let deliveryTax = 2.5;
    
    let totalPrice = price + dessertPrice + deliveryTax;

    console.log(totalPrice);

}

foodDelivery(['2', '4', '3']);
