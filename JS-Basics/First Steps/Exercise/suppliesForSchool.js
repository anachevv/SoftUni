function suppliesForSchool(input) {
    let pensPrice = 5.8;
    let markersPrice = 7.2;
    let detergent = 1.2;

    let pensAmount = Number(input[0]);
    let markersAmount = Number(input[1]);
    let detergentQuantity = Number(input[2]);
    let discount = Number(input[3]) / 100;

    let totalPensPrice = pensPrice * pensAmount;
    let totalMarkersPrice = markersPrice * markersAmount;
    let totalDetergent = detergent * detergentQuantity;

    let price = totalPensPrice + totalMarkersPrice + totalDetergent;
    let totalPrice = price - (price * discount);

    console.log(totalPrice);
}

suppliesForSchool(["2", "3", "4", "25"]);
