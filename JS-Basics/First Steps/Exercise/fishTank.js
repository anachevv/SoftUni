function fishTank(input) {
    let length = Number(input[0]);
    let width = Number(input[1]);
    let height = Number(input[2]);
    let percentage = Number(input[3]) / 100;

    let volume = length * width * height / 1000;
    let totalVolume = volume - (percentage * volume);

    console.log(totalVolume);
}

fishTank(['85', '75', '47', '17']);
