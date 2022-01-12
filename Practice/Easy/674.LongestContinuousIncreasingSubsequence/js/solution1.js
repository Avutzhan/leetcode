/**
 * @param {number[]} nums
 * @return {number}
 */
var findLengthOfLCIS = function(nums) {
    let len = 1, maxLen = 0;

    for(let i = 0; i < nums.length; i++) {
        if(nums[i] < nums[i+1]) len++;
        else len = 1;
        maxLen = Math.max(len, maxLen);
    }
    return maxLen;
};