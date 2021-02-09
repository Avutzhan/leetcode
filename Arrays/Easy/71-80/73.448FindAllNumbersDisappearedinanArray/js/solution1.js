/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    let length = nums.length
    let arr = []

    for (let i = 0; i < length; i++) {
        arr[i] = i+1
    }

    for (v of nums) {
        arr[v-1] = -1
    }

    return arr.filter( i => (i > 0) )
};