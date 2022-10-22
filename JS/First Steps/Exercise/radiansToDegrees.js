function radiansToDegrees(input) {
    let radiansAngle = input[0];
    let degreesAngle = Number(radiansAngle * 180 / Math.PI);

    console.log(degreesAngle);
}

radiansToDegrees(["3.1416"]);