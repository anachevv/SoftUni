function getAge(age) {
    var message = "";

    if (age < 0) {
        message = "out of bounds";
    } else if (age <= 2) {
        message = "baby";
    } else if (age <= 13) {
        message = "child";
    } else if (age <= 19) {
        message = "teenager";
    } else if (age <= 65) {
        message = "adult";
    } else if (age >= 66) {
        message = "elder";
    }

    return message;
}

console.log(getAge(20));
console.log(getAge(1));
console.log(getAge(100));
console.log(getAge(-1));