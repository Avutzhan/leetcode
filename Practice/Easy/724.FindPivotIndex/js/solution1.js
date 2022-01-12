/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let sum = nums.reduce((a,b)=>a+b, 0);
    let sumL = 0;
    for(let i=0, len=nums.length; i<len; i++){
        if(sumL === (sum-nums[i])/2) return i;
        sumL += nums[i];
    }
    return -1;
};