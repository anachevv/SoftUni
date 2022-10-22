function vacationBooksList(input) {
    let pages = Number(input[0]);
    let pagesPerHour = Number(input[1]);
    let daysToGo = Number(input[2]);

    let totalHours = pages / pagesPerHour;
    let hoursPerDay = totalHours / daysToGo;

    console.log(hoursPerDay);
}

vacationBooksList(["212", "20", "2"]);
