function lunchBreak(input) {
    let seriesName = input[0];
    let timePerEpisode = Number(input[1]);
    let breakTime = Number(input[2]);

    let lunchBreak = breakTime / 8;
    let relaxTime = breakTime / 4;
    let freeTime = breakTime - (lunchBreak + relaxTime);

    if (freeTime > timePerEpisode || freeTime == timePerEpisode) {
        remainingTime = freeTime - timePerEpisode;
        console.log(`You have enough time to watch ${seriesName} and left with ${Math.ceil(remainingTime)} minutes free time.`);
    } else {
        remainingTime = timePerEpisode - freeTime;
        console.log(`You don't have enough time to watch ${seriesName}, you need ${Math.ceil(remainingTime)} more minutes.`);
    }
}

lunchBreak(["Teen Wolf","48","60"]);
