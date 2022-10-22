function day(text) {

    text = text[0];

    let workingDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
    let weekend = ["Saturday", "Sunday"];

    if (workingDays.includes(text) === true) {
        console.log("Working day");
    } else if (weekend.includes(text) === true) {
        console.log("Weekend");
    }
    else {
        console.log("Error");
    }
}

// day(['Saturday']);
