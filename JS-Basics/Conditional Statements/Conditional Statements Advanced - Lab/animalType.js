function classType(animal) {
    animal = animal[0];
    let mammal = ['dog'];
    let reptile = ['crocodile', 'tortoise', 'snake'];

    if (mammal.includes(animal) === true) {
        console.log("mammal");
    } else if (reptile.includes(animal) === true) {
        console.log("reptile");
    } else {
        console.log("unknown");
    }
}

// classType(['dog']);
