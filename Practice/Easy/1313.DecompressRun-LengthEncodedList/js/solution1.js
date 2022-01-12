/**
 * @param {number[]} nums
 * @return {number[]}
 * simple to understand
 */
var decompressRLElist = function(nums) {
    var result = [];

    for (var i = 1; i < nums.length; i += 2 ) {
        for (var j = 0; j < nums[i - 1]; j++ ) {
            result.push(nums[i]);
        }
    }

    return result;
};