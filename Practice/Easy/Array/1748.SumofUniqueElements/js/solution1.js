/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
    var sum =0;
    let a = new Set(nums);
    for(var t of a.keys()){
        var count =0;
        for(var q =0;q<nums.length;q++){
            if(nums[q]==t) count++;
        }
        if(count<=1) sum+=t;
    }
    return sum;
};
