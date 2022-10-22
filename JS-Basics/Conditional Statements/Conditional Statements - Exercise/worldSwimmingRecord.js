function worldSwimmingRecord(input) {
    let record = Number(input[0]);
    let distance = Number(input[1]);
    let timePerMeter = Number(input[2]);

    let waterResistanceTime = Math.floor(distance / 15);
    waterResistanceTime *= 12.5;
    let totalTime = distance * timePerMeter + waterResistanceTime;

    if (totalTime < record) {
        console.log(`Yes, he succeeded! The new world record is ${totalTime.toFixed(2)} seconds.`)
    } else {
        let remainingTime = totalTime - record;
        console.log(`No, he failed! He was ${remainingTime.toFixed(2)} seconds slower.`)
    }
}

worldSwimmingRecord(["10464","1500","20"]);
