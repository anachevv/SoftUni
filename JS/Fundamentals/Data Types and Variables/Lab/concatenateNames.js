function concatenate(firstName, surname, delimeter) {
    return `${firstName}${delimeter}${surname}`;
}

console.log(
    concatenate(
        'John',
        'Smith',
        '->'

    )
)