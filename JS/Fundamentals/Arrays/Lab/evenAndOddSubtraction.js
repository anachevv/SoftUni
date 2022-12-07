function main(arr) {
    let evenSum = 0, oddSum = 0;

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % 2 === 0) {
            evenSum += arr[i];
        } else {
            oddSum += arr[i];
        }
    }

    return evenSum - oddSum;
}

console.log(
    main(
        [1,2,3,4,5,6]
    )
)