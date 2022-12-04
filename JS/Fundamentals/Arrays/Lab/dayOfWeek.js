function main(number) {
    var days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"};

    if (number in days) {
        return days[number];
    }
    return "Invalid day!";

}

console.log(
    main(
        7
    )
)