/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let m1 = 0;
    let m2 = 0;

    for (let i = 0; i < nums.length; i++) {
        m2 = Math.max(m2, Math.min(m1, nums[i]));
        m1 = Math.max(m1, nums[i]);
    }
    return (m1 - 1) * (m2 - 1);
};