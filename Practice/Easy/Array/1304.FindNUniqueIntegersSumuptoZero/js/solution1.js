/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    let arr = new Array(n);

    for (let i = 0; i < n; i++) {
        arr[i] = i * 2 - n + 1;
    }

    return arr;
};