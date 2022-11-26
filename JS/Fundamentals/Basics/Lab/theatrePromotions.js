function tickets(dayType, age) {
    var ticketPrice = 0;

    if (age < 0 || age > 122) {
        return "Error!";
    }

    if (age <= 18) {
        if (dayType === "Weekday") {
            ticketPrice = 12;
        } else if (dayType === "Weekend") {
            ticketPrice = 15;
        } else if (dayType === "Holiday") {
            ticketPrice = 5;
        }
    } else if (age <= 64) {
        if (dayType === "Weekday") {
            ticketPrice = 18;
        } else if (dayType === "Weekend") {
            ticketPrice = 20;
        } else if (dayType === "Holiday") {
            ticketPrice = 12;
        }
    } else if (age <= 122) {
        if (dayType === "Weekday") {
            ticketPrice = 12;
        } else if (dayType === "Weekend") {
            ticketPrice = 15;
        } else if (dayType === "Holiday") {
            ticketPrice = 10;
        }
    }

    return ticketPrice + "$";

}