function timePlus15(input) {
    let hours = Number(input[0]);
    let minutes = Number(input[1]);
    
    minutes += 15;
    hours += ~~(minutes / 60);
    minutes %= 60;

    if (hours > 23) {
        hours = 0;
    }
    if (minutes < 10) {
        console.log(`${hours}:0${minutes}`)
    } else {
        console.log(`${hours}:${minutes}`)
    }
}

timePlus15(['12', '49']);
