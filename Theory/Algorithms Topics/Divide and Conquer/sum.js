function sum(arr) {
    var total = 0;

    for (var i = 0; i < arr.length; i++) {
        total += arr[i];
    }

    return total;
}

console.log(sum([2,2,2,2,2]));