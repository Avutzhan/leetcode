/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    while(nums.indexOf(val,0) >= 0) {
        nums.splice(nums.indexOf(val,0), 1);
    }
    return nums.length;
};