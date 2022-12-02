function main(x, y, z) {
    var totalSum = x + y + z;

    console.log(`${totalSum} - ${totalSum % 1 === 0 ? "Integer" : "Float"}`);

}

    main(
        9, 100, 1.1
    )