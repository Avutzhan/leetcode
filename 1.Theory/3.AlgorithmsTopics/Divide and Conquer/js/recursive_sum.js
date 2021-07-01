//recursive

function sum(arr) {
    if (arr.length == 0) {
        return 0;
    }

    return arr[0] + sum(arr.slice(1));
}

console.log(sum([2,2,2,2,2]));