function triangle(n) {
    var result = "";

    for (let i = 1; i <= n; i++) {
        text = i.toString() + ' ';
        result += `\n${text.repeat(i)}`;
    }

    return result.trim();

}

console.log(
    triangle(
        5
    )
)