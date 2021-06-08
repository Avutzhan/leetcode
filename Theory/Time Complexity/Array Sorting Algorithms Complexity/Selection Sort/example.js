function findSmallest(arr) {
    var smallest = arr[0];
    var smallest_index = 0;

    for (var i = 1; i < arr.length; i++) {
        if (arr[i] < smallest) {
            smallest = arr[i];
            smallest_index = i;
        }
    }

    return smallest_index;
}

function selectSort(arr) {
    var newArr = [];
    for (var i = 0, len = arr.length; i < len ; i++) {
        smallest = findSmallest(arr);
        newArr.push(arr.splice(smallest, 1)[0]);
    }

    return newArr;
}

console.log(selectSort([5, 3, 6, 2, 10]))