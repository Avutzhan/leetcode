/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @param {number} d
 * @return {number}
 */
var findTheDistanceValue = function(arr1, arr2, d) {
    return arr1.reduce((res, curr) => {
        for(const num of arr2) {
            if(Math.abs(curr - num) <= d) return res;
        }
        return res + 1;
    }, 0);
};