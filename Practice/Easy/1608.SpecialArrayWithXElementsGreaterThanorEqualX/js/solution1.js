/**
 * @param {number[]} nums
 * @return {number}
 */
var specialArray = function(nums) {
    for (let i = 0; i <= nums.length; ++i) {
        let c = 0;
        for (const num of nums) {
            num >= i && ++c;
        }
        if (c === i) return i;
    }
    return -1;
};