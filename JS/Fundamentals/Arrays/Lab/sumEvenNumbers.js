function main(arr) {
    var evenNumbers = [];

    for (let i = 0; i < arr.length; i++) {
        if (parseInt(arr[i]) % 2 === 0) {
            evenNumbers.push(parseInt(arr[i]));
        }
    }
    
    if (evenNumbers.length === 0) {
        return 0;
    }

    function sum_reducer(accumulator, currentValue) {
      return accumulator + currentValue;
    }
    
    let sumOfNumbers = evenNumbers.reduce(sum_reducer);

    return sumOfNumbers;
}

console.log(
    main(
        ['1','2','3','4','5','6']
    )
)