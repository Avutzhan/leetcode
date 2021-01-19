/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
//best solution this simplest than previous
//nums = array
//n = how many pairs of integers in array
var shuffle = function(nums, n) {
    let res = [];
    for (i = 0; i < n; i++) {
        res.push(nums[i],nums[i+n]);
    }
    return res;
};