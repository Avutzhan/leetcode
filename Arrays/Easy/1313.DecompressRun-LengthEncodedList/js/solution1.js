/**
 * @param {number[]} nums
 * @return {number[]}
 */
var decompressRLElist = function(nums) {
    return nums.reduce(
        (acc, cur, i, arr) =>
            i % 2 ? [...acc, ...Array(arr[i - 1]).fill(cur)] : acc,
        []
    );
};