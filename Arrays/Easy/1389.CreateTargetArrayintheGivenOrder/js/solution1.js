/**
 * @param {number[]} nums
 * @param {number[]} index
 * @return {number[]}
 */
var createTargetArray = function(nums, index) {
    let result=[]
    for(let number of nums){
        let idx = index.shift();
        result.splice(idx,0,number)
    }
    return result
};