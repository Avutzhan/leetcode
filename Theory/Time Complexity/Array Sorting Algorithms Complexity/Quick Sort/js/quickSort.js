function quickSort(arr) {
    if (arr.length < 2) {
        return arr;
    } else {
        let pivot = arr[0];

        let less = [];
        let greater = [];

        for (let i = 1; i < arr.length; i++) {
            if (arr[i] <= pivot) {
                less.push(arr[i]);
            }

            if (arr[i] > pivot) {
                greater.push(arr[i]);
            }
        }

        return quickSort(less).concat(pivot, quickSort(greater));
    }

}

console.log(quickSort([10, 5, 2, 3]));
