function main(newString, char, resultString) {
    var newString = newString.replace('_', char);

    if (newString === resultString) {
        return "Matched";
    }

    return "Not Matched";

}

console.log(
    main(
        'Str_ng', 'i', 'String'
    )
)