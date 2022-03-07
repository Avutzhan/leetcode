function linearSearch(arr, x) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] == x) {
            return i;
        }
    }

    return -1;
}

var arr = [4, 2, 5, 6, 14, 7, 15, 3];

console.log(linearSearch(arr, 14));