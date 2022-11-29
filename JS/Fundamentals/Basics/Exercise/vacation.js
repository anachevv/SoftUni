function vacation(people, type, day) {
    var totalSum = 0;
    var message = "";

    if (day === "Friday") {
        if (type === "Students") {
            totalSum += 8.45 * people;
        } else if (type === "Business") {
            totalSum += 10.9 * people;
        } else if (type === "Regular") {
            totalSum += 15 * people;
        }
    } else if (day === "Saturday") {
        if (type === "Students") {
            totalSum += 9.8 * people;
        } else if (type === "Business") {
            totalSum += 15.6 * people;
        } else if (type === "Regular") {
            totalSum += 20 * people;
        }
    } else if (day === "Sunday") {
        if (type === "Students") {
            totalSum += 10.46 * people;
        } else if (type === "Business") {
            totalSum += 16 * people;
        } else if (type === "Regular") {
            totalSum += 22.5 * people;
        }
    }

    if (type === "Students" && people >= 30) {
        totalSum *= 0.85;
    } else if (type === "Business" && people >= 100) {
        totalSum -= 10 * (totalSum / people);
    } else if (type === "Regular" && (people >= 10 && people <= 20)) {
        totalSum *= 0.95;  
    }

    message = `Total price: ${totalSum.toFixed(2)}`;

    return message;

}

console.log(vacation(30,
    "Students",
    "Sunday"
    ))