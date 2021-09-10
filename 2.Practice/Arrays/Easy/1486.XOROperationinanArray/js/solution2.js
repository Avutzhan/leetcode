/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
var xorOperation = function(n, start) {
    let result = start;
    let nums = [];

    for (let i = 0; i < n; i++) {
        nums.push(start + 2 * i);
    }

    for (let i = 1; i < nums.length; i++) {
        result = result ^ nums[i];
    }

    return result;
};