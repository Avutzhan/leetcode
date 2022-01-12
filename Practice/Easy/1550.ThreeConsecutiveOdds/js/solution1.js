/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function(arr) {
    for (let i = 0, x = 0; i < arr.length; i++) {
        x = arr[i] % 2 ? x | [1, 2, 4][i % 3] : 0;
        if (7 === x) return true;
    }
    return false;
};