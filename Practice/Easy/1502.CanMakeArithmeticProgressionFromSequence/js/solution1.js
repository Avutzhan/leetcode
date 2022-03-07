/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canMakeArithmeticProgression = function(arr) {
    arr = [...arr].sort((a, b) => a - b);

    for (let i = 2; i < arr.length; i++) {
        if (arr[i - 1] - arr[i - 2] != arr[i] - arr[i - 1]) {
            return false;

        }
    }
    return true;
};